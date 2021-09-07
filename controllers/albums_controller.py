from flask import Flask, render_template, redirect
from flask import Blueprint, request
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

albums_blueprint = Blueprint("albums", __name__)

# GET albums
@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("/albums/index.html", albums = albums)

@albums_blueprint.route("/albums/<id>", methods = ["GET"])
def show_album(id):
    album = album_repository.select(id)
    return render_template("/albums/show.html", album = album)

@albums_blueprint.route("/albums/<id>/delete", methods=['POST'])
def delete_album(id):
    album_repository.delete(id)
    return redirect('/albums')

# Tried to make a CREATE but couldn't get it to work 
@albums_blueprint.route("/albums", methods=['POST'])
def add_album():
    album_title = request.form['title']
    album_artist = request.form['artist']
    album_year = request.form['year']
    album_stock = request.form['stock_level']
    artist = Artist(album_artist)
    artist_repository.save(artist)
    new_album = Album(album_title, artist, album_year, album_stock)
    album_repository.save(new_album)
    return render_template('/albums/index.html')






