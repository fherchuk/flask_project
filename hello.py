from flask import Flask, render_template


#Instance
app = Flask(__name__)

#Route decorator
@app.route('/')

def index():
    stuff = "<strong>Bold</strong> Text"
    return render_template("index.html", stuff=stuff)

# localhost:5000/user/Rick
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
        return render_template("404.html"), 404


#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
        return render_template("500.html"), 500