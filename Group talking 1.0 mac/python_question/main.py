from Tkinter import *
from login import main
import tkMessageBox, urllib, check, httplib, urllib2, time
def login():
	while True:
		userinfo = main()
		passt = check.check(userinfo['Gn'], userinfo['Gp'],
		 userinfo['Un'], userinfo['Up'])
		if passt:
			break
def get_version():
	tkMessageBox.showinfo('Version','The Group Talking version is 1.0')
login()
window = Tk(className = ' Group Talking ')
#window.maxsize(550, 400)
window.minsize(550,400)
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="About", command=get_version)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

menubar.add_cascade(label="Group Talking", menu=filemenu)
window.config(menu=menubar)
Lb1 = Listbox(window, height = 30)

from user import user, g, un
n = 1
for i in user[g][1]:
	Lb1.insert(n, i)
	n+=1
Lb1.pack(side = LEFT)

get = ''
def sendmessage():
	get = talkinput.get()
	talkinput.delete(0, END)
	data = {'Un':un,'Text':get,'Date':time.localtime().tm_yday}
	url = 'http://orangeapple-student-data.appspot.com/pt'
	data = urllib.urlencode(data)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	

labelframe = LabelFrame(window, text = "Talking", height = 100,
	 width = 150)

var = StringVar()
label = Label( labelframe, textvariable=var )
var.set("")
label.pack(side = LEFT)


labelframe.pack(fill = "both", expand = "yes", side = TOP)
talkinput = Entry(window, width=40)
talkinput.pack( side = RIGHT)
subtalk = Button( window, text = 'send', command = sendmessage)
subtalk.pack()
def task(var):
	u = urllib2.urlopen("http://orangeapple-student-data.appspot.com/pt")
	window.update()
	data = u.read()
	data = data.replace("u'","")
	data = data.replace("'","")
	data = data.split("<br> ")
	w = ""
	for i in data:
		word = (str(i.split('s+s')).replace("', '"," "))[2:-2]
		date = 0
		f = word.find(' ')+1
		while word.find(' ',f) != -1:
			f = word.find(' ',f)+1
		try:
			date = str(time.localtime().tm_yday - int(word[f:]))
		except:
			date = ""
		word = word[ :word.find(' ')]+"  :  "+word[word.find(' ')+1:(len(date))*-1] 
		w += word + "\n"+date+"\n\n"

	var.set(w)
	u.close()

def f(var):
	while True:
		window.after(500,task(var))
window.after(0,f(var))
window.mainloop()


