import os
from datetime import datetime

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    abort
)

from flask_login import (
    LoginManager,
    login_user,
    current_user,
    logout_user,
    login_required
)

from sqlalchemy import func, or_

from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

from models import db, User, Book, Review


# =========================================
# CONFIGURATION
# =========================================

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////opt/app/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY',
    'dev-secret-key'
)

db.init_app(app)


# =========================================
# LOGIN MANAGER
# =========================================

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'
login_manager.login_message = 'Для этого действия необходимо войти в аккаунт.'


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# =========================================
# HOME PAGE / BOOK CATALOG
# =========================================

@app.route('/')
def index():

    search = request.args.get('q', '').strip()

    query = Book.query

    if search:
        query = query.filter(
            or_(
                Book.title.ilike(f'%{search}%'),
                Book.author.ilike(f'%{search}%')
            )
        )

    books = query.order_by(Book.id.desc()).all()

    # Получаем средний рейтинг и количество отзывов
    ratings = {}

    if books:
        book_ids = [book.id for book in books]

        results = db.session.query(
            Review.book_id,
            func.avg(Review.rating),
            func.count(Review.id)
        ).filter(
            Review.book_id.in_(book_ids)
        ).group_by(
            Review.book_id
        ).all()

        for book_id, average, count in results:
            ratings[book_id] = {
                'average': round(average, 1),
                'count': count
            }

    # Для книг без отзывов
    for book in books:
        if book.id not in ratings:
            ratings[book.id] = {
                'average': None,
                'count': 0
            }

    return render_template(
        'index.html',
        books=books,
        search=search,
        ratings=ratings
    )


# =========================================
# ABOUT
# =========================================

@app.route('/about')
def about():
    return render_template('about.html')


# =========================================
# LOGIN
# =========================================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    if request.method == 'POST':

        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter_by(
            username=username
        ).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            flash('Вы успешно вошли в аккаунт.')

            return redirect(url_for('index'))

        flash('Неверный логин или пароль.')

    return render_template('login.html')


# =========================================
# REGISTER
# =========================================

@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    if request.method == 'POST':

        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        if not username or not email or not password:
            flash('Заполните все поля.')
            return render_template('register.html')

        if len(username) > 50:
            flash('Логин не должен превышать 50 символов.')
            return render_template('register.html')

        if len(email) > 120:
            flash('Email слишком длинный.')
            return render_template('register.html')

        if len(password) < 6:
            flash('Пароль должен содержать минимум 6 символов.')
            return render_template('register.html')

        if User.query.filter_by(username=username).first():
            flash('Такой логин уже занят.')
            return render_template('register.html')

        if User.query.filter_by(email=email).first():
            flash('Этот email уже зарегистрирован.')
            return render_template('register.html')

        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Аккаунт успешно создан. Теперь войдите.')

        return redirect(url_for('login'))

    return render_template('register.html')


# =========================================
# USER PROFILE
# =========================================

@app.route('/profile')
@login_required
def profile():

    books = Book.query.filter_by(
        creator_id=current_user.id
    ).order_by(Book.id.desc()).all()

    return render_template(
        'profile.html',
        user=current_user,
        books=books
    )


# =========================================
# LOGOUT
# =========================================

@app.route('/logout')
@login_required
def logout():

    logout_user()

    flash('Вы вышли из аккаунта.')

    return redirect(url_for('index'))


# =========================================
# BOOK DETAILS
# =========================================

@app.route('/book/<int:book_id>')
def book_detail(book_id):

    book = db.get_or_404(Book, book_id)

    reviews = Review.query.filter_by(
        book_id=book.id
    ).order_by(
        Review.date.desc()
    ).all()

    average_rating = db.session.query(
        func.avg(Review.rating)
    ).filter_by(
        book_id=book.id
    ).scalar()

    return render_template(
        'book_detail.html',
        book=book,
        reviews=reviews,
        average_rating=(
            round(average_rating, 1)
            if average_rating is not None
            else None
        )
    )


# =========================================
# CREATE BOOK
# =========================================

@app.route('/books/new', methods=['GET', 'POST'])
@login_required
def create_book():

    if request.method == 'POST':

        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        description = request.form.get('description', '').strip()

        if not title or not author or not description:
            flash('Заполните все поля.')
            return render_template('book_form.html', book=None)

        if len(title) > 150 or len(author) > 100:
            flash('Название или имя автора слишком длинное.')
            return render_template('book_form.html', book=None)

        book = Book(
            title=title,
            author=author,
            description=description,
            creator_id=current_user.id
        )

        db.session.add(book)
        db.session.commit()

        flash('Книга успешно добавлена.')

        return redirect(
            url_for('book_detail', book_id=book.id)
        )

    return render_template('book_form.html', book=None)


# =========================================
# EDIT BOOK
# =========================================

@app.route('/book/<int:book_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):

    book = db.get_or_404(Book, book_id)

    if book.creator_id != current_user.id:
        abort(403)

    if request.method == 'POST':

        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        description = request.form.get('description', '').strip()

        if not title or not author or not description:
            flash('Заполните все поля.')
            return render_template('book_form.html', book=book)

        if len(title) > 150 or len(author) > 100:
            flash('Название или имя автора слишком длинное.')
            return render_template('book_form.html', book=book)

        book.title = title
        book.author = author
        book.description = description

        db.session.commit()

        flash('Книга обновлена.')

        return redirect(
            url_for('book_detail', book_id=book.id)
        )

    return render_template('book_form.html', book=book)


# =========================================
# DELETE BOOK
# =========================================

@app.route('/book/<int:book_id>/delete', methods=['POST'])
@login_required
def delete_book(book_id):

    book = db.get_or_404(Book, book_id)

    if book.creator_id != current_user.id:
        abort(403)

    db.session.delete(book)
    db.session.commit()

    flash('Книга удалена.')

    return redirect(url_for('index'))


# =========================================
# ADD OR UPDATE REVIEW
# =========================================

@app.route('/book/<int:book_id>/review', methods=['POST'])
@login_required
def add_review(book_id):

    book = db.get_or_404(Book, book_id)

    text = request.form.get('text', '').strip()
    rating = request.form.get('rating', type=int)

    if not text:
        flash('Введите текст отзыва.')
        return redirect(
            url_for('book_detail', book_id=book.id)
        )

    if rating is None or rating < 1 or rating > 5:
        flash('Оценка должна быть от 1 до 5.')
        return redirect(
            url_for('book_detail', book_id=book.id)
        )

    review = Review.query.filter_by(
        user_id=current_user.id,
        book_id=book.id
    ).first()

    if review:

        review.text = text
        review.rating = rating
        review.date = datetime.utcnow()

        flash('Ваш отзыв обновлён.')

    else:

        review = Review(
            text=text,
            rating=rating,
            user_id=current_user.id,
            book_id=book.id
        )

        db.session.add(review)

        flash('Отзыв успешно добавлен.')

    db.session.commit()

    return redirect(
        url_for('book_detail', book_id=book.id)
    )


# =========================================
# START APPLICATION
# =========================================

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(
        host='0.0.0.0',
        port=5000
    )
