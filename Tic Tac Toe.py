from tkinter import *

root=Tk()
c="white"
c1="black"
root.config(bg=c)
root.resizable(0,0)
root.title("TIC TAC TOE")

count=0
move=0
mode=0
xcount=0
ocount=0

def colour(c1,c,text):
	cm.config(text=text,fg=c1,bg=c)
	b1.config(bg=c)
	b2.config(bg=c)
	b3.config(bg=c)
	b4.config(bg=c)
	b5.config(bg=c)
	b6.config(bg=c)
	b7.config(bg=c)
	b8.config(bg=c)
	b9.config(bg=c)
	label.config(fg=c1,bg=c)
	xc.config(fg=c1,bg=c)
	oc.config(fg=c1,bg=c)
	refreshb.config(fg=c1,bg=c)
	resetb.config(fg=c1,bg=c)
	root.config(bg=c)

def cmode():
	global c,c1,mode
	temp=c
	c=c1
	c1=temp
	if mode==0:
		colour(c1,c,"Light")
		mode=1
	else:
		colour(c1,c,"Dark")
		mode=0

def stop():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)

def refresh():
	global b1,b2,b3,b4,b5,b6,b7,b8,b9,move,count
	label.config(text="")
	b1=Button(root,text=" ",bg=c,height=1,width=3,padx=12,command=lambda: buttonpress(b1))
	b1.grid(row=1,column=0)
	b1.config(font=("Times New Roman",50))
	b2=Button(root,text=" ",bg=c,height=1,width=3,padx=12,command=lambda: buttonpress(b2))
	b2.grid(row=1,column=1)
	b2.config(font=("Times New Roman",50))
	b3=Button(root,text=" ",bg=c,height=1,width=3,padx=12,command=lambda: buttonpress(b3))
	b3.grid(row=1,column=2)
	b3.config(font=("Times New Roman",50))
	b4=Button(root,text=" ",bg=c,height=1,width=3,padx=12,command=lambda: buttonpress(b4))
	b4.grid(row=2,column=0)
	b4.config(font=("Times New Roman",50))
	b5=Button(root,text=" ",bg=c,height=1,width=3,padx=12,command=lambda: buttonpress(b5))
	b5.grid(row=2,column=1)
	b5.config(font=("Times New Roman",50))
	b6=Button(root,text=" ",bg=c,height=1,width=3,padx=12,command=lambda: buttonpress(b6))
	b6.grid(row=2,column=2)
	b6.config(font=("Times New Roman",50))
	b7=Button(root,text=" ",bg=c,height=1,width=3,padx=12,command=lambda: buttonpress(b7))
	b7.grid(row=3,column=0)
	b7.config(font=("Times New Roman",50))
	b8=Button(root,text=" ",bg=c,height=1,width=3,padx=12,command=lambda: buttonpress(b8))
	b8.grid(row=3,column=1)
	b8.config(font=("Times New Roman",50))
	b9=Button(root,text=" ",bg=c,height=1,width=3,padx=12,command=lambda: buttonpress(b9))
	b9.grid(row=3,column=2)
	b9.config(font=("Times New Roman",50))
	count=0
	move=0

def checkxo(n1,n2,n3):
	global xcount,ocount
	bu=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
	x=bu[n1]
	y=bu[n2]
	z=bu[n3]

	if x["text"]=="x" and y["text"]=="x" and z["text"]=="x":
		x.config(bg="green")
		y.config(bg="green")
		z.config(bg="green")
		label.config(text="X WINS",fg=c1)
		xcount+=1
		xc.config(text="X : "+str(xcount))
		oc.config(text="O : "+str(ocount))
		stop()
	elif x["text"]=="o" and y["text"]=="o" and z["text"]=="o":
		x.config(bg="green")
		y.config(bg="green")
		z.config(bg="green")
		label.config(text="O WINS",fg=c1)
		ocount+=1
		oc.config(text="O : "+str(ocount))
		xc.config(text="X : "+str(xcount))
		stop()
	else:
		if label["text"]!="X WINS" and count>=9:
			label.config(text="TIE",fg=c1)
			oc.config(text="O WINS : "+str(ocount))
			xc.config(text="X WINS : "+str(xcount))
			stop()
		else:
			pass

	if xcount>ocount:
		xc.config(fg="green")
		oc.config(fg="red")
	elif xcount<ocount:
		xc.config(fg="red")
		oc.config(fg="green")
	else:
		xc.config(fg=c1)
		oc.config(fg=c1)

def check():
	n1=0
	n2=1
	n3=2
	for l1 in range(1,9):
		if l1<4:
			checkxo(n1,n2,n3)
			n1+=3
			n2+=3
			n3+=3
		elif l1<7:
			if n1==n2-1==n3-2:
				n1=0
				n2=3
				n3=6
				checkxo(n1,n2,n3)
			else:
				n1+=1
				n2+=1
				n3+=1
				checkxo(n1,n2,n3)
		else:
			if n1==n2-3==n3-6:
				n1=0
				n2=4
				n3=8
				checkxo(n1,n2,n3)
			else:
				n1+=2
				n3-=2
				checkxo(n1,n2,n3)

def buttonpress(b):
	global move,count
	if move==0 and b["text"]==" ":
		b.config(text="x",fg="blue")
		label.config(text="")
		count+=1
		move=1
		check()
	elif move==1 and b["text"]==" ":
		b.config(text="o",fg="red")
		label.config(text="")
		count+=1
		move=0
		check()
	else:
		label.config(text='"Select an empty box"',fg="red")

label=Label(root,text="",font=("Times New Roman",10),bg=c,fg=c1)
label.grid(row=0,column=1)

resetb=Button(root,text="RESET",bg=c,fg=c1,command=lambda: reset())
resetb.grid(row=0,column=2)

xc=Label(root,text="",bg=c,fg=c1)
xc.grid(row=4,column=0)

oc=Label(root,text="",bg=c,fg=c1)
oc.grid(row=4,column=2)

cm=Button(root,text="Dark",command=lambda: cmode())
cm.grid(row=4,column=1)

refreshb=Button(root,text="REFRESH",bg=c,fg=c1,command=lambda: refresh())
refreshb.grid(row=0,column=0)

def reset():
	global xcount,ocount
	xc.config(text="")
	oc.config(text="")
	refresh()
	xcount=0
	ocount=0

refresh()

root.mainloop()
