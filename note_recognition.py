import argparse
from pydub import AudioSegment
import pydub.scipy_effects
import numpy as np
import scipy
import matplotlib.pyplot as plt

from utils import (
    frequency_spectrum,
    classify_note_attempt_3,
)


def main(
    file, note_file=None, note_starts_file=None, plot_starts=False, plot_fft_indices=[]
):
    # If a note file and/or actual start times are supplied read them in
    actual_starts = []
    if note_starts_file:
        with open(note_starts_file) as f:
            for line in f:
                actual_starts.append(float(line.strip()))

    actual_notes = []
    if note_file:
        with open(note_file) as f:
            for line in f:
                actual_notes.append(line.strip())

    song = AudioSegment.from_file(file)
    song = song.high_pass_filter(80, order=4)

    starts = predict_note_starts(song)

    predicted_notes = predict_notes(song, starts)

    print()
    print("Predicted Notes")
    print(predicted_notes)
    # print(starts)


# Returns perdicted starts in ms
def predict_note_starts(song):
    # Size of segments to break song into for volume calculations
    SEGMENT_MS = 50
    # Minimum volume necessary to be considered a note
    VOLUME_THRESHOLD = -35
    # The increase from one sample to the next required to be considered a note
    EDGE_THRESHOLD = 5
    # Throw out any additional notes found in this window
    MIN_MS_BETWEEN = 100

    # Filter out lower frequencies to reduce noise
    song = song.high_pass_filter(80, order=4)
    # dBFS is decibels relative to the maximum possible loudness
    volume = [segment.dBFS for segment in song[::SEGMENT_MS]]

    predicted_starts = []
    for i in range(1, len(volume)):
        if volume[i] > VOLUME_THRESHOLD and volume[i] - volume[i - 1] > EDGE_THRESHOLD:
            ms = i * SEGMENT_MS
            # Ignore any too close together
            if (
                len(predicted_starts) == 0
                or ms - predicted_starts[-1] >= MIN_MS_BETWEEN
            ):
                predicted_starts.append(ms)

    return predicted_starts


def predict_notes(song, starts):
    notes_with_times = []
    for i, start in enumerate(starts):
        temp = ()
        sample_from = start + 50
        sample_to = start + 550
        if i < len(starts) - 1:
            sample_to = min(starts[i + 1], sample_to)
        segment = song[sample_from:sample_to]
        freqs, freq_magnitudes = frequency_spectrum(segment)

        predicted = classify_note_attempt_3(freqs, freq_magnitudes)

        # convert ms to seconds
        start_in_seconds = start / 1000

        # temp = temp + (start_in_seconds, predicted or "U")
        # notes_with_times.append(temp)

        # Get note end time
        if i < len(starts) - 1:
            end = starts[i + 1]
        else:
            end = len(song)

        end_in_seconds = end / 1000

        temp = temp + (start_in_seconds, end_in_seconds, predicted or "U")
        notes_with_times.append(temp)

    return notes_with_times


if __name__ == "__main__":
    main(
        "audio/acc.mp3",
        note_file="",
        note_starts_file="",
        plot_starts=False,
        plot_fft_indices=[],
    )
