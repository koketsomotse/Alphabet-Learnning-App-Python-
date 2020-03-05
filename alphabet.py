#alphabet app in Python

from tkinter import *
import pygame
import os


pygame.init()
root=Tk()
root.title("Alphabet Application")
root.geometry('1352x653+0+0')
root.configure(background='white')

str1=StringVar()
str1.set("Welcome to the Alphabet Application")
ABC = Frame(root,bg="white")
ABC.grid()


cont = Canvas(ABC,width=160,height=120, bg="white")
cont.grid(row=3,column=3)
image1= PhotoImage(file="image.PNG")

#===========================================Functions============================================#
imgClear=PhotoImage(file="image.PNG")
def Clear():
    str1.set("Welcome to the Alphabet Application")
    image=cont.create_image(80,70,image=imgClear)
    

imageA=PhotoImage(file="Apple-PNG-Image2.png")
def Alphabet_A():
    str1.set("A is for Apple")
    image=cont.create_image(80,70,image=imageA)

imageB=PhotoImage(file="banana.png")
def Alphabet_B():
    str1.set("B is for Banana")
    image=cont.create_image(80,70,image=imageB)

imageC=PhotoImage(file="cat.png")
def Alphabet_C():
    str1.set("C is for Cat")
    image=cont.create_image(80,70,image=imageC)

imageD=PhotoImage(file="dog.png")
def Alphabet_D():
    str1.set("D is for Dog")
    image=cont.create_image(80,70,image=imageD)

imageE=PhotoImage(file="egg.png")
def Alphabet_E():
    str1.set("E is for Egg")
    image=cont.create_image(80,70,image=imageE)

imageF=PhotoImage(file="fish.png")
def Alphabet_F():
    str1.set("F for Fish")
    image=cont.create_image(80,70,image=imageF)

imageG=PhotoImage(file="gate.png")
def Alphabet_G():
    str1.set("G for Gate")
    image=cont.create_image(80,70,image=imageG)


imageH=PhotoImage(file="horse.PNG")
def Alphabet_H():
    str1.set("H for Horse")
    image=cont.create_image(80,70,image=imageH)


imageI=PhotoImage(file="ice.PNG")
def Alphabet_I():
    str1.set("I for Ice")
    image=cont.create_image(80,70,image=imageI)

imageJ=PhotoImage(file="jam.PNG")
def Alphabet_J():
    str1.set("J for Jam")
    image=cont.create_image(80,70,image=imageJ)


imageY=PhotoImage(file="yoyo.PNG")
def Alphabet_Y():
    str1.set("Y for Yo-Yo")
    image=cont.create_image(80,70,image=imageY)

imageZ=PhotoImage(file="zebra.PNG")
def Alphabet_Z():
    str1.set("Z for Zebra")
    image=cont.create_image(80,70,image=imageZ)    

txtDisplay=Entry(ABC,textvariable=str1,font=('arial',44,'bold'),bg="powder blue",bd=34,width=39,justify=CENTER)
txtDisplay.grid(row=0,column=0,columnspan=7,pady=1)



#===========================================Row 1============================================#
btnA=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="A",bg="CornSilk",command=Alphabet_A).grid(row=1,column=0)
btnB=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="B",bg="powder blue",command=Alphabet_B).grid(row=1,column=1)
btnC=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="C",command=Alphabet_C).grid(row=1,column=2)
btnD=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="D",bg="CornSilk",command=Alphabet_D).grid(row=1,column=3)
btnE=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="E",bg="powder blue",command=Alphabet_E).grid(row=1,column=4)
btnF=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="F",command=Alphabet_F).grid(row=1,column=5)
btnG=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="G",bg="CornSilk",command=Alphabet_G).grid(row=1,column=6)

#===========================================Row 2============================================#
btnH=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="H",bg="powder blue",command=Alphabet_H).grid(row=2,column=0)
btnI=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="I",command=Alphabet_I).grid(row=2,column=1)
btnJ=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="J",bg="CornSilk",command=Alphabet_J).grid(row=2,column=2)
btnK=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="K",bg="powder blue").grid(row=2,column=3)
btnL=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="L").grid(row=2,column=4)
btnM=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="M",bg="CornSilk").grid(row=2,column=5)
btnN=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="N",bg="powder blue").grid(row=2,column=6)
#===========================================Row 3============================================#

btnO=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="O").grid(row=3,column=0)
btnP=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="P",bg="CornSilk").grid(row=3,column=1)
btnQ=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="Q",bg="powder blue").grid(row=3,column=2)
btnR=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="R",bg="CornSilk").grid(row=3,column=4)
btnS=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="S",bg="powder blue").grid(row=3,column=5)
btnT=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="T").grid(row=3,column=6)

#===========================================Row 4============================================#

btnU=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="U",bg="CornSilk").grid(row=4,column=0)
btnV=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="V",bg="powder blue").grid(row=4,column=1)
btnW=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="W").grid(row=4,column=2)
btnX=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="X",bg="CornSilk").grid(row=4,column=3)
btnY=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="Y",bg="powder blue",command=Alphabet_Y).grid(row=4,column=4)
btnZ=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="Z",command=Alphabet_Z).grid(row=4,column=5)
btnClear=Button(ABC,pady=1,bd=4,font=('arial',21,'bold'),width=10,height=3,text="Clear",bg="CornSilk",command=Clear).grid(row=4,column=6)

root.mainloop()
