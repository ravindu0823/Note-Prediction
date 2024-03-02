import autochord as chord
# from spleeter.separator import Separator

# separator = Separator('spleeter:2stems')
# separator.separate_to_file('audio/final.wav', 'audio/spleeter/')

# print()
print(chord.recognize("audio/Christina-Perri-A-Thousand-Years-Official-Music-Video.mp3", lab_fn="lab-files/Christina-Perri-A-Thousand-Years-Official-Music-Video-chords.lab"))