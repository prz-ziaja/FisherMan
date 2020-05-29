import tkinter as tk, os
from random import randint
questionstxt=[]
answerstxt=[]
with open('update','r') as f:
    a=f.readlines()
    for comm in a[:-1]:
        os.system(comm)

with open('questions','r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        elif line[0]=='?':
            questionstxt.append(line[1:])
        elif line[0]=='!':
            answerstxt.append(line[1:])
if len(questionstxt)!=len(answerstxt):
    print("Set of questions and set of answers are different sizes")
    print("Try to update using git")
    exit(1)
rand=randint(0,len(questionstxt)-1)
def question():
    global rand
    rand=randint(0,len(questionstxt)-1)
    text='Pytanie:\n'+questionstxt[rand]
    questLab.configure(text=text)
    ansLab.configure(text='')
def answer():
    global rand
    text='Pytanie:\n'+questionstxt[rand]
    questLab.configure(text=text)
    text='Odpowiedź:\n'+answerstxt[rand]
    ansLab.configure(text=text)
def on_closing():
    print('hehe')
    root.destroy()
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
canvas=tk.Canvas(root, height=700, width=700, bg='#263E42')
canvas.pack()
frame1=tk.Frame(root,bg='white')
frame1.place(relwidth=0.8,relheight=0.3,relx=0.1,rely=0.1)
frame2=tk.Frame(root,bg='white')
frame2.place(relwidth=0.8,relheight=0.3,relx=0.1,rely=0.5)
ans = tk.Button(root,text='answer', padx=110, pady=5, fg='orange',bg='#000000',command=answer)
ans.pack()
next = tk.Button(root,text='next', padx=110, pady=5, fg='orange',bg='#000000',command=question)
next.pack()
questLab=tk.Label(frame1, font="Helvetica 16 bold",wraplength=500)
questLab.pack()
ansLab=tk.Label(frame2, font="Helvetica 16 bold",wraplength=500)
ansLab.pack()
root.mainloop()
