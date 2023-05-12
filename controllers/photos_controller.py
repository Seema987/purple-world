from flask import render_template, request, redirect
from models.photo import all_photos, get_photo, create_photo, update_photo, delete_photo, comment_photo
from services.session_info import current_user

def index():
    photos = all_photos()
   
    
    return render_template('photos/index.html', photos=photos, current_user=current_user)

def new():
    return render_template('photos/new.html')

def create():
    name = request.form.get('name')
    image_url = request.form.get('image_url')
    create_photo(name, image_url)
    return redirect('/')


def edit(id):
    photo = get_photo(id)
    return render_template('photos/edit.html', photo=photo)

    

def update(id):
    name = request.form.get('name')
    image_url = request.form.get('image_url')
    update_photo(id, name, image_url)
    return redirect('/')
   

def delete(id):
  delete_photo(id)
  return redirect('/')

def comment(id):
    user_comment = request.form.get('user_comment')
    print(f' My user comments is {user_comment}')
    comment_photo(id, user_comment)
    return redirect('/')

