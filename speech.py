import speech_recognition as sr
import time
r = sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("Speak")
	time_before = time.time
	audio = r.listen(source)
	print("Processing")
	try:
		text = r.recognize_google(audio)
		print(text)
	except:
		print("It did not work")
