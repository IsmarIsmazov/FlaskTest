from flask import Flask, render_template, url_for, request

app = Flask(__name__)
menu = [{'name': 'Установка', 'url': 'install-Flask'},
        {'name': 'Первое приложение', 'url': 'first-app'},
        {'name': 'обратная связь', 'url': 'contact'}]


@app.route('/')
def index():
    # print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    # print(url_for('about'))
    return render_template('about.html', title="О нас", menu=menu)


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form)
    return render_template("contact.html", title="Обратная связь", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь - {username}"


if __name__ == '__main__':
    app.run()
