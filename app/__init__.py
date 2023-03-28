from flask import Flask, render_template, request, url_for
import hashlib

def save_blog(blog_data):
    sha256 = hashlib.sha256()
    sha256.update(f"{blog_data}".encode("utf-8"))
    blog_id = sha256.hexdigest()
    # DATABSE SAVING LEFT
   

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    @app.route("/")
    @app.route("/<name>-<date>")
    def root_route(name = None, date = None):
        if name and date:
            return f"{name} -- {date}"
        return render_template("index.html")

    @app.post("/create_post/")
    def create_post():
        blog_data = request.form
        save_blog(blog_data)
        data = {
            "title" : blog_data.get("title"),
            "author" : blog_data.get("author"),
            "content" : blog_data.get("content")
        }
        return render_template('post.html', data = data)

    return app