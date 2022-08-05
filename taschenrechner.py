from Tkinter import *

#takes string, puts out a list of strings of numbers and operators
def cutMyStringIntoPieces(string):
	pieces = []
	text = ""
	for i in string:
		if i in "+-*/^()":
			if text != "":
				pieces.append(float(text))
			pieces.append(i)
			text = ""
		else:
			text += i
	if text != "":
		pieces.append(float(text))
	elif pieces[len(pieces)-1] != ")":
		print("-ERROR: operation at the end of the formula.")
		return []
	return pieces


#finds the position of something in a string
def find(someList, what):
	n = -1
	for i in someList:
		n += 1
		if i == what:
			return n
	print("-ERROR: no such symbol in list.")


class window():
	def __init__(self, master):
		self.master = master
		
		inputs = Entry(master, justify = "right")
		inputs.grid(row = 0, columnspan = 6, sticky = N+E+S+W)
		
		num = []
		num.append(Button(master, text = "0", command = lambda: self.chInputs(inputs, "0")))
		num[0].grid(row = 4, column = 0, sticky = N+E+S+W)
		num.append(Button(master, text = "1", command = lambda: self.chInputs(inputs, "1")))
		num[1].grid(row = 3, column = 0, sticky = N+E+S+W)
		num.append(Button(master, text = "2", command = lambda: self.chInputs(inputs, "2")))
		num[2].grid(row = 3, column = 1, sticky = N+E+S+W)
		num.append(Button(master, text = "3", command = lambda: self.chInputs(inputs, "3")))
		num[3].grid(row = 3, column = 2, sticky = N+E+S+W)
		num.append(Button(master, text = "4", command = lambda: self.chInputs(inputs, "4")))
		num[4].grid(row = 2, column = 0, sticky = N+E+S+W)
		num.append(Button(master, text = "5", command = lambda: self.chInputs(inputs, "5")))
		num[5].grid(row = 2, column = 1, sticky = N+E+S+W)
		num.append(Button(master, text = "6", command = lambda: self.chInputs(inputs, "6")))
		num[6].grid(row = 2, column = 2, sticky = N+E+S+W)
		num.append(Button(master, text = "7", command = lambda: self.chInputs(inputs, "7")))
		num[7].grid(row = 1, column = 0, sticky = N+E+S+W)
		num.append(Button(master, text = "8", command = lambda: self.chInputs(inputs, "8")))
		num[8].grid(row = 1, column = 1, sticky = N+E+S+W)
		num.append(Button(master, text = "9", command = lambda: self.chInputs(inputs, "9")))
		num[9].grid(row = 1, column = 2, sticky = N+E+S+W)
		
		opsa = Button(master, text = "+", command = lambda: self.chInputs(inputs, "+"))
		opsa.grid(row = 1, column = 3, sticky = N+E+S+W)
		opss = Button(master, text = "-", command = lambda: self.chInputs(inputs, "-"))
		opss.grid(row = 2, column = 3, sticky = N+E+S+W)
		opsm = Button(master, text = "*", command = lambda: self.chInputs(inputs, "*"))
		opsm.grid(row = 3, column = 3, sticky = N+E+S+W)
		opsd = Button(master, text = "/", command = lambda: self.chInputs(inputs, "/"))
		opsd.grid(row = 4, column = 3, sticky = N+E+S+W)
		
		dot = Button(master, text = ".", command = lambda: self.chInputs(inputs, "."))
		dot.grid(row = 4, column = 1, sticky = N+E+S+W)
		
		eq = Button(master, text = "=", command = lambda: self.equals(inputs))
		eq.grid(row = 4, column = 2, sticky = N+E+S+W)
		
		delete = Button(master, text = "del", command = lambda: inputs.delete(0, "end"))
		delete.grid(row = 1, column = 4, sticky = N+E+S+W)
		
		CE = Button(master, text = "CE", command = lambda: self.deleteLast(inputs))
		CE.grid(row = 2, column = 4, sticky = N+E+S+W)
		
		power = Button(master, text = "^", command = lambda: self.chInputs(inputs, "^"))
		power.grid(row = 3, column = 4, sticky = N+E+S+W)
		
		openBracket = Button(master, text = "(", command = lambda: self.chInputs(inputs, "("))
		openBracket.grid(row = 4, column = 4, sticky = N+E+S+W)
		
		closedBracket = Button(master, text = ")", command = lambda: self.chInputs(inputs, ")"))
		closedBracket.grid(row = 4, column = 5, sticky = N+E+S+W)
		

	def chInputs(self, inp, i):
		text = inp.get()
		if i in ".+-*/^":
			if len(text) == 0:
				return
			elif text[len(text)-1] in ".+-*/^":
				return
		inp.insert(len(inp.get()), i)
		
		
	def equals(self, inp):
		formula = cutMyStringIntoPieces(inp.get())
		if formula == []:
			print("-ERROR: formula is incorrect/ cannot be computed.")
			return
#		for i in range(0,len(formula)-1):
#			if i != (len(formula)-1) and formula[i] in "+-*/" and formula[i+1] in "+-*/":
#				print("-ERROR: operation following an operation.")
#				return
		ops = "^/*-+"
		while "(" in formula:
			j = find(formula, ")")
			k = j
			while formula[k] != "(":
				k -= 1
			smallForm = formula[k:j+1]
			for o in ops:
				while o in smallForm:
					i = find(smallForm, o)
					if o == "^":
						smallForm[i] = smallForm[i-1] ** smallForm[i+1]
					elif o == "/":
						smallForm[i] = smallForm[i-1] / smallForm[i+1]
					elif o == "*":
						smallForm[i] = smallForm[i-1] * smallForm[i+1]
					elif o == "-":
						smallForm[i] = smallForm[i-1] - smallForm[i+1]
					elif o == "+":
						smallForm[i] = smallForm[i-1] + smallForm[i+1]
					del smallForm[i+1]
					del smallForm[i-1]
			formula[k] = smallForm[1]
			while(formula[k+1] != ")"):
				del formula[k+1]
			del formula[k+1]
		while "^" in formula:
			i = find(formula, "^")
			formula[i] = formula[i-1] ** formula[i+1]
			del formula[i+1]
			del formula[i-1]
		while "/" in formula:
			i = find(formula, "/")
			formula[i] = formula[i-1] / formula[i+1]
			del formula[i+1]
			del formula[i-1]
		while "*" in formula:
			i = find(formula, "*")
			formula[i] = formula[i-1] * formula[i+1]
			del formula[i+1]
			del formula[i-1]
		while "-" in formula:
			i = find(formula, "-")
			formula[i] = formula[i-1] - formula[i+1]
			del formula[i+1]
			del formula[i-1]
		while "+" in formula:
			i = find(formula, "+")
			formula[i] = formula[i-1] + formula[i+1]
			del formula[i+1]
			del formula[i-1]
		inp.delete(0, "end")
		inp.insert(0, formula[0])
		return formula[0]
		
	
	def deleteLast(self, inp):
		if len(inp.get()) == 0:
			return
		inp.delete(len(inp.get())-1, "end")


if __name__ == "__main__":
	root = Tk()
	widgets = window(root)
	root.mainloop()
