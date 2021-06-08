from newspaper import Article
import nltk
from gtts import gTTS
import os

article= Article('#URL')
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

mytext = article.text
print(mytext)

language='en'

myobj=gTTS(text=mytext, lang=language, slow=False)

myobj.save('read_article.mp3')

os.system('start read_article.mp3')
