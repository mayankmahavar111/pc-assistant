from SpeechRecognition import speech
from sel import search

text =speech()
print(text)
text=text.split(" ")
if text[0] == 'search':
    temp=' '.join(text[1:])
    search(temp)