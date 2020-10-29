import pyttsx3
speaker = pyttsx3.init()
f=open("D:\\audio_books.txt",'r')
f.seek(0)
b=f.tell()
c=f.readlines(b)
try:
    for i in range (100):
        speaker.say(c[i])
        speaker.runAndWait()
except IndexError:
     print('')

  



