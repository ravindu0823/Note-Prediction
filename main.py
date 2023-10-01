from music21 import stream, chord, note
from music21.stream.base import Score
from music21.stream.base import Measure

score = Score()

chord_data = [
    (4.040272108843538, 5.944308390022676, "D"),
    (5.944308390022676, 8.17342403628118, "B"),
    (8.17342403628118, 10.263219954648527, "E"),
    (10.263219954648527, 12.538775510204083, "Gb")
    # (12.538775510204083, 14.303492063492063, "D:maj")
    # (14.303492063492063, 16.532607709750568, "B:min")
]

# dMaj = chord.Chord(['D', 'f', 'a'])
# print(dMaj)

# Print the chord of chord data
for start_time, end_time, chord_symbol in chord_data:
    # Create a chord or note object depending on the chord symbol
    if ":" in chord_symbol:
        chord_parts = chord_symbol.split(":")
        new_chord = chord.Chord(chord_parts)
    else:
        new_chord = note.Note(chord_symbol)

    # Set the duration of the chord or note
    # new_chord.duration.quarterLength = end_time - start_time

    # Add the chord or note to a new measure in the score
    new_measure = Measure()
    new_measure.append(new_chord)
    score.append(new_measure)

notation_file_path = "your_notation_file.xml"
score.write("xml", notation_file_path)

if not score.isWellFormedNotation():
    print("The MusicXML file is not well-formed.")
else:
    print("The MusicXML file is well-formed.")