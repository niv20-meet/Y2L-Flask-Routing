from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import query_all

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/')
def home_page():
	return render_template("home.html")

@app.route('/store')
def store_page():
	return render_template("store.html")

@app.route('/cart')
def cart_page():
	return render_template("cart.html",items=query_all()) 
@app.route('/about')
def about_page():
	return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)