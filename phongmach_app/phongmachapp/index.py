from flask import render_template, request, redirect
import dao
from phongmachapp import app, admin


@app.route('/')
def index():
    categories = dao.load_categories()
    return render_template('index.html', categories=categories)


@app.route('/benhnhan')
def user():
    return render_template('trangBenhNhan.html')


@app.route('/dangkykham', methods=['get', 'post'])
def dangKyLich():
    if request.method.__eq__('POST'):
        print(request.form)
    return render_template('dangKyKham.html')


@app.route('/login', methods=['get', 'post'])
def login_my_user():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        if username.__eq__('admin') and password.__eq__('1'):
            return redirect('/')
    return render_template('login.html')


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
