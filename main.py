import autochord
import numpy
# autochord.recognize('final.wav', lab_fn='chords.lab')

# print(autochord.recognize('final.wav'))

data = autochord.recognize("final.wav")
print(data)
