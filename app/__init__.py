from flask import Flask, render_template, request, redirect
import hashlib

def save_blog(blog_data):
    sha256 = hashlib.sha256()
    sha256.update(f"{blog_data}".encode("utf-8"))
    blog_id = sha256.hexdigest()
    # DATABSE SAVING LEFT

def get_blog_data(blog_route):
    return { "author": "qwerty", "story": "New\n\n\npost", "title": "NEW post" }   

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    @app.get("/")
    def root_route():
        return render_template("index.html")

    @app.post("/create_post/")
    def create_post():
        blog_data = request.get_json()
        blog_route = save_blog(blog_data)
        return redirect(f"/{blog_route}")
    
    @app.get('/<blog_route>')
    def get_blog(blog_route):
        blog_data = get_blog_data(blog_route)
        return render_template("post.html", blog_data = blog_data)

    return app