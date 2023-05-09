#!Python3
import re
import time
import os

param = 0.5 #Parameter für Pausenzeit


#####String-to-List-Funktion
def stringToList(string):
	listRes = list(string.split(" "))
	listRes = [i + ' ' for i in listRes] #Benötigt für Silbenfunktion
	return listRes

#####Silbenzählerfunktion
def silbcount(word):

	while_var = 0
	syllable_count = 0

	while while_var < len(word):
	#	print("now looking at " + str(word[while_var]))
		if(word[while_var] in 'eE' and word[while_var+1] in 'iu'):
			while_var += 2
			syllable_count += 1
		elif(word[while_var] in 'aAäÄ' and word[while_var+1]=='u'):
			while_var += 2
			syllable_count += 1
		elif(word[while_var]=='i' and word[while_var+1]=='e'):
			while_var += 2
			syllable_count += 1
		elif(word[while_var] in 'yaeiouÄÖÜäöüAEIOU'):
			while_var += 1
			syllable_count += 1
		else:
			while_var += 1

	#print('in total the word ' + word + ' has ' + str(syllable_count) + ' syllables')
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

	#####Textformatierung um Fehler zu vermeiden (Alle nicht alphanumerischen Zeichen, außer Leerzeichen, Punkte und Kommata, gehen verloren)
	dicttext = a = re.sub(r'\n', ' ', dicttext)
	dicttext = a = re.sub(r'[^ \w+äöüÄÖÜ.,]', '', dicttext)
	dicttext = a = re.sub(r'\s{2,}', ' ', dicttext)

#####Text in Liste aus Einzelwörtern unterteilen
list_of_words = stringToList(dicttext)

#####Ausführung der Funktionen
starttime = time.time()
for m in range(len(list_of_words)):

	wort_silben = silbcount(list_of_words[m])
	print(list_of_words[m] + ' ' + str(wort_silben))

	w_start = time.time()
	os.system("say " + list_of_words[m])

	delta_t = time.time() - w_start
	sleeptime = 60 * wort_silben / spm - param * wort_silben

	#print('          ' + str(wort_silben) + ' Silben --- ' + str(round(delta_t, 2)) + 's Aussprechen --- ' + str(round(sleeptime,2 )) + 's Sleeptime') #Debugging

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
os.system("say Das Diktat ist zu Ende")
