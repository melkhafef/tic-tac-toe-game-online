# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:43:41 2019

@author: CSE
"""
import tkinter
from socket import *
import _thread
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host="127.0.0.1"
port=9000
s.bind((host,port))
s.listen(5)
root = tkinter.Tk()
root.title("server")
whoPlay=tkinter.StringVar()
labelWho = tkinter.Label( root, textvariable=whoPlay)
whoPlay.set("start play")
labelWho.grid(row=5,column=1)
X=True
def tictactoe(button,numBtn) :
    global X,buttons,label
    global c
    x=str(numBtn)
    if(X==True):
        c.send(x.encode('utf-8'))
        button["text"]="X"
        button["command"]=""
        X=False
        whoPlay.set("Wait for other player .....")
        if (buttons[0]["text"]=="X" and buttons[1]["text"]=="X" and buttons[2]["text"]=="X"):
                    buttons[0].config(fg="red", bg="blue")
                    buttons[1].config(fg="red", bg="blue")
                    buttons[2].config(fg="red", bg="blue")
                    label["text"]="X Win"
                    for b in range(0,9):
                        buttons[b]["command"]=""
        elif (buttons[3]["text"]=="X" and buttons[4]["text"]=="X" and buttons[5]["text"]=="X"):
            buttons[3].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[6]["text"]=="X" and buttons[7]["text"]=="X" and buttons[8]["text"]=="X"):
            buttons[6].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="X" and buttons[3]["text"]=="X" and buttons[6]["text"]=="X"):
            buttons[0].config(fg="red", bg="blue")
            buttons[3].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[1]["text"]=="X" and buttons[4]["text"]=="X" and buttons[7]["text"]=="X"):
            buttons[1].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="X" and buttons[5]["text"]=="X" and buttons[8]["text"]=="X"):
            buttons[2].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="X" and buttons[4]["text"]=="X" and buttons[8]["text"]=="X"):
            buttons[0].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="X" and buttons[4]["text"]=="X" and buttons[6]["text"]=="X"):
            buttons[2].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="O" and buttons[1]["text"]=="O" and buttons[2]["text"]=="O"):
            buttons[0].config(fg="red", bg="blue")
            buttons[1].config(fg="red", bg="blue")
            buttons[2].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[3]["text"]=="O" and buttons[4]["text"]=="O" and buttons[5]["text"]=="O"):
            buttons[3].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[6]["text"]=="O" and buttons[7]["text"]=="O" and buttons[8]["text"]=="O"):
            buttons[6].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="O" and buttons[3]["text"]=="O" and buttons[6]["text"]=="O"):
            buttons[0].config(fg="red", bg="blue")
            buttons[3].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[1]["text"]=="O" and buttons[4]["text"]=="O" and buttons[7]["text"]=="O"):
            buttons[1].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="O" and buttons[5]["text"]=="O" and buttons[8]["text"]=="O"):
            buttons[2].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label = tkinter.Label( root, text="O Win")
            label.grid(row=4,column=1)
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="O" and buttons[4]["text"]=="O" and buttons[8]["text"]=="O"):
            buttons[0].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="O" and buttons[4]["text"]=="O" and buttons[6]["text"]=="O"):
            buttons[2].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
def replay():
     global X,buttons,label
     whoPlay.set("start play")
     X=True
     label.destroy()
     for i in range(0,10):
       buttons[i].destroy()
     buttons=[]
     b=0
     for i in range(0,10):
       buttons.append(tkinter.Button(root,width=20))
     for r in range(3):
             for c in range(3):
               buttons[b]["command"]=lambda button=buttons[b],numBtn=b: tictactoe(button,numBtn)
               buttons[b].grid(row=r,column=c)
               b+=1
     label = tkinter.Label( root, text="                   ")
     label.grid(row=4,column=1)
     buttons[9]["command"]=replay
     buttons[9]["text"]="replay"
     buttons[9].grid(row=6,column=1)
  
buttons=[]
b=0
for i in range(0,10):
    buttons.append(tkinter.Button(root,width=20))
for r in range(3):
   for c in range(3):
       buttons[b]["command"]=lambda button=buttons[b],numBtn=b: tictactoe(button,numBtn)
       buttons[b].grid(row=r,column=c)
       b+=1
label = tkinter.Label( root, text="")
label.grid(row=4,column=1)
buttons[9]["command"]=replay
buttons[9]["text"]="replay"
buttons[9].grid(row=6,column=1)
c,a=s.accept()
def rec():
    global s,X,buttons,label
    while True:
        w=c.recv(2048)
        btnNum=int(w.decode("utf-8"))
        buttons[btnNum]["text"]="O"
        buttons[btnNum]["command"]=""
        if (buttons[0]["text"]=="X" and buttons[1]["text"]=="X" and buttons[2]["text"]=="X"):
                    buttons[0].config(fg="red", bg="blue")
                    buttons[1].config(fg="red", bg="blue")
                    buttons[2].config(fg="red", bg="blue")
                    label["text"]="X Win"
                    for b in range(0,9):
                        buttons[b]["command"]=""
        elif (buttons[3]["text"]=="X" and buttons[4]["text"]=="X" and buttons[5]["text"]=="X"):
            buttons[3].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[6]["text"]=="X" and buttons[7]["text"]=="X" and buttons[8]["text"]=="X"):
            buttons[6].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="X" and buttons[3]["text"]=="X" and buttons[6]["text"]=="X"):
            buttons[0].config(fg="red", bg="blue")
            buttons[3].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[1]["text"]=="X" and buttons[4]["text"]=="X" and buttons[7]["text"]=="X"):
            buttons[1].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="X" and buttons[5]["text"]=="X" and buttons[8]["text"]=="X"):
            buttons[2].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="X" and buttons[4]["text"]=="X" and buttons[8]["text"]=="X"):
            buttons[0].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="X" and buttons[4]["text"]=="X" and buttons[6]["text"]=="X"):
            buttons[2].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="O" and buttons[1]["text"]=="O" and buttons[2]["text"]=="O"):
            buttons[0].config(fg="red", bg="blue")
            buttons[1].config(fg="red", bg="blue")
            buttons[2].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[3]["text"]=="O" and buttons[4]["text"]=="O" and buttons[5]["text"]=="O"):
            buttons[3].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[6]["text"]=="O" and buttons[7]["text"]=="O" and buttons[8]["text"]=="O"):
            buttons[6].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="O" and buttons[3]["text"]=="O" and buttons[6]["text"]=="O"):
            buttons[0].config(fg="red", bg="blue")
            buttons[3].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[1]["text"]=="O" and buttons[4]["text"]=="O" and buttons[7]["text"]=="O"):
            buttons[1].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="O" and buttons[5]["text"]=="O" and buttons[8]["text"]=="O"):
            buttons[2].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label = tkinter.Label( root, text="O Win")
            label.grid(row=4,column=1)
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="O" and buttons[4]["text"]=="O" and buttons[8]["text"]=="O"):
            buttons[0].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="O" and buttons[4]["text"]=="O" and buttons[6]["text"]=="O"):
            buttons[2].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        X=True
        whoPlay.set("start play")
_thread.start_new_thread(rec,())
root.mainloop()

   
    
    
