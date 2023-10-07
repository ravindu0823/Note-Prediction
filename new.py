from music21 import *
from utils import (
    CHORD_DATA
)
import autochord

environment.set(
    "musicxmlPath", "/home/dhanu/.local/bin/MuseScore-4.1.1.232071203-x86_64.AppImage")
environment.set("musescoreDirectPNGPath",
                "/home/dhanu/.local/bin/MuseScore-4.1.1.232071203-x86_64.AppImage")
""" 
# configure.run()
s = stream.Stream()
s.append(meter.TimeSignature('4/4'))
s.append(note.Rest(type='whole'))
s.append(note.Note('C4', type='quarter'))
s.append(note.Note('D4', type='quarter'))
s.append(note.Note('E4', type='quarter'))
s.append(note.Note('F4', type='quarter'))
s.append(note.Note('G4', type='quarter'))
s.append(note.Note('A4', type='quarter'))
s.append(note.Note('B4', type='quarter'))
s.append(note.Note('C5', type='quarter'))
s.append(note.Note('D5', type='quarter'))
s.append(note.Note('E5', type='quarter'))
s.append(note.Note('F5', type='quarter'))
s.append(note.Note('F5', type='quarter'))
s.append(note.Note('F5', type='quarter'))
s.append(note.Note('F5', type='quarter'))
s.append(note.Note('F5', type='quarter'))
s.append(note.Note('F5', type='quarter'))
s.append(note.Note('F5', type='quarter'))
s.append(note.Note('F5', type='quarter'))
s.append(note.Note('F5', type='quarter'))
s.append(note.Note('F5', type='quarter'))
# s.show()
# Save as an image file
s.write('musicxml.png', fp='images/musicxml.png')
 """

# score = converter.parse('your_notation_file.xml')
# stream_to_save = stream.Stream()
# stream_to_save.append(score)

# stream_to_save.show('musicxml.png')


# print(chord.Chord(CHORD_DATA["A:min"], duration=duration.Duration(2.32)))


""" b = corpus.parse('bwv66.6')
bChords = b.chordify()
bChords.show() """


autochord.recognize("audio1.mp3", "audio1.lab")