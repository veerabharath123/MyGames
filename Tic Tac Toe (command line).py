#tic tac toe
from os import system
from time import sleep
from random import randint 

abc="cls"
end=0

def toss():
	system(abc)
	print("-TOSS-\n")
	toss=int(input("1.heads 2.tails\n"))
	for tossv in range(0,3):
		system(abc)
		print("/")
		sleep(0.5)
		system(abc)
		print("\\")
		sleep(0.5)
	system(abc)
	print("-TOSS-\n")
	tossr=randint(1,2)
	if tossr==1:
		print("HEADS\n")
	else:
		print("TAILS\n")
	print("Heads=x\nTails=o" )
	sleep(3)

def instructions():
	global x1,y1,temp
	system(abc)
	vals=1
	x1=y1=""
	for i1 in range(1,4):
		for j1 in range(0,3):
			x1=x1+" "+str(vals)+" "
			vals+=1
			if j1<2:
				x1=x1+"|"
			else:
				pass
			if i1<3:
				for k1 in range(0,3):
					y1=y1+"-"
				y1=y1+" "
			else:
				pass
		print(x1)
		print(y1)
		x1=""
		y1=""
	print("---INSTRUCTIONS---\n\n-Each box is denoted with a number.\n\n-Enter the number where you want to place your mark.\n")
	inv=input("Press ENTER to start the game.\n")
	sleep(0.5)
	toss()

def reset(ins):
	global temp,count,move
	move="x"
	count=0
	temp={
	1:["   ","   ","   "],
	2:["   ","   ","   "],
	3:["   ","   ","   "]
	}
	if ins==1:
		instructions()
	else:
		pass

reset(1)

def gameend():
	global end
	op=int(input("1.play again 2.exit\n"))
	if op==2:
		end=1
	else:
		reset(0)

def show():
	global temp
	x=y=""
	for i in range(1,4):
		for j in range(0,3):
			x=x+(str(temp[i][j]))
			if j<2:
				x=x+"|"
			else:
				pass
			if i<3:
				for k in range(0,3):
					y=y+"-"
				y=y+" "
			else:
				pass
		print(x)
		print(y)
		x=""
		y=""

def checkxo(a,b,c,a1,b1,c1):
	if temp[a1][a]==" x " and temp[b1][b]==" x " and temp[c1][c]==" x ":
		system(abc)
		show()
		print("X WINS")
		gameend()
		
	elif temp[a1][a]==" o " and temp[b1][b]==" o " and temp[c1][c]==" o ":
		system(abc)
		show()
		print("O WINS")
		gameend()
		
	else:
		if count==9 and temp[a1][a]!=" x " and temp[b1][b]!=" x " and temp[c1][c]!=" x ":
			system(abc)
			show()
			print("DRAW")
			gameend()

def check():
	n1=0
	n2=1
	n3=2
	val=0
	for a in range(1,9):
		if  a<4:
			val+=1
			checkxo(n1,n2,n3,val,val,val)
		elif a<7:
			if n1+2==n2+1==n3:
				n1=0
				n2=0
				n3=0
				val=1
			else:
				n1+=1
				n2+=1
				n3+=1
			checkxo(n1,n2,n3,val,val+1,val+2)
		else:
			if n1==n2==n3:
				n1=0
				n2=1
				n3=2
				val=1
			else:
				n1+=2
				n3-=2
			checkxo(n1,n2,n3,val,val+1,val+2)

while True:
	global move,count
	if end==1:
		break
	else:
		pass
	system(abc)
	show()
	
	pos=int(input("Enter the position of "+move+":\n"))
	e3=pos
	if pos!=0 and pos<4:
		e1=1
		pos-=1
	elif pos!=0 and pos<7:
		e1=2
		pos-=4
	elif pos!=0 and pos<10:
		e1=3
		pos-=7
	else:
		move=""
		
	e2=pos
	
	if move=="x" and temp[e1][e2]=="   ":
		temp[e1][e2]=" x "
		count+=1
		move="o"
		system(abc)
		show()
		check()
		
	elif move=="o" and temp[e1][e2]=="   ":
		temp[e1][e2]=" o "
		count+=1
		move="x"
		system(abc)
		show()
		check()
		
	else:
		if e3==0 or pos>9:
			system(abc)
			show()
			print("Enter a number from 1 to 9")
			sleep(3)
			
		elif temp[e1][e2]==" x " or temp[e1][e2]==" o ":
			system(abc)
			show()
			print("Select an empty space")
			sleep(3)
		else:
			pass