import pyttsx3
import time


engine = pyttsx3.init()
#rate = engine.getProperty('rate')

#####String-to-List-Funktion
def stringToList(string):
    listRes = list(string.split(" "))
    listRes = [i + ' ' for i in listRes] #Cheat, um Doppelvokalkomposita händeln zu können
    return listRes

#####Silbenzählerfunktion
def silbcount(word):

	while_var=0
	syllable_count=0

	while while_var < len(word):
	#    print("now looking at " + str(word[while_var]))
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


	    elif(word[while_var]=='a' or 
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
	            while_var = while_var +1
	        
	    else:
	        while_var +=1

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


#####Diktiertext
with open('diktat.txt', 'r', encoding='utf-8') as file:
    dicttext = file.read().rstrip()


#####Text in Liste aus Einzelwörtern unterteilen
list_of_words=stringToList(dicttext)


for m in range(len(list_of_words)):
    print(list_of_words[m])

    engine.say(list_of_words[m])
    engine.runAndWait()

    wort_silben=silbcount(list_of_words[m])
    sleeptime=60*wort_silben/spm - 0.6*wort_silben

#    print(str(sleeptime)+ '\n') #Debugging

    time.sleep(sleeptime)


#####Ende
print('Das Diktat ist zu Ende.')
engine.say('Das Diktat ist zu Ende.')
engine.runAndWait()
