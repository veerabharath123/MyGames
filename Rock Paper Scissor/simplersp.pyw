from tkinter import *
from random import randint
from PIL import Image,ImageTk
import os

root=Tk()
root.geometry('650x550+100+100')
root.title('ROCK PAPER SCISSOR')
#root.overrideredirect(1)
root.resizable(0,0)
bc="white"
bc1="#399bbe"
root.config(bg=bc1)

exit=Button(root,text="X",fg=bc,bg=bc1,bd=0,activebackground='red',command=lambda: exit())
exit.place(relx=0.5,rely=0.0,x=300)
exit.config(font=("Gill Sans Ultra Bold", 10))

gname=Label(root,text="ROCK, PAPER, SCISSOR",fg=bc,bg=bc1)
gname.grid(row=0, column=0,columnspan=3,padx=38,pady=20)
gname.config(font=("Gill Sans Ultra Bold", 30))

info=Label(root,text="HELLO PLAYER",fg=bc,bg="#2b748e")
info.grid(row=1,column=0,columnspan=3,padx=0,pady=10)
info.config(font=("Gill Sans Ultra Bold", 15))

def exit():
	root.destroy()

def stop():
	r_b.config(state=DISABLED)
	p_b.config(state=DISABLED)
	s_b.config(state=DISABLED)
	resetb.config(state=DISABLED)

def reset():
	call_image(4,4)

	info.config(text="HELLO PLAYER")
	c_name.config(text="COMPUTER")

	u_name.config(text="YOU")
	c_name.config(fg=bc)
	u_name.config(fg=bc)

	global c_count,u_count
	c_count=0
	u_count=0

def animate(m):
	global i,count
	itext=["ROCK","PAPER","SCISSOR"]
	stop()
	if count<=6 and (count%2)==0 and count!=0:
		o=int(count/2-1)
		info.config(text=itext[o])
	else:
		pass

	if count<=6 and i==0:
		count+=1
		call_image(1,1)
		i=1
		info.after(200,lambda: animate(m))

	elif count<=7 and i==1:
		count+=1
		call_image(5,5)
		i=0
		info.after(200,lambda: animate(m))

	elif count==8:
		h_values()
		count+=1
		if m==1:
			call_image(rnum,hrock)
			check(rnum,hrock)
			info.after(500,lambda: animate(0))

		elif m==2:
			call_image(rnum,hpaper)
			check(rnum,hpaper)
			info.after(500,lambda: animate(0))

		elif m==3:
			call_image(rnum,hscissor)
			check(rnum,hscissor)
			info.after(500,lambda: animate(0))
		else:
			pass
	else:	
		count=0
		refresh()

def call_image(x,y):
	global l_image,r_image
	
	l_image = ImageTk.PhotoImage(images[x][0])
	ll_image.configure(image =  l_image)

	r_image = ImageTk.PhotoImage(images[y][1])
	rr_image.configure(image =  r_image)

def h_values():
	global rnum,hrock,hpaper,hscissor
	rnum=randint(1,3)
	hrock=1
	hpaper=2
	hscissor=3

def check(lhand,rhand):
	global c_count,u_count

	if lhand==rhand:
		info.config(text="DRAW")
		info.config(font=("Gill Sans Ultra Bold", 15))

	elif lhand==hrock and rhand==hscissor:
		info.config(text="YOU LOST")
		info.config(font=("Gill Sans Ultra Bold", 15))
		c_count+=1

	elif lhand==hpaper and rhand==hrock:
		info.config(text="YOU LOST")
		info.config(font=("Gill Sans Ultra Bold", 15))
		c_count+=1

	elif lhand==hscissor and rhand==hpaper:
		info.config(text="YOU LOST")
		info.config(font=("Gill Sans Ultra Bold", 15))
		c_count+=1

	else:
		info.config(text="YOU WON")
		info.config(font=("Gill Sans Ultra Bold", 15))
		u_count+=1

	c_text="COMPUTER : "+str(c_count)
	c_name.config(text=c_text)
	u_text="YOU : "+str(u_count)
	u_name.config(text=u_text)

	if c_count>u_count:
		c_name.config(fg="green")
		u_name.config(fg="red")
	elif c_count<u_count:
		c_name.config(fg="red")
		u_name.config(fg="green")
	else:
		c_name.config(fg=bc)
		u_name.config(fg=bc)

cwd=os.getcwd()

lr=cwd+"\\images\\lr.png"
lp=cwd+"\\images\\lp.png"
ls=cwd+"\\images\\ls.png"
ld=cwd+"\\images\\computer.png"
lu=cwd+"\\images\\lu.png"

rr=cwd+"\\images\\rr.png"
rp=cwd+"\\images\\rp.png"
rs=cwd+"\\images\\rs.png"
rd=cwd+"\\images\\user.png"
ru=cwd+"\\images\\ru.png"

l_rock = Image.open(lr)
l_paper = Image.open(lp)
l_scissor = Image.open(ls)
l_default = Image.open(ld)
l_up = Image.open(lu)

r_rock = Image.open(rr)
r_paper = Image.open(rp)
r_scissor = Image.open(rs)
r_default = Image.open(rd)
r_up = Image.open(ru)

lrimg_copy= l_rock.copy()
lpimg_copy= l_paper.copy()
lsimg_copy= l_scissor.copy()
ldimg_copy= l_default.copy()
luimg_copy= l_up.copy()

rrimg_copy= r_rock.copy()
rpimg_copy= r_paper.copy()
rsimg_copy= r_scissor.copy()
rdimg_copy= r_default.copy()
ruimg_copy= r_up.copy()

lr_image = ImageTk.PhotoImage(l_rock)
lp_image = ImageTk.PhotoImage(l_paper)
ls_image = ImageTk.PhotoImage(l_scissor)
ld_image = ImageTk.PhotoImage(l_default)
lu_image = ImageTk.PhotoImage(l_up)

rr_image = ImageTk.PhotoImage(r_rock)
rp_image = ImageTk.PhotoImage(r_paper)
rs_image = ImageTk.PhotoImage(r_scissor)
rd_image = ImageTk.PhotoImage(r_default)
ru_image = ImageTk.PhotoImage(r_up)

ll_image = Label(root, image=ld_image,bg=bc1)
ll_image.grid(row=2,column=0,columnspan=2,padx=1,pady=10)
rr_image = Label(root, image=rd_image,bg=bc1)
rr_image.grid(row=2,column=1,columnspan=2,padx=1,pady=10)

x,y=200,200

l_rock = lrimg_copy.resize((x, y))
l_paper = lpimg_copy.resize((x, y))
l_scissor = lsimg_copy.resize((x, y))
l_default = ldimg_copy.resize((x, y))
l_up = luimg_copy.resize((x, y))

r_rock = rrimg_copy.resize((x, y))
r_paper = rpimg_copy.resize((x, y))
r_scissor = rsimg_copy.resize((x, y))
r_default = rdimg_copy.resize((x, y))
r_up = ruimg_copy.resize((x, y))

images={
1:[l_rock,r_rock],
2:[l_paper,r_paper],
3:[l_scissor,r_scissor],
4:[l_default,r_default],
5:[l_up,r_up]
}

call_image(4,4)

c_name=Label(root,text="COMPUTER",fg=bc,bg=bc1)
c_name.grid(row=3,column=0,columnspan=2,padx=1,pady=10)
c_name.config(font=("Gill Sans Ultra Bold", 10))
u_name=Label(root,text="YOU",fg=bc,bg=bc1)
u_name.grid(row=3,column=1,columnspan=2,padx=1,pady=10)
u_name.config(font=("Gill Sans Ultra Bold", 10))

c_count=0
u_count=0
count=0
i=0

def refresh():
	global r_b,s_b,p_b,resetb
	r_b=Button(root,text="ROCK",bg="#9d2464",fg=bc,padx=20,command=lambda: animate(1))
	#r_b.grid(row=5,column=0,padx=1,pady=20)
	r_b.place(x=120,y=435)
	r_b.config(font=("Gill Sans Ultra Bold", 10))

	p_b=Button(root,text="PAPER",bg="#9d2464",fg=bc,padx=13,command=lambda: animate(2))
	#p_b.grid(row=5,column=1,padx=1,pady=20)
	p_b.place(x=282,y=435)
	p_b.config(font=("Gill Sans Ultra Bold",10))

	s_b=Button(root,text="SCISSOR",bg="#9d2464",fg=bc,padx=8,command=lambda: animate(3))
	#s_b.grid(row=5,column=2,padx=1,pady=20)
	s_b.place(x=438,y=435)
	s_b.config(font=("Gill Sans Ultra Bold", 10))
	resetb=Button(root,text="reset",fg=bc,bg="#9d2464",padx=20,command=lambda: reset())
	#resetb.grid(row=6,column=1,padx=1,pady=5)
	resetb.place(x=282,y=500)
	resetb.config(font=("Gill Sans Ultra Bold", 10))

refresh()

root.mainloop()