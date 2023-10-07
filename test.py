from music21 import *
from utils import (
    CHORD_DATA
)

""" # Create a new score
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
n.show() """

file_path = 'charitha.lab'

# Initialize an empty list to store the data
data = []

# Open the file and read it line by line
with open(file_path, 'r') as file:
    for line in file:
        # Split the line by tab to separate the columns
        columns = line.strip().split('\t')

        # Convert start and end times to float and store them as a tuple with the label
        if len(columns) == 3:
            start_time = float(columns[0])
            end_time = float(columns[1])
            label = columns[2]
            data.append((start_time, end_time, label))


# s = stream.Stream()
# s.append(meter.TimeSignature('4/4'))

# for start_time, end_time, label in data:
#     # print("duration {}".format("{:.2f}".format(end_time - start_time)))
#     # print("label {}".format(CHORD_DATA[label]))
#     time = (end_time - start_time).__round__(2)
#     # print(chord.Chord(CHORD_DATA[label], duration=duration.Duration(time)))
#     s.append(chord.Chord(CHORD_DATA[label], duration=duration.Duration(time)))

#     # Create a new chord or note object depending on the label
#     """ if ":" in label:
#         chord_parts = label.split(":")
#         new_chord = chord.Chord(chord_parts)
#     else:
#         new_chord = note.Note(label)

#     # Set the duration of the chord or note
#     new_chord.duration.quarterLength = end_time - start_time

#     # Add the chord or note to a new measure in the score
#     new_measure = stream.Measure()
#     new_measure.append(new_chord)
#     score.append(new_measure) """

# s.show()

s = stream.Score()
s.append(meter.TimeSignature('4/4'))

for start_time, end_time, label in data:
    time = (end_time - start_time).__round__(2)
    # print(chord.Chord(CHORD_DATA[label], duration=duration.Duration(time)))
    new_chord = chord.Chord(CHORD_DATA[label], duration=duration.Duration(time))

    new_measure = stream.Measure()
    new_measure.append(new_chord)
    s.append(new_measure)

s.show()