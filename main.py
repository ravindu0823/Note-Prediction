import autochord as chord
# from spleeter.separator import Separator

# separator = Separator('spleeter:2stems')
# separator.separate_to_file('audio/final.wav', 'audio/spleeter/')

# print()
print(chord.recognize("audio/A-Thousand-Years-Christina-Perri.mp3", lab_fn="lab-files/A-Thousand-Years-Christina-Perri-chords.lab"))