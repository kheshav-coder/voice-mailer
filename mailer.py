import smtplib
import os
import config
import playsound
import speech_recognition as sr
from gtts import gTTS

def recognise():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            return False

def speak(text):
    voice=gTTS(text=text,lang="en",slow=False)
    file="voice.mp3"
    voice.save(file)
    playsound.playsound(file,True)
    os.remove(file)

def send_mail(to,msg):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(config.email,config.password)
        s.sendmail(config.email,to, msg)
        s.quit()
        print()
        print("message sent successfully")
        speak("message sent successfully")
    except:
        print()
        print("error sending the message")
        speak("error sending the message")

speak("can you please specify the recipant of you mail")
to=recognise()
speak("what is the message you want to send")
msg=recognise()
send_mail(to,msg)
