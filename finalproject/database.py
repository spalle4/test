import sqlite3

connection = sqlite3.connect("movies.db")

def get_movies(id=None):
    cursor = connection.cursor()
    if id is None:
        rows = cursor.execute("select id, title, star from movies")
    else:
        rows = cursor.execute(f"select id, title, star from movie where id={id}")

    rows = list(rows)
    rows = [{'id': row[0], 'title': row[1], 'star': row[2]} for row in rows]
    return rows

def setup_database():
    cursor = connection.cursor()
    try:
        cursor.execute("drop table movie")
    except:
        pass
    cursor.execute("create table movie(id integer primary key, title text, star text)")
    for movie in [('The Matrix', 'Keanu Reeves'), ('Inception', 'Leonardo DiCaprio'), ('Jurassic Park', 'Sam Neill'),
                  ('The Shawshank Redemption', 'Tim Robbins'), ('Forrest Gump', 'Tom Hanks')]:
        cursor.execute(f"insert into movie (title, star) values (?, ?)", movie)
    connection.commit()

def add_movie(title, star):
    cursor = connection.cursor()
    cursor.execute("insert into movie (title, star) values (?, ?)", (title, star))
    connection.commit()

def delete_movie(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from movie where id={id}")
    connection.commit()

def update_movie(id, title, star):
    cursor = connection.cursor()
    cursor.execute(f"update movie set title=?, star=? where id={id}", (title, star))
    connection.commit()

def test_get_movies():
    print("testing get_movies()")
    movies = get_movies()
    assert type(movies) is list
    assert len(movies) > 0
    for movie in movies:
        assert 'id' in movie
        assert type(movie['id']) is int
        assert 'title' in movie
        assert type(movie['title']) is str
        assert 'star' in movie
        assert type(movie['star']) is str
    example_id = movies[0]['id']
    example_title = movies[0]['title']
    example_star = movies[0]['star']
    movies = get_movies(example_id)
    assert len(movies) == 1
    assert example_id == movies[0]['id']
    assert example_title == movies[0]['title']
    assert example_star == movies[0]['star']

# ... (similar changes for other test functions)

if __name__ == "__main__":
    test_get_movies()
    test_setup_database()
    test_add_movie()
    test_delete_movie()
    test_update_movie()
    print("done.")
