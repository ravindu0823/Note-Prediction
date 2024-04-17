import array
from collections import Counter
import numpy as np
import scipy
from pydub.utils import get_array_type
from Levenshtein import distance

NOTES = {
    "C4": 261.6255653005986,
    "C#4": 277.18263097687196,
    "D4": 293.6647679174076,
    "D#4": 311.1269837220809,
    "E4": 329.6275569128699,
    "F4": 349.2282314330039,
    "F#4": 369.9944227116344,
    "G4": 391.99543598174927,
    "G#4": 415.3046975799451,
    "A4": 440,
    "A#4": 466.1637615180899,
    "B4": 493.8833012561241,
    "C5": 523.2511306011972,
    "C#5": 554.3652619537442,
    "D5": 587.3295358348151,
    "D#5": 622.2539674441618,
    "E5": 659.2551138257398,
    "F5": 698.4564628660078,
    "F#5": 739.9888454232688,
    "G5": 783.9908719634985,
    "G#5": 830.6093951598903,
    "A5": 880.0,
    "A#5": 932.3275230361799,
    "B5": 987.7666025122483,
    "C6": 1046.5022612023945
}


def frequency_spectrum(sample, max_frequency=800):
    bit_depth = sample.sample_width * 8
    array_type = get_array_type(bit_depth)
    raw_audio_data = array.array(array_type, sample._data)
    n = len(raw_audio_data)
    if n == 0:
        raise ValueError("The audio data is empty. Cannot compute frequency spectrum.")

    freq_array = np.arange(n) * (float(sample.frame_rate) / n)
    freq_array = freq_array[: (n // 2)]  # one side frequency range

    raw_audio_data = raw_audio_data - np.average(raw_audio_data)  # zero-centering
    # fft computing and normalization
    freq_magnitude = np.fft.fft(raw_audio_data)
    freq_magnitude = freq_magnitude[: (n // 2)]  # one side

    if max_frequency:
        max_index = int(max_frequency * n / sample.frame_rate) + 1
        freq_array = freq_array[:max_index]
        freq_magnitude = freq_magnitude[:max_index]

    freq_magnitude = abs(freq_magnitude)
    freq_magnitude = freq_magnitude / np.sum(freq_magnitude)
    return freq_array, freq_magnitude


def classify_note_attempt_3(freq_array, freq_magnitude):
    min_freq = 82
    note_counter = Counter()
    for i in range(len(freq_magnitude)):
        if freq_magnitude[i] < 0.01:
            continue

        for freq_multiplier, credit_multiplier in [
            (1, 1),
            (1 / 3, 3 / 4),
            (1 / 5, 1 / 2),
            (1 / 6, 1 / 2),
            (1 / 7, 1 / 2),
        ]:
            freq = freq_array[i] * freq_multiplier
            if freq < min_freq:
                continue
            note = get_note_for_freq(freq)
            if note:
                note_counter[note] += freq_magnitude[i] * credit_multiplier

    return note_counter.most_common(1)[0][0]


def get_note_for_freq(f, tolerance=33):
    # Calculate the range for each note
    tolerance_multiplier = 2 ** (tolerance / 1200)
    note_ranges = {
        k: (v / tolerance_multiplier, v * tolerance_multiplier) for (k, v) in NOTES.items()
    }

    # Get the frequence into the 440 octave
    range_min = note_ranges["A4"][0]
    range_max = note_ranges["C6"][1]
    if f < range_min:
        while f < range_min:
            f *= 2
    else:
        while f > range_max:
            f /= 2

    # Check if any notes match
    for (note, note_range) in note_ranges.items():
        if f > note_range[0] and f < note_range[1]:
            return note
    return None


def calculate_distance(predicted, actual):
    def transform(note):
        if "#" in note:
            return note[0].upper()
        return note.lower()

    return distance(
        "".join([transform(n) for n in predicted]), "".join(
            [transform(n) for n in actual]),
    )
