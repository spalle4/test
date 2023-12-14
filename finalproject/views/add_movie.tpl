<!DOCTYPE html>
<html>
<head>
    <title>Add Movie</title>
</head>
<body>
    <h2>Add a Movie</h2>
    <form method="post" action="/add">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required><br>
        <label for="star">Star:</label>
        <input type="text" id="star" name="star" required><br>
        <input type="submit" value="Add Movie">
    </form>
    <p><a href="/list">Back to Movies List</a></p>
</body>
</html>
