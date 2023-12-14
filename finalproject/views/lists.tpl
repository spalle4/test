<!DOCTYPE html>
<html>
<head>
    <title>Movies List</title>
</head>
<body>
    <h2>Movies List</h2>
    <ul>
        % for movie in movie_list:
            <li>
                <strong>${movie['title']}</strong> starring ${movie['star']}
                [<a href="/update/${movie['id']}">Edit</a>]
                [<a href="/delete/${movie['id']}">Delete</a>]
            </li>
        % end
    </ul>
    <p><a href="/add">Add a Movie</a></p>
</body>
</html>
