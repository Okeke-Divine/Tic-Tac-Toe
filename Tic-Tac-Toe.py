import tkinter.messagebox
from tkinter import*

root = Tk()
root.geometry("1200x750")
root.title("Skiyen - Tic Tac Toe")
root.configure(background = 'cadet blue')


Tops = Frame(root, bg='cadet blue', pady =2, width =900, height= 93.3, relief =RIDGE)
Tops.grid(row=0, column=0)




MainFrame = Frame(root, bg = 'Powder blue', pady=2, width=900, height=560, relief =RIDGE)
MainFrame.grid(row=1, column=0)


LeftFrame = Frame(MainFrame , bd=10, width=700, height=466.667, pady=2,padx=10,bg='cadet blue' , relief =RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame , bd=10, width=522.389, height=466.667, pady=2,padx=10,bg='cadet blue' , relief =RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame , bd=10, width=186.667, height=186.667, pady=2,padx=10,bg='cadet blue' , relief =RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame , bd=10, width=186.667, height=186.667, pady=2,padx=10,bg='cadet blue' , relief =RIDGE)
RightFrame2.grid(row=1, column=0)


PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
click = True


def checker (buttons):
	global click
	if buttons["text"] == " " and click == True:
		buttons["text"] = "X"
		click = False
		scorekeeper()
	elif buttons["text"] == " " and click == False:
		buttons["text"] = "O"
		click = True
		scorekeeper()



def scorekeeper():
	if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
		button1.configure(background ="powder blue")
		button2.configure(background ="powder blue")
		button3.configure(background ="powder blue")
		n = float(PlayerX.get())
		score = (n + 1)
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner : Player X", "Just Won A Game")


	if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
		button4.configure(background ="powder blue")
		button5.configure(background ="powder blue")
		button6.configure(background ="powder blue")
		n = float(PlayerX.get())
		score = (n + 1)
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner : Player X", "Just Won A Game")


	if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
		button7.configure(background ="powder blue")
		button8.configure(background ="powder blue")
		button9.configure(background ="powder blue")
		n = float(PlayerX.get())
		score = (n + 1)
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner : Player X", "Just Won A Game")

	if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
		button3.configure(background ="powder blue")
		button5.configure(background ="powder blue")
		button7.configure(background ="powder blue")
		n = float(PlayerX.get())
		score = (n + 1)
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner : Player X", "Just Won A Game")

	if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
		button1.configure(background ="powder blue")
		button5.configure(background ="powder blue")
		button9.configure(background ="powder blue")
		n = float(PlayerX.get())
		score = (n + 1)
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner : Player X", "Just Won A Game")

	if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
		button1.configure(background ="powder blue")
		button4.configure(background ="powder blue")
		button7.configure(background ="powder blue")
		n = float(PlayerX.get())
		score = (n + 1)
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner : Player X", "Just Won A Game")

	if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
		button3.configure(background ="powder blue")
		button5.configure(background ="powder blue")
		button7.configure(background ="powder blue")
		n = float(PlayerX.get())
		score = (n + 1)
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner : Player X", "Just Won A Game")

	if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
		button2.configure(background ="powder blue")
		button5.configure(background ="powder blue")
		button8.configure(background ="powder blue")
		n = float(PlayerX.get())
		score = (n + 1)
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner : Player X", "Just Won A Game")

	if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
		button3.configure(background ="powder blue")
		button6.configure(background ="powder blue")
		button9.configure(background ="powder blue")
		n = float(PlayerX.get())
		score = (n + 1)
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner : Player X", "Just Won A Game")

# player O $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$




	if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
		button1.configure(background ="powder blue")
		button2.configure(background ="powder blue")
		button3.configure(background ="powder blue")
		n = float(PlayerO.get())
		score = (n + 1)
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner : Player O", "Just Won A Game")


	if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
		button4.configure(background ="powder blue")
		button5.configure(background ="powder blue")
		button6.configure(background ="powder blue")
		n = float(PlayerO.get())
		score = (n + 1)
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner : Player O", "Just Won A Game")


	if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
		button7.configure(background ="powder blue")
		button8.configure(background ="powder blue")
		button9.configure(background ="powder blue")
		n = float(PlayerO.get())
		score = (n + 1)
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner : Player O", "Just Won A Game")

	if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
		button3.configure(background ="powder blue")
		button5.configure(background ="powder blue")
		button7.configure(background ="powder blue")
		n = float(PlayerO.get())
		score = (n + 1)
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner : Player O")

	if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
		button1.configure(background ="red")
		button5.configure(background ="red")
		button9.configure(background ="red")
		n = float(PlayerO.get())
		score = (n + 1)
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner : Player O", "Just Won A Game")

	if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
		button1.configure(background ="powder blue")
		button4.configure(background ="powder blue")
		button7.configure(background ="powder blue")
		n = float(PlayerO.get())
		score = (n + 1)
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner : Player O", "Just Won A Game")

	if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
		button3.configure(background ="powder blue")
		button5.configure(background ="powder blue")
		button7.configure(background ="powder blue")
		n = float(PlayerO.get())
		score = (n + 1)
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner : Player O", "Just Won A Game")

	if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
		button2.configure(background ="powder blue")
		button5.configure(background ="powder blue")
		button8.configure(background ="powder blue")
		n = float(PlayerO.get())
		score = (n + 1)
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner : Player O", "Just Won A Game")

	if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
		button3.configure(background ="powder blue")
		button6.configure(background ="powder blue")
		button9.configure(background ="powder blue")
		n = float(PlayerO.get())
		score = (n + 1)
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner : Player O", "Just Won A Game")











def reset():
	button1['text'] =" "
	button2['text'] =" "
	button3['text'] =" "
	button4['text'] =" "
	button5['text'] =" "
	button6['text'] =" "
	button7['text'] =" "
	button8['text'] =" "
	button9['text'] =" "


	button1.configure(background ="gainsboro")
	button2.configure(background ="gainsboro")
	button3.configure(background ="gainsboro")
	button4.configure(background ="gainsboro")
	button5.configure(background ="gainsboro")
	button6.configure(background ="gainsboro")
	button7.configure(background ="gainsboro")
	button8.configure(background ="gainsboro")
	button9.configure(background ="gainsboro")

def NewGame():
	reset()
	PlayerX.set(0)
	PlayerO.set(0)	









lblPlayerX =Label(RightFrame1, font=('Arial',35,'bold'), text="PlayerX :",pady=2,padx=2, bg='cadet blue')
lblPlayerX.grid(row=0, column=0, sticky =W)
txtPlayerX =Entry(RightFrame1, font=('Arial',35,'bold'),bd=2,fg="black", textvariable=PlayerX,width=14,
				justify=LEFT).grid(row=0, column=1,)





lblPlayerO =Label(RightFrame1, font=('Arial',35,'bold'), text="PlayerO :",pady=2,padx=2, bg='cadet blue')
lblPlayerO.grid(row=1, column=0, sticky =W)
txtPlayerO =Entry(RightFrame1, font=('Arial',35,'bold'),bd=2,fg="black", textvariable=PlayerO,width=14,
				justify=LEFT).grid(row=1, column=1,)





btnReset = Button(RightFrame2, text="Reset", font=('Times 26 bold'), height=1, width=20, command =reset)
btnReset.grid(row=0,column=0,padx=6,pady=10)

btnNewGame = Button(RightFrame2, text="New Game", font=('Times 26 bold'), height = 1, width=20, command = NewGame)
btnNewGame.grid(row=1,column=0,padx=6,pady=10)






button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=5, bg='gainsboro', command=lambda:checker(button1))
button1.grid(row=1,column=0, sticky = S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=5, bg='gainsboro', command=lambda:checker(button2))
button2.grid(row=1,column=1, sticky = S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=5, bg='gainsboro', command=lambda:checker(button3))
button3.grid(row=1,column=2, sticky = S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=5, bg='gainsboro', command=lambda:checker(button4))
button4.grid(row=2,column=0, sticky = S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=5, bg='gainsboro', command=lambda:checker(button5))
button5.grid(row=2,column=1, sticky = S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=5, bg='gainsboro', command=lambda:checker(button6))
button6.grid(row=2,column=2, sticky = S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=5, bg='gainsboro', command=lambda:checker(button7))
button7.grid(row=3,column=0, sticky = S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=5, bg='gainsboro', command=lambda:checker(button8))
button8.grid(row=3,column=1, sticky = S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=5, bg='gainsboro', command=lambda:checker(button9))
button9.grid(row=3,column=2, sticky = S+N+E+W)

root.mainloop()