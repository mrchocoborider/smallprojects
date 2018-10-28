import re

#check for alphabet
reg = re.compile(r'[a-zA-Z]+')

f = open('Zhongwen-Words.txt', 'r')

text = f.read().decode('utf-8')


#create an object that takes in a zhongwen formatted word list, and returns a dictionary of chinese word keys and English definition values
class WordList:
    
    def __init__(self, zwlist):
        #self.zwdict = {}
        self.wordarray = []
        self.set_words(zwlist)
     
    #We need an array of dictionaries with keys: Chinese word, Pronunciation, and Definition
    def set_words(self, zwlist):
        start_index = 0
        current_index = 0
        worddict = {}
        for z in zwlist:
            current_index += 1
            if z == '\t':
                word = zwlist[start_index:current_index - 1]
                start_index = current_index
                #if it has alphabet in it then it's pinyin
                if reg.search(word) == None:
                    worddict['hanzi'] = word
                #if not it's hanzi (character)
                else:
                    worddict['pinyin'] = word
                        
                #saving in an array until I figure out how to set up the dictionary
                #self.wordarray.append(word)
            elif z == '\r':
                #this one will be the definition, because it appears last before the new line
                word = zwlist[start_index:current_index - 1]
                start_index = current_index
                worddict['definition'] = word
                #put the filled out word dictionary into the array
                self.wordarray.append(worddict)
                
            elif z == '\n':
                #\r and \n appear together, so just skip over the \n
                start_index += 1
                
    #generate the html table from the words in the list!
    def make_html(self):            
            
                

           
                
#try it out
tio = WordList(text).wordarray
print(tio[:10])


