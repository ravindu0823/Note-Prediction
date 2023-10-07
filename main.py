from music21 import *
from utils import (
    CHORD_DATA
)

environment.set(
    "musicxmlPath", "/home/dhanu/.local/bin/MuseScore-4.1.1.232071203-x86_64.AppImage")
environment.set("musescoreDirectPNGPath",
                "/home/dhanu/.local/bin/MuseScore-4.1.1.232071203-x86_64.AppImage")

# Lead lab file
file_path = 'final.lab'

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
# s.write('musicxml.png', "images/musicxml.png")