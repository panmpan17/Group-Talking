from Tkinter import *
def main():
	Userifo = {}
	window = Tk(className = " User Login ")
	menu = Menu(window)
	filemenu = Menu(menu, tearoff = 0)
	window.config(menu = menu)
	var = StringVar()
	label = Label( window, textvariable = var, relief = RAISED )
	var.set("Group Name :")
	label.pack()
	EGN = Entry(window,bd = 1)
	EGN.pack()
	var1 = StringVar()
	label = Label( window, textvariable = var1, relief = RAISED )
	var1.set("Group Password :")
	label.pack()
	EGP = Entry(window,bd = 1)
	EGP.pack()
	labelframe = LabelFrame(window, text = "Member")
	labelframe.pack(fill = "both", expand = "yes",side = TOP)
	var2 = StringVar()
	label = Label( labelframe, textvariable = var2, relief = RAISED )
	var2.set("User Name :")
	label.pack()
	UGN = Entry(labelframe,bd = 1)
	UGN.pack()
	var3 = StringVar()
	label = Label( labelframe, textvariable = var3, relief = RAISED )
	var3.set("User Password :")
	label.pack()
	UGP = Entry(labelframe,bd = 1)
	UGP.pack()
	buttton = Button(window, text = "Submit", command = window.quit)
	buttton.pack()
	window.mainloop()
	Userifo['Gn'] = EGN.get()
	Userifo['Gp'] = EGP.get()
	Userifo['Un'] = UGN.get()
	Userifo['Up'] = UGP.get()
	return Userifo