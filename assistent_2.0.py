import speech_recognition as sr
import pyttsx3
import pyaudio
import os
import wikipedia


opt = {
	'Name':(
		'колян' , 'калыван' , 'колываныч' , 'коляныч'
		),


	'Words':(
		'калыван' , 'пк' , 'компьютер' , 'ноутбук' , 'можешь' , 'сможешь' , 'Включи' , ',' , 'включи'
		)
}



''' Словарь команд '''
command = {

	'Shutdown':(
		'выключить' , 'отключить' , 'выключи' , 'отключи','включить','Включи' , 'Выключи'
		),


	'Google':(
		'Chrome' , 'Google'
		),


	'Wiki':(
		'Wikipedia' , 'Википедия' , 'Википедию'
		)
}


class Main():
	'''Главный класс'''
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate' , 170)


	def say(vote):
		''' Говорить '''
		vote.say('Здравствуй,повелитель! Колыван Вас слушает') 
		vote.runAndWait()


	def speech_r(vote):
		'''Прослушивание и очистка речи'''
		for index, name in enumerate(sr.Microphone.list_microphone_names()):
			print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


		r = sr.Recognizer()
		m = sr.Microphone(device_index = 2)

		''' Распознание речи '''
		try:
			with m as source:
				print('Говорите...')

				audio = r.listen(source)
	
				global recognize
				recognize = str(r.recognize_google(audio , language = 'ru-RU'))

				print('Сказано:' + recognize)


		except sr.UnknownValueError:
			vote.say('Я Вас не понял')


		except sr.RequestError as e:
			vote.say('Нет подключения к Интернету')

		''' Убираем лишние слова  '''

		for i in opt['Name'] and opt['Words']:
			if i in recognize:
				recognize = recognize.replace(i , '')
				recognize = ''.join(recognize.split(
					))
		

		return recognize


	def command(vote):
		'''Выполнение команды'''
		print('Анализ')
		print(recognize)

		if recognize in command['Google']:
			vote.say('Выполняю...')

			path = '"C:\Google Chrome.lnk"'

			return os.system(path)


		elif recognize in command['Shutdown']:
			vote.say('Выполняю...')
			os.system('shutdown /p')


		elif recognize in command['Wiki']:
			vote.say('Что найти?')

			search = str(input('Введите:'))

			wikipedia.summary(search)

		else:
			vote.say('Нет такой команды')

	if __name__ == '__main__':
		say(engine)
		speech_r(engine)
		command(engine)

Main()