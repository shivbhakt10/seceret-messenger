import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> dictionary <<<<<<<<<<<<<<<<<<<<<<<<<#
d={'A': 'y', 'Y':'a', 'B': 'w', 'W': 'b', 'C': 't', 'T': 'c', 'D': 'u', 'U': 'd', 'E': 'r', 'R': 'e', 'P': 's', 'S': 'p', 'H': 'n',
 'N': 'h', 'K': 'q', 'Q': 'k', 'O': 'f', 'F': 'o', 'J': 'm', 'M': 'j', 'G': 'x', 'X': 'g', 'I': 'z', 'Z': 'i', 'V': 'l', 'L': 'v','y': 'A', 'a': 'Y', 'w': 'B',
  'b': 'W', 't': 'C', 'c': 'T', 'u': 'D', 'd': 'U', 'r': 'E', 'e': 'R', 's': 'P', 'p': 'S', 'n': 'H',
  'h': 'N', 'q': 'K', 'k': 'Q', 'f': 'O', 'o': 'F', 'm': 'J', 'j': 'M', 'x': 'G', 'g': 'X', 'z': 'I', 'i': 'Z', 'l': 'V', 'v': 'L',' ':'%',
 '%':' ',".":"'","'":'.','$': '!', '*': '@', '{': '&', '}': '^', '_': '(', '-': ')', '`': '#', '+': '~', '\\': '=','=':'\\', '>': '[', '<': ']', '?': ';', '/': ':', ',': '|',
 '!': '$', '@': '*', '&': '{', '^': '}', '(': '_', ')': '-', '#': '`', '~': '+', '[': '>', ']': '<', ';': '?', ':': '/', '|': ',','\n':'\t','\t':'\n',
 '0':'7','7':'0','1':'6','6':'1','2':'9','9':'2','3':'5','5':'3','4':'8','8':'4','"':'"'}

#####################################################################################################################################################################################


################  functions  ###################

def openfile():
    file = filedialog.askopenfile()
    if file:
          filepath = os.path.abspath(file.name)
    filepath=filepath.replace('\\','/')
    #filepath="'"+filepath+"'"
    f1=open(filepath)
    message=f1.read()
    converting(message)
    wantsavefile()

def converting(messagee):
    #l=list(messagee)
    messagellist=[]
    counting1=messagee.count("'")
    counting2=messagee.count('"')
    if counting1 % 2 !=0:
        filee='"'+messagee+'"'
    elif counting2 % 2 !=0:
        filee="'"+messagee+"'"
    else:
        filee=messagee
    for i in filee:
        output=d[i]
        messagellist.append(output)
    global messageoutput
    messageoutput=''.join(messagellist)
    
    text_box2.insert('end',messageoutput)

def savesfile():
    filename = filedialog.asksaveasfilename(initialdir='/', title='Save File', filetypes=(('Text Files', 'txt.*'), ('All Files', '*.*')))
    myfile = open(filename, "w+")
    print(messageoutput)
    myfile.write(messageoutput)
def wantsavefile():
    value=messagebox.askquestion("save file", "Do you want to save file")
    if value == 'yes':
        savesfile()
        
def convertviatext():
    message1=text_box.get("1.0","end")
    converting(message1)
    try:
        wantsavefile()
    except:
        pass

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#--------------------head of tkinter-----------------#
root=tkinter.Tk()
root.title('Secret Messenge')
root.minsize(800,450)
root.maxsize(800,455)
root.config(bg='dimgrey')

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#====================heading=========================#
Label(text='Secret Messenger',bg='black',fg='orange',font='comicsansms 20 bold',borderwidth=5,relief=SUNKEN).place(x=280,y=0)#grid(row=0,column=0,pady=10,sticky=E)

#########################################################################################################
#inputbox

Label(root,text='Enter your message here ▼▼▼',font='comicsansms 12 bold').place(x=40,y=45)#grid(row=1,column=0)
text_box = Text(
    root,
    height=9,
    width=35,
    font= ('Arial', 12, 'bold')
)
text_box.place(x=20,y=80)#grid(row=2,column=0,padx=10)

######################################################################################################
#outputbox

Label(root,text='output==>',font='comicsansms 12 bold').place(x=335,y=270)#grid(row=1,column=1)
text_box2 = Text(
    root,
    height=9,
    width=35,
    font= ('Arial', 12, 'bold')
)
text_box2.place(x=420,y=250)#grid(column=1,row=2, sticky=S, padx=10)
########################################################################################################
Label(text='OR',bg='blue',fg='yellow',font='comicsansms 11 bold').place(x=400,y=145)#.grid(row=3,column=0,pady=5)

b1=Button(root,text='choose file',font='comicsansms 14 bold',command=openfile).place(x=510,y=140)#grid(row=4,column=0)

b2=Button(root,text='CONVERT',font='comicsansms 16 bold',command=convertviatext).place(x=110,y=350)#.grid(row=3,column=1,ipadx=12,ipady=7,pady=2,padx=7)
###################################################################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~mainlooping tkinter~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
root.mainloop()
