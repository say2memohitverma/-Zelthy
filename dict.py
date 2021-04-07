import urllib.request as urllib2
import json

word = input("Word? ")

url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/' + word + ''
#url stores the json formatted output from Glosbe


result = json.load(urllib2.urlopen(url))	#json representation of url

print(str(word)+". "+str(result[0]["meanings"][1]["partOfSpeech"])+". "+str(result[0]["meanings"][1]["definitions"][0]["definition"]))
