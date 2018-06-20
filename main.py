from bottle import route, request, static_file, get, run
from gtts import gTTS
from pygame import mixer
from random import randint
import os
import time

@route('/')
def main():
    return static_file("index.html", root="./")

@get("/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./")

@route('/playtts', method='POST')
def getaudio():
    stuff = request.forms.get('stuff')
    filename = str(randint(0,999)) + ".mp3"
    tts = gTTS(text=stuff, lang='en', slow=False)
    tts.save('./' + filename)
    mixer.init()
    mixer.music.load('./' + filename)
    mixer.music.play()
    return ("<span> you said " + stuff + " with the file name " + filename + "</span>")


run(host='localhost', port=8080, debug=True)