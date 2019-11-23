#Simple Flask application. base.html,signup_form.html,thank_you.html,error_404.html are this app files
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/signup_form")
def signup_form():
	return render_template("signup_form.html")

@app.route("/thank_you")
def thank_you():
	first = request.args.get("first")
	last = request.args.get("last")
	return render_template("thank_you.html",first=first,last=last)

@app.errorhandler(404)
def error(e):
	return render_template("error_404.html"),404

if __name__ == "__main__":
	app.run(debug=True)


