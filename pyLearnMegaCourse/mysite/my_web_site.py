from flask import Flask, render_template

app = Flask(__name__)

#add decorators
@app.route('/')
def home():
    return "This is home page for the website"

@app.route('/about/')
def about():
    return " This is about page for the website"

if __name__ == "__main__":
    app.run(debug=True)
