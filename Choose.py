
try:
    import Tkinter as tk
    import ttk
except ImportError:
    import tkinter as tk
    import tkinter.ttk as ttk
from tkinter import *

global str
from PIL import ImageTk, Image
import os
import random
import names
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from random import randint
import nltk.data


root= tk.Tk()
root.geometry("500x500")
root.title("Primary Math")


t=[0,1]
str3=""

def generateQuestion():
        
    
    item = [ 'Pens', 'Books', 'Boxes', 'Chocolates', 'Biscuits', 'Mangos', 'Bananas', 'Dolls', 'Flowers', 'Breads', 'Watches', 'Apples', 'Apricots', 'Avocadoes', 'Blackberries', 'Blueberries', 'Cherries', 'Figs', 'toys', 'kiwi(fruit)', 'lemons', 'oranges','Papers', 'Peaches', 'pears', 'pineapples', 'plums', 'raspberries', 'strawberries', 'watermelons']
    z = (random.choice(item))
    addition = ['originally', 'in the first', 'in the beginning', 'earlier', 'to begin with', 'primitively', 'at first', 'initially', 'incipiently']
    az1 = (random.choice(addition))




    def multiwordReplace(text, wordDic):
        """
        take a text and replace words that match a key in a dictionary with
        the associated value, return the changed text
        """
        rc = re.compile('|'.join(map(re.escape, wordDic)))

        def translate(match):
            return wordDic[match.group(0)]

        return rc.sub(translate, text)


    p1 = random.randint(2, 9)
    p2 = random.randint(10, 50)
    q = str(p1)
    x = str(p2)


#    def get_name(filename):
#        selected = random.random() * 90
#        with open(filename) as name_file:
#            for line in name_file:
#                name, _, cummulative, _ = line.split()
#                if float(cummulative) > selected:
#                    return name


    def get_first_name(gender=None):
        if gender not in ('male', 'female'):
            gender = random.choice(('male', 'female'))
        return get_name(FILES['first:%s' % gender]).capitalize()


    def get_last_name():
        return get_name(FILES['last']).capitalize()


    def get_full_name(gender=None):
        return u"%s %s" % (get_first_name(gender), get_last_name())


    tn = (names.get_first_name())
    p = (names.get_first_name())

    str1 = """John had some marbles, 
    Jim gave him 3 more, 
    Now John has 8 marbles. 
    How many marbles did John 
    have to begin with ?"""
    # the dictionary has target_word : replacement_word pairs
    # print (str1)
    wordDic = {
        'John': tn,
        'marbles': z,
        'Jim': p,
        '3': q,
        '8': x,
        'to begin with' : az1}
    # call the function and get the changed text
    str2 = multiwordReplace(str1, wordDic)
    str3 = (str2)
    #print (str2)
    output = ""

    #synset library for changing the nouns, vowels etc.
    # Load the pretrained neural net

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    # Tokenize the text
    tokenized = tokenizer.tokenize(str3)

    # Get the list of words from the entire text
    words = word_tokenize(str3)

    # Identify the parts of speech
    tagged = nltk.pos_tag(words)

    

    for i in range(0, len(words)):
        replacements = []

        # Only replace nouns with nouns, vowels with vowels etc.
        for syn in wordnet.synsets(words[i]):

            # Do not attempt to replace proper nouns or determiners
            if tagged[i][1] == 'NNP' or tagged[i][1] == 'DT':
                break

            # The tokenizer returns strings like NNP, VBP etc
            # but the wordnet synonyms has tags like .n.
            # So we extract the first character from NNP ie n
            # then we check if the dictionary word has a .n. or not
            word_type = tagged[i][1][0].lower()
            if syn.name().find("." + word_type + "."):
                # extract the word only
                r = syn.name()[0:syn.name().find(".")]
                replacements.append(r)

        if len(replacements) > 0:
            # Choose a random replacement
            replacement = replacements[randint(0, len(replacements) - 1)]
            output = output + " " + replacement
        else:
            # If no replacement could be found, then just use the
            # original word
            output = output + " " + words[i]
    
    strr = str3
    tn = [int(s) for s in strr.split() if s.isdigit()]
    t[0] = tn[0]
    t[1] = tn[1]
    return strr

  
class Base_Form(object):
    """Base class of all forms"""

    def __init__(self, widget_class, master, action, hidden_input, kw):
        self.action = action

        if hidden_input is None:
            self.hidden_input = dict()
        else:
            if not isinstance(hidden_input, dict):
                raise ValueError("'hidden_input' should be a dict")
                
            self.hidden_input = hidden_input

        kw["class"] = "Form"
        widget_class.__init__(self, master, **kw)
        
class Form_Frame(tk.Frame, Base_Form):
    def __init__(self, master, action=None, hidden_input=None, **kw):
        Base_Form.__init__(self, tk.Frame, master, action, hidden_input, kw)
        
Form = Form_Frame


class MainWindow(tk.Frame):
    counter = 0

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.t = t
        self.k=self.t[1]-self.t[0]
        self.label = tk.Label( self,font=('arial', 15, 'bold'), bd=16,bg="#01b9f5", fg="#012b74", text="Equation Form of The Problem Is:\n"+"? + " +str(self.t[0])+ " = "+ str(self.t[1]),relief=RAISED)
        self.label.pack()
        self.label2 = tk.Label( self ,font=('arial', 25, 'bold'), bd=16,bg="#01b9f5", fg="#012b74", text="Correct Answer is -> "+str(abs(self.k)))
        self.label2.pack()
 

    def answer(self):
        self.k=self.t[1]+self.t[0]
        return str(abs(self.k))
    
    def answer2(self): #correct
        self.k=self.t[0]-self.t[1]
        return str(abs(self.k))
    
    def answer3(self):
        self.k=self.t[1]+self.t[0]+1
        return str(abs(self.k))
    def answer4(self):
        self.k=self.t[0]-self.t[1]+2
        return str(abs(self.k))
    
    
objt = MainWindow(root) 


class Base_SubmitButton(object):
    """Base class of submit buttons"""

    def submit(self ):
        form_widget = self
        
        while True:
            form_widget = form_widget.master
            if form_widget is None:
                raise Exception("No equation found")
            else:
                if form_widget.winfo_class() == "Form":
                    break

        if form_widget.action is None: return
        
        form_action = form_widget.action

        form_data = {}
        form_data.update(form_widget.hidden_input)

        # Applying list for python 2/3 compatibility. dict_values is a view in Python 3.
        list_of_widgets = list(form_widget.children.values())
        form_action(form_data)
       
        nextquestion = nextQuestion()
 
 
 
class Submit_Button(tk.Button, Base_SubmitButton):
    def __init__(self, parent, *args, **kw ):
        kw["command"] = self.submit 
        tk.Button.__init__(self, parent, *args, **kw )
 
   

               
path ='/home/hossam/Documents/MathWordProblem-master/Star.png'
Ans_btn_img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root , bg="#FFFFFF")
panel.pack(side = "bottom", fill = "both", expand = "yes")


##uper part of the page

form = Form(root, action =lambda data:funct(),bg="#FFFFFF") 
form.pack(expand=True, fill="both", ipadx=0, ipady=0)

   
Label(form, font=('arial', 12, 'bold'), text="Question :", bg="#3D4D7F", fg="#FFFFFF", bd=10 , anchor='w').grid(row=0 , column=0, sticky=E, pady=(25,0), padx=(0,15))


#function to show and print questi

question = generateQuestion()
str3 =question 



display = Label(form, font=('arial',15,'bold'), text=str3, bg="#FFFFFF", fg="#000000")
display.grid(row=0,column=1, sticky=E ,  pady=(25,0), padx=(0,100))   


  

def nextQuestion():
    

    str3 = generateQuestion()
    display.config(text=str3)
    
    all_answers = [objt.answer() , objt.answer2() , objt.answer3() , objt.answer4()]
    random.shuffle(all_answers)

 
    Submit_Button(form ,font=('arial',19,'bold'),bg="#b0c4de",bd=10,height=128 ,  width=128 ,  fg="#000000",image = Ans_btn_img,compound="center", text=all_answers[0]).grid(row=26,column=0,sticky =E )#l_up
    Submit_Button(form ,font=('arial',19,'bold'),bg="#b0c4de",bd=10,height=128 ,  width=128, fg="#000000" ,image = Ans_btn_img,compound="center" , text=all_answers[1]).grid(row=27,column=0,sticky =E , pady=(20,0), padx=(50,0))#Left_down
    Submit_Button(form,font=('arial',19,'bold'),bg="#b0c4de",bd=10,height=128 ,  width=128, fg="#000000" ,image = Ans_btn_img,compound="center", text=all_answers[2]).grid(row=27,column=1 ,sticky =W, pady=(25,0) , padx=(100,0))#R_Down
    Submit_Button(form ,font=('arial',19,'bold'),bg="#b0c4de",bd=10,height=128 ,  width=128 , fg="#000000" ,image = Ans_btn_img,compound="center", text=all_answers[3]).grid(row=26,column=1,sticky =W , padx=(100,0))#R_UP


frame = Frame(root)
frame.pack()

def funct():
    root = tk.Tk()
    main = MainWindow(root)
    root.geometry("1100x650")
    root.title("Correct Answer")
    main.pack(side="top", fill="both", expand=True)
    
    
##creat gap
Label(form, font=('arial',12,'bold'),bg="#FFFFFF",bd=8, fg="#99ccff", text=" ").grid(row=24,column=2, sticky=E, pady=(10,0) )


      
all_answers = [objt.answer() , objt.answer2() , objt.answer3() , objt.answer4()] 
random.shuffle(all_answers)

     
Submit_Button(form ,image = Ans_btn_img,compound="center",font=('arial',15,'bold'),bg="#b0c4de", bd=10 ,height=128 ,  width=128 , fg="#000000" , text=all_answers[0]).grid(row=26,column=0,sticky =E ) #Left_up
Submit_Button(form,image = Ans_btn_img,compound="center" ,font=('arial',15,'bold'),bg="#b0c4de",bd=10 , height=128 ,  width=128 , fg="#000000" , text=all_answers[1]).grid(row=27,column=0,sticky =E , pady=(20,0), padx=(50,0))#Left_down
Submit_Button(form,image = Ans_btn_img,compound="center",font=('arial',15,'bold'),bg="#b0c4de",bd=10 ,height=128 ,  width=128 , fg="#000000" , text=all_answers[2]).grid(row=27,column=1 ,sticky =W, pady=(25,0) , padx=(100,0))#R_Down
Submit_Button(form,image = Ans_btn_img,compound="center",font=('arial',15,'bold'),bg="#b0c4de",bd=10 ,height=128 ,  width=128 , fg="#000000" , text=all_answers[3]).grid(row=26,column=1,sticky =W , padx=(100,0))#R_Up



      
root.mainloop()
