#coding=utf-8
import re


#check for alphabet
reg = re.compile(r'[a-zA-Z]+')

f = open('Zhongwen-Words.txt', 'r')

text = f.read().decode('utf-8')

wordarray = []

    

    
#We need an array of dictionaries with keys: Chinese word, Pronunciation, and Definition
def set_words(zwlist):
    #print(zwlist)
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
                    
            
        elif z == '\r':
            #this one will be the definition, because it appears last before the new line
            word = zwlist[start_index:current_index - 1]
            start_index = current_index
            worddict['definition'] = word
            #put the filled out word dictionary into the array
            wordarray.append(worddict)
            
        elif z == '\n':
            #\r and \n appear together, so just skip over the \n
            start_index += 1
            worddict = {}
    print(wordarray)
    make_html()       

#generate the html table from the words in the list!
def make_html():    
    g = open('vocab.html', 'w+')

    head = u"""
    <link rel="stylesheet" href="style.css">
    <table id="t01" style="width:60%">
        <tr>
            <th>生词</th> 
            <th>定义</th>
        </tr>"""

    for i in wordarray:
        new_row = u"""
        <tr>
            <td>{}, {}</td>
            <td>{}</td>
        </tr>""".format(i['hanzi'], i['pinyin'], i['definition'])
        head += new_row
    #print self.wordarray

    g.write(head.encode('utf-8'))

#Generating the HTML works like a charm, now I need to work on the word array part, I thought it was working well, but it turns out it's just grabbing the first definition?
#Might be because I'm using a class, it would be helpful to revisit the class article and see why I did that in the first place, might want to rewrite as just a set of functions. The class structure might be more trouble
#than it's worth for this.
#I also want to learn to check out the master version of this code to see if it worked then. That will also provide a useful git lesson.


#try it out
#tio = WordList(text).wordarray
set_words(text)
#make_html()
#print(zwlist)


