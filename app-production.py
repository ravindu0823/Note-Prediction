import os
from flask import Flask, request, jsonify
from note_recognition_simplified import main
import autochord as chord
from scrape import getNews
from gevent.pywsgi import WSGIServer
from dotenv import load_dotenv

load_dotenv()
ENV = os.getenv('PYTHON_ENV')
PORT = os.getenv('PORT')

app = Flask(__name__)

@app.route("/analyzeNotes", methods=["POST"])
def analyzeNotes():
    # Get the song file from the form data
    song = request.files["song"]

    # Save the song file to a temporary location
    song.save("uploads/tempNoteSong.mp3")

    # Call the main function from your code with the song file name and a lab file name
    main("uploads/tempNoteSong.mp3", "labuploads/tempNote.lab")

    # Read the contents of the lab file
    with open("labuploads/tempNote.lab", "r") as f:
        lab = f.read()

     # Parse the lab file contents as a list of dictionaries
    data = []
    for line in lab.splitlines():
        start, end, note = line.split()
        data.append({"start": start, "end": end, "note": note})

    # Return the data as JSON
    return jsonify(notes=data)


@app.route("/analyzeChords", methods=["POST"])
def analyzeChords():
    # Get the song file from the form data
    song = request.files["song"]

    # Save the song file to a temporary location
    song.save("uploads/tempChordSong.mp3")

    # Call the main function from your code with the song file name and a lab file name
    chord.recognize("uploads/tempChordSong.mp3", "labuploads/tempChord.lab")

    # Read the contents of the lab file
    with open("labuploads/tempChord.lab", "r") as f:
        lab = f.read()

     # Parse the lab file contents as a list of dictionaries
    data = []
    for line in lab.splitlines():
        start, end, note = line.split()
        data.append({"start": start, "end": end, "note": note})

    # Return the data as JSON
    return jsonify(chords=data)


@app.route("/analyzeBoth", methods=["POST"])
def analyzeBoth():
    # Get the song file from the form data
    song = request.files["song"]

    # Save the song file to a temporary location
    song.save("uploads/song.mp3")

    # Call the main function from your code with the song file name and a lab file name
    chord.recognize("uploads/song.mp3", "labuploads/tempChord.lab")
    main("uploads/song.mp3", "labuploads/tempNote.lab")

    # Read the Chords data
    with open("labuploads/tempChord.lab", "r") as f:
        labChords = f.read()

    # Add this chord data to the data json
    chordData = []
    for line in labChords.splitlines():
        start, end, note = line.split()
        chordData.append({"start": start, "end": end, "note": note})

    with open("labuploads/tempNote.lab", "r") as f:
        labNotes = f.read()

     # Parse the lab file contents as a list of dictionaries
    notesData = []
    for line in labNotes.splitlines():
        start, end, note = line.split()
        notesData.append({"start": start, "end": end, "note": note})

    # Return the data as JSON
    return jsonify(chords=chordData, notes=notesData), 200


@app.route("/getScrapeNews", methods=["GET"])
def getScrapeNews():
    # Call the getNews function from your code
    news = getNews()

    # Return the data as JSON
    return jsonify(news)


if __name__ == '__main__':
    print("ENV", ENV)
    
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    
    if not os.path.exists("labuploads"):
        os.makedirs("labuploads")
    
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
