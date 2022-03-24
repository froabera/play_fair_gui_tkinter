import os
import datetime
import random
from tkinter import * 
import tkinter.messagebox       
import string 
play_fair = Tk()
play_fair.geometry("950x750+0+0")
play_fair.title("PLAY FAIR IMPLEMENTATION IN PYTHON")
play_fair.configure(background = "green")
# ============== variable declaration=============================
key_text = StringVar()
message_text = StringVar()
ciph_text = StringVar()
key = str(key_text.get())
message = str(message_text.get())
cipher = str(ciph_text.get())
key=key.replace(" ", "")
key=key.upper()  
# ============== create listener for buttons========================================
def qExit():
    qExit = tkinter.messagebox.askyesno("Quit System","do you want to Quit?")
    if qExit > 0:
        play_fair.destroy()
        return
def qClear():
   key_text.set("")
   ciph_text.set("")
   message_text.set("")
   pp.delete("1.0",END)
   pp.insert(END,"")
   cc.delete("1.0",END)
   cc.insert(END,"")
   
def generate_cipher(key):
   ey = ''.join(key.split(' ')) #remove spaces from given key and PF cipher is only for letters. 
   mat=[]
   for c in key.upper():
      if c not in mat:
         mat.append(c)
   alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
   pad = [c for c in alphabet if c not in mat] #List comprehension is more pythonic
   mat = mat + pad
   mat_2D = [mat[i*5:(i+1)*5] for i in range(5)] #condensed into one line
   key_entry00.delete("1.0",END)
   key_entry00.insert(END,mat_2D[0][0])
   key_entry01.delete("1.0",END)
   key_entry01.insert(END,mat_2D[0][1])
   key_entry02.delete("1.0",END)
   key_entry02.insert(END,mat_2D[0][2])
   key_entry03.delete("1.0",END)
   key_entry03.insert(END,mat_2D[0][3])
   key_entry04.delete("1.0",END)
   key_entry04.insert(END,mat_2D[0][4])
   key_entry10.delete("1.0",END)
   key_entry10.insert(END,mat_2D[1][0])
   key_entry11.delete("1.0",END)
   key_entry11.insert(END,mat_2D[1][1])
   key_entry12.delete("1.0",END)
   key_entry12.insert(END,mat_2D[1][2])
   key_entry13.delete("1.0",END)
   key_entry13.insert(END,mat_2D[1][3])
   key_entry14.delete("1.0",END)
   key_entry14.insert(END,mat_2D[1][4])
   key_entry20.delete("1.0",END)
   key_entry20.insert(END,mat_2D[2][0])
   key_entry21.delete("1.0",END)
   key_entry21.insert(END,mat_2D[2][1])
   key_entry22.delete("1.0",END)
   key_entry22.insert(END,mat_2D[2][2])
   key_entry23.delete("1.0",END)
   key_entry23.insert(END,mat_2D[2][3])
   key_entry24.delete("1.0",END)
   key_entry24.insert(END,mat_2D[2][4])
   key_entry30.delete("1.0",END)
   key_entry30.insert(END,mat_2D[3][0])
   key_entry31.delete("1.0",END)
   key_entry31.insert(END,mat_2D[3][1])
   key_entry32.delete("1.0",END)
   key_entry32.insert(END,mat_2D[3][2])
   key_entry33.delete("1.0",END)
   key_entry33.insert(END,mat_2D[3][3])
   key_entry34.delete("1.0",END)
   key_entry34.insert(END,mat_2D[3][4])
   key_entry40.delete("1.0",END)
   key_entry40.insert(END,mat_2D[4][0])
   key_entry41.delete("1.0",END)
   key_entry41.insert(END,mat_2D[4][1])
   key_entry42.delete("1.0",END)
   key_entry42.insert(END,mat_2D[4][2])
   key_entry43.delete("1.0",END)
   key_entry43.insert(END,mat_2D[4][3])
   key_entry44.delete("1.0",END)
   key_entry44.insert(END,mat_2D[4][4])
   return mat_2D
def prettify(table):      #For a more appealing display.
    res1 = '[{}]\n'.format(' '.join(table[0]))
    res2 = ''
    for i in range(1,len(table)-1,1):
        res2 = res2 + '|{}|\n'.format(' '.join(table[i]))
    res3 = '[{}]\n'.format(' '.join(table[len(table)-1]))
    res = res1 + res2 + res3
    
    return res
def find_position(key_matrix,letter):
   x=y=0
   for i in range(5):
      for j in range(5):
         if key_matrix[i][j]==letter:
            x=i
            y=j

   return x,y
################################################################################

def mes2pairs(message):
   key = str(key_text.get())
   message = str(message_text.get())
   if not message.isalpha() or not key.isalpha() or key == " " or message == " ":
          qExit = tkinter.messagebox.askretrycancel("INVALID INPUT","INVALID INPUT")
          if qExit > 0:
            key_text.set("")
            ciph_text.set("")
            message_text.set("")
          
   else:
    
      pp.delete("1.0",END)
      pp.insert(END,message)
      message = ''.join(message.split(' ')).upper()
      if len(message)%2 == 1:
         message = message + 'X'
      pair = [list(message[i:i + 2]) for i in range(0, len(message), 2)]
      pair2 = [[l[0],'X'] if l[0] == l[1] else [l[0],l[1]] for l in pair]
      pairs = [''.join(l) for l in pair2]
      pairs = ' '.join(pairs)
      return pair2
def encrypt():
   key = str(key_text.get())
   message = str(message_text.get())

   message = mes2pairs(message)
   key_matrix = generate_cipher(key)
   cipher=[]
   for e in message:
      p1,q1=find_position(key_matrix,e[0])
      p2,q2=find_position(key_matrix,e[1])
      if p1==p2:
         if q1==4:
            q1=-1
         if q2==4:
            q2=-1
         cipher.append(key_matrix[p1][q1+1])
         cipher.append(key_matrix[p1][q2+1])    
      elif q1==q2:
         if p1==4:
            p1=-1;
         if p2==4:
            p2=-1;
         cipher.append(key_matrix[p1+1][q1])
         cipher.append(key_matrix[p2+1][q2])
      else:
         cipher.append(key_matrix[p1][q2])
         cipher.append(key_matrix[p2][q1])
   cc.delete("1.0",END)
   cc.insert(END,cipher)
   print(cipher)
##########################################################################

def cip2pairs(cipher):
   key = str(key_text.get())
   cipher = str(ciph_text.get())
   if not cipher.isalpha() or not key.isalpha() or key == " " or cipher == " ":
      qExit = tkinter.messagebox.askretrycancel("INVALID INPUT","INVALID INPUT")
      if qExit > 0:
         key_text.set("")
         ciph_text.set("")
         message_text.set("")
   else:
      cc.delete("1.0",END)
      cc.insert(END,cipher)
      cipher = ''.join(cipher.split(' ')).upper()
      pair = [list(cipher[i:i + 2]) for i in range(0, len(cipher), 2)]
      pairs = [cipher[i:i + 2] for i in range(0, len(cipher), 2)]
      pairs = ' '.join(pairs)
      return pair   
   
def decrypt(): 
   key = str(key_text.get())
   cipher = str(ciph_text.get())
   cipher = cip2pairs(cipher)
   key_matrix = generate_cipher(key)
   plaintext=[]
   for e in cipher:
      p1,q1=find_position(key_matrix,e[0])
      p2,q2=find_position(key_matrix,e[1])
      if p1==p2:
         if q1==4:
            q1=-1
         if q2==4:
            q2=-1
         plaintext.append(key_matrix[p1][q1-1])
         plaintext.append(key_matrix[p1][q2-1])    
      elif q1==q2:
         if p1==4:
            p1=-1;
         if p2==4:
            p2=-1;
         plaintext.append(key_matrix[p1-1][q1])
         plaintext.append(key_matrix[p2-1][q2])
      else:
         plaintext.append(key_matrix[p1][q2])
         plaintext.append(key_matrix[p2][q1])

   count = 0
   pt = []
   for c in plaintext:
      if c == 'X':
         count = count + 1
   if count<2 and count>0:          
      plaintext.remove('X')
   elif count == 0:
      pass
   else:                    #In case there were repeated characters
      for i in range(len(plaintext)):
          if plaintext[i]=='X':
              pt.append(plaintext[i-1])
          else:
              pt.append(plaintext[i])
   output = ''
   if len(pt)!=0:
      output=''.join(pt)
   else:
      output=''.join(plaintext)
   pp.delete("1.0",END)
   pp.insert(END,output)
 
          

# ================== frame creation============================

Tops = Frame(play_fair, width=1200, height=100, bd=14, relief="raise")
Tops.pack()
left_frame = Frame(play_fair, width=400, height=600, bd=8, relief="raise")
left_frame.pack(side=LEFT)
right_frame = Frame(play_fair, width=400, height=600, bd=8, relief="raise")
right_frame.pack(side=RIGHT)
top_frame = Frame(left_frame, width=400, height=320, bd=8, relief="raise")
top_frame.pack(side=TOP)
bottom_frame = Frame(left_frame, width=400, height=330, bd=8, relief="raise")
bottom_frame.pack(side=BOTTOM)
right_top_frame = Frame(right_frame, width=400, height=300, bd=8, relief="raise")
right_top_frame.pack(side=TOP)
right_bottom_frame = Frame(right_frame, width=400, height=600, bd=8, relief="raise")
right_bottom_frame.pack(side=BOTTOM)
Tops.configure(background="green")
#============== Label creation=================================
LabelInfo = Label(right_top_frame, font={'arial',100,'bold'},text="====RESULT====",bd=10)
LabelInfo.grid(row=0,column=1)
LabelInfo = Label(right_top_frame, font={'arial',100,'bold'},text="PLAIN TEXT",bd=10)
LabelInfo.grid(row=1,column=0)
LabelInfo = Label(right_top_frame, font={'arial',100,'bold'},text="CIPHER TEXT",bd=10)
LabelInfo.grid(row=2,column=0)
LabelInfo = Label(Tops, font={'arial',100,'bold'},text="PLAY FAIR IMPLEMENTATION IN PYTHON",bd=10)
LabelInfo.grid(row=0,column=0)
clarity_label = Label(top_frame, font={'arial',100,'bold'},text="please enter key & message",bd=10)
clarity_label.grid(row=0,column=1)
key_label = Label(top_frame, font={'arial',100,'bold'},text="key",bd=10)
key_label.grid(row=1,column=0)
key_entry = Entry(top_frame, font={'arial',100,'bold'},bd=10,textvariable=key_text)
key_entry.grid(row=1,column=1)
key_label = Label(top_frame, font={'arial',100,'bold'},text="Encrypt",bd=10)
key_label.grid(row=2,column=1)
message_label = Label(top_frame, font={'arial',100,'bold'},text="plain text",bd=10)
message_label.grid(row=3,column=0)
message_entry = Entry(top_frame, font={'arial',100,'bold'},bd=10,textvariable=message_text)
message_entry.grid(row=3,column=1)
dec_label = Label(top_frame, font={'arial',100,'bold'},text="Decrypt",bd=10)
dec_label.grid(row=5,column=1)
plain_label = Label(top_frame, font={'arial',100,'bold'},text="cipher text",bd=10)
plain_label.grid(row=6,column=0)
plain_entry = Entry(top_frame, font={'arial',100,'bold'},bd=10,textvariable=ciph_text)
plain_entry.grid(row=6,column=1)
# ==============create button===============
enc_btn = Button(top_frame,pady=1,bd=4,fg="black",font={'arial',100,'bold'},text="Encrypt",
                 width=5,command=encrypt).grid(row=4,column=1)
ex_btn = Button(top_frame,pady=1,bd=4,fg="black",font={'arial',100,'bold'},text="Exit",
                 width=5,command=qExit).grid(row=7,column=3)
dec_btn = Button(top_frame,pady=1,bd=4,fg="black",font={'arial',100,'bold'},text="Decrypt",
                 width=5,command=decrypt).grid(row=7,column=1)
dec_clr = Button(top_frame,pady=1,bd=4,fg="black",font={'arial',100,'bold'},text="clear",
                 width=5,command=qClear).grid(row=7,column=2)
#==============create 5x5 matrix==========
key_entry00 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry00.grid(row=0,column=0)
key_entry01 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry01.grid(row=0,column=1)
key_entry02 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry02.grid(row=0,column=2)
key_entry03 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry03.grid(row=0,column=3)
key_entry04 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry04.grid(row=0,column=4)
key_entry10 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry10.grid(row=1,column=0)
key_entry11 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry11.grid(row=1,column=1)
key_entry12 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry12.grid(row=1,column=2)
key_entry13 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry13.grid(row=1,column=3)
key_entry14 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry14.grid(row=1,column=4)
key_entry20 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry20.grid(row=2,column=0)
key_entry21 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry21.grid(row=2,column=1)
key_entry22 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry22.grid(row=2,column=2)
key_entry23 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry23.grid(row=2,column=3)
key_entry24 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry24.grid(row=2,column=4)
key_entry30 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry30.grid(row=3,column=0)
key_entry31 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry31.grid(row=3,column=1)
key_entry32 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry32.grid(row=3,column=2)
key_entry33 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry33.grid(row=3,column=3)
key_entry34 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry34.grid(row=3,column=4)
key_entry40 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry40.grid(row=4,column=0)
key_entry41 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry41.grid(row=4,column=1)
key_entry42 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry42.grid(row=4,column=2)
key_entry43 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry43.grid(row=4,column=3)
key_entry44 = Text(bottom_frame, font={'arial',100,'bold'},height=2,width=3,bd = 8)
key_entry44.grid(row=4,column=4)
pp = Text(right_top_frame, font={'arial',100,'bold'},height=1,width=25,bd = 8)
pp.grid(row=1,column=1)
cc = Text(right_top_frame, font={'arial',100,'bold'},height=1,width=25,bd = 8)
cc.grid(row=2,column=1)
play_fair.mainloop()