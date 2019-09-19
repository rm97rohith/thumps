from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return "welcome to my website"

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('home.html')


if(__name__=="__main__"):
    app.run(debug=True)