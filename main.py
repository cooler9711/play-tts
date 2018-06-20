from bottle import route, request, static_file, get, run
from gtts import gTTS
from pygame import mixer

@route('/')
def main():
return static_file("index.html", root="./")

@get("/<filepath:re:.*\.css>")
def css(filepath):
return static_file(filepath, root="./")