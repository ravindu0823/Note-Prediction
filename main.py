import autochord as chord
# from spleeter.separator import Separator

# separator = Separator('spleeter:2stems')
# separator.separate_to_file('audio/final.wav', 'audio/spleeter/')

print(chord.recognize("audio/We_Don't_Talk_Anymore.mp3", lab_fn="lab-files/We_Don't_Talk_Anymore.lab"))