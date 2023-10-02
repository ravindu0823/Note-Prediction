from music21 import *

environment.set(
    "musicxmlPath", "C:\\Program Files\\MuseScore 4\\bin\\MuseScore4.exe")
environment.set("musescoreDirectPNGPath",
                "C:\\Program Files\\MuseScore 4\\bin\\MuseScore4.exe")
""" 
# configure.run()
s = stream.Stream()
s.append(meter.TimeSignature('4/4'))
s.append(note.Rest(type='whole'))
s.append(note.Note('C4', type='quarter'))
# s.show()
# Save as an image file
s.write('musicxml.png', fp='images/musicxml.png')


# score = converter.parse('your_notation_file.xml')
# stream_to_save = stream.Stream()
# stream_to_save.append(score)

# stream_to_save.show('musicxml.png')
 """

# a_note = note.Note("A")
# c_note = note.Note("C")
# e_note = note.Note("E")

# # Create a chord object for the A minor chord
# a_minor_chord = chord.Chord([a_note, c_note, e_note])

# # Show the chord (this will display it in a musical notation)
# a_minor_chord.show()

b = corpus.parse('bwv66.6')
bChords = b.chordify()
bChords.show()