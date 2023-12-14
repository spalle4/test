from bottle import route, post, run, template, redirect, request
import database

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    movies = database.get_movies()
    return template("list.tpl", movie_list=movies)

@route("/add")
def get_add():
    return template("add_movie.tpl")

@post("/add")
def post_add():
    title = request.forms.get("title")
    star = request.forms.get("star")
    database.add_movie(title, star)
    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    database.delete_movie(id)
    redirect("/list")

@route("/update/<id>")
def get_update(id):
    movie = database.get_movie(id)
    if not movie:
        redirect("/list")
    title = movie['title']
    star = movie['star']
    return template("update_movie.tpl", id=id, title=title, star=star)

@post("/update")
def post_update():
    title = request.forms.get("title")
    star = request.forms.get("star")
    id = request.forms.get("id")
    database.update_movie(id, title, star)
    redirect("/list")

run(host='localhost', port=8080)
