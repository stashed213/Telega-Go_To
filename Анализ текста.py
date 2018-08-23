import nltk
from pymorphy2 import MorphAnalyzer
nltk.download('point')
morph=MorphAnalyzer()
souls=[]
dict_souls={}
with open('new.txt') as anek:
  anekdoty= anek.read()
  tokens=nltk.word_tokenize(anekdoty)
for token in tokens:
  words=morph.parse(token)
  first=words[0]
  if first.tag.animacy=='anim':
    souls.append(first.normal_form)
souls.sort()

for soul in souls:
  num=souls.count(soul)
  dict_souls[soul]=num
souls_list=dict_souls.items()
for word, count in sorted(souls_list, key=lambda x:x[1], reverse=True):
    print("{} - {}".format(word, count))