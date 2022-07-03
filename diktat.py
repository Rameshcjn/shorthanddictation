#!Python3
import pyttsx3
import time


engine = pyttsx3.init()
param = 0.7 #Parameter für Pausenzeit


#####Einstellungen für TTS
#rate = engine.getProperty('rate')
#engine.setProperty('rate', rate+100)

#voices = engine.getProperty('voices')  
#engine.setProperty('voice', voices[0].id)


#####String-to-List-Funktion
def stringToList(string):
	listRes = list(string.split(" "))
	listRes = [i + ' ' for i in listRes] #Cheat, um Doppelvokalkomposita händeln zu können
	return listRes


#####Silbenzählerfunktion
def silbcount(word):

	while_var = 0
	syllable_count = 0

	while while_var < len(word):
	#	print("now looking at " + str(word[while_var]))
		if(word[while_var]=='e' or word[while_var]=='E' and word[while_var+1]=='i'):
			while_var = while_var + 2
			syllable_count = syllable_count + 1

		elif(word[while_var]=='E' or word[while_var]=='e' and word[while_var+1]=='u'):
			while_var = while_var + 2
			syllable_count = syllable_count + 1

		elif(word[while_var]=='A' or word[while_var]=='a' and word[while_var+1]=='u'):
			while_var = while_var + 2
			syllable_count = syllable_count + 1

		elif(word[while_var]=='Ä' or word[while_var]=='Ä' and word[while_var+1]=='u'):
			while_var = while_var + 2
			syllable_count = syllable_count + 1

		elif(word[while_var]=='i' and word[while_var+1]=='e'):
			while_var = while_var + 2
			syllable_count = syllable_count + 1


		elif(word[while_var]=='y' or # das "y" ist meistens ne eigene Silbe
			word[while_var]=='a' or 
			word[while_var]=='e' or 
			word[while_var]=='i' or 
			word[while_var]=='o' or 
			word[while_var]=='u' or 
			word[while_var]=='A' or 
			word[while_var]=='E' or 
			word[while_var]=='I' or 
			word[while_var]=='O' or 
			word[while_var]=='U' or 
			word[while_var]=='ä' or 
			word[while_var]=='Ä' or 
			word[while_var]=='ö' or 
			word[while_var]=='Ö' or 
			word[while_var]=='Ü' or 
			word[while_var]=='ü'):
				syllable_count = syllable_count + 1
				while_var = while_var + 1

		else:
			while_var += 1

#	print('in total the word ' + word + ' has ' + str(syllable_count) + ' syllables')
	return syllable_count


#####Input
while True:
	try:
		spm=input('Wie viele SPM? zwischen 20 und 100: ')
		spm=float(spm)

		if spm >= 20 and spm <=100:
			break
		elif spm > 100:
			print('Kleiner als 100!\n')
		elif spm < 20:
			print('Größer als 20!\n')

	except ValueError:
		print('Eine Zahl!\n')
print('')

#####Diktiertext
with open('diktat.txt', 'r', encoding='utf-8') as file:
	dicttext = file.read().rstrip()


#####Text in Liste aus Einzelwörtern unterteilen
list_of_words = stringToList(dicttext)


#####Ausführung der Funktionen
starttime = time.time()


for m in range(len(list_of_words)):

	print(list_of_words[m])
	wort_silben = silbcount(list_of_words[m])
		
	w_start = time.time()
	engine.say(list_of_words[m])
	engine.runAndWait()
	w_end = time.time()
		
	#delta_t = w_end - w_start
	delta_t = w_end - w_start
	sleeptime = 60 * wort_silben / spm - param * wort_silben

	print('          ' + str(wort_silben) + ' Silben --- ' + str(round(delta_t, 2)) + 's Aussprechen --- ' + str(round(sleeptime,2 )) + 's Sleeptime') #Debugging

	try:
		time.sleep(sleeptime)
	except ValueError:
		continue
endtime=time.time()


#####Ende
print('')
print('Das Diktat ist zu Ende.')
print('Zeit: ' + str(round(endtime - starttime,2)) + ' Sekunden')
print('Eff SPM: ' + str(round(silbcount(dicttext)/((endtime - starttime)/60))) + '\n')
engine.say('Das Diktat ist zu Ende.')
engine.runAndWait()
