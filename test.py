from music21 import *

# Create a new score
score = stream.Score()

# Create a new part for the score
part = stream.Part()

# Create a new measure for the part
measure = stream.Measure()

# Define the chords to be added to the measure
# chord_symbols = ["C", "G", "A", "F"]

# # Add each chord to the measure
# for chord_symbol in chord_symbols:
#     # Create a new chord object from the chord symbol
#     new_chord = chord.Chord(chord_symbol)

#     # Add the chord to the measure
#     measure.append(new_chord)

# # Add the measure to the part
# part.append(measure)

# # Add the part to the score
# score.append(part)

# # Write the score to a MusicXML file
# notation_file_path = "your_notation_file.xml"
# score.write("xml", notation_file_path)

#  Load the MusicXML file into a new score object
# score = converter.parse("your_notation_file.xml")
# score.show()

n = note.Note("C")
n.quarterLength = 2
n.show()