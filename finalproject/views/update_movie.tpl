<!DOCTYPE html>
<html>
<head>
    <title>Edit Movie</title>
</head>
<body>
    <h2>Edit Movie</h2>
    <form method="post" action="/update">
        <input type="hidden" name="id" value="${id}">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" value="${title}" required><br>
        <label for="star">Star:</label>
        <input type="text" id="star" name="star" value="${star}" required><br>
        <input type="submit" value="Update Movie">
    </form>
    <p><a href="/list">Back to Movies List</a></p>
</body>
</html>
