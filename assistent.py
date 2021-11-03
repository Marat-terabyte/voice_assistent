import pyttsx3
import pyaudio
import speech_recognition as sr
import pyautogui
import os
import wikipedia
import time


hello = [	'Привет' , 'Hello' , 'Holla' , 'Здарова' , 'Здравствуйте' , 'Здраствуйте' , 'Хеллоу'	]
name = [	'Колыван' , 'Колываныч' , 'Колян'	]
commands = [{'Выключить' , 'Отключить' , 'Google' , 'Chrome' , 'Wikipedia' }]

engine = pyttsx3.init()
engine.setProperty ('rate', 130)
engine.say('Здравствуй,повелитель!Колыван Вас слушает!')
engine.runAndWait()


for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


m = sr.Microphone(device_index = 1)
r = sr.Recognizer()

while True:
	with m as source:
		print("Cлушаю!")
		audio = r.listen(source)
		recognize = r.recognize_google(audio)


		if recognize.startswith((hello , name)):
			replace(hello and name , '')


	try:
		print("Вы сказали:" + recognize)
	except sr.UnknownValueError:
		engine.say("Я Вас не понял")
		engine.runAndWait()
	except sr.RequestError as e:
		print("Нет подключения к Интернету; {0}".format(e))



	if commands in recognize:	#Запуск Chrome
		engine.say('Выполняю...')
		engine.runAndWait()
		os.system('"C:\\Users\\User\\Desktop\\Google Chrome.lnk"')


	elif 'Wikipedia' in recognize: #Википедия
		wikipedia.search("Лондон")


	elif 'Выключить' in recognize:	
		os.system('shutdown /s') #Выключить систему


	else:
		print('Я не знаю такую команду')