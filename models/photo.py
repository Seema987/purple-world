from db.db import sql
def all_photos():
    return sql('SELECT * FROM photos')

def get_photo(id):
    photos = sql('SELECT * FROM photos WHERE id = %s', [id])
    return photos[0]

def create_photo(name, image_url):
    sql('INSERT INTO photos(name, image_url) VALUES(%s, %s)RETURNING *', [name, image_url])

def update_photo(id, name, image_url):
    sql('UPDATE photos SET name=%s, image_url=%s WHERE id=%s RETURNING *',[name, image_url, id])

def delete_photo(id):
    sql('DELETE FROM photos WHERE id=%s RETURNING *', [id])

def comment_photo(id, user_comment):
    sql('INSERT INTO comments(user_comment, id) VALUES(%s, %s)RETURNING *', [user_comment, id])