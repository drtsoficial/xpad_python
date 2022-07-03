import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:

	__root = Tk()

	# Default width and height
	__thisWidth = 300
	__thisHeight = 300
	__thisTextArea = Text(__root)
	__thisMenuBar = Menu(__root)
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0)
	__thisEditMenu = Menu(__thisMenuBar, tearoff=0)
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
	
	# Add scrollbar
	__thisScrollBar = Scrollbar(__thisTextArea)	
	__file = None

	def __init__(self,**kwargs):

		# Set Icon
		try:
				self.__root.wm_iconbitmap("icon.ico")
		except:
				pass

		# Set window size

		try:
			self.__thisWidth = kwargs['width']
		except KeyError:
			pass

		try:
			self.__thisHeight = kwargs['height']
		except KeyError:
			pass

		# Set the window title
		self.__root.title("Untitled - Xpad")

		# Center the window
		screenWidth = self.__root.winfo_screenwidth()
		screenHeight = self.__root.winfo_screenheight()
	
		# Left align
		left = (screenWidth / 2) - (self.__thisWidth / 2)
		
		# Right align
		top = (screenHeight / 2) - (self.__thisHeight /2)
		
		# Top and bottom align
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
											self.__thisHeight,
											left, top))

		# Textarea auto resizable
		self.__root.grid_rowconfigure(0, weight=1)
		self.__root.grid_columnconfigure(0, weight=1)

		# Add controls
		self.__thisTextArea.grid(sticky = N + E + S + W)
		
		# Open new file
		self.__thisFileMenu.add_command(label="Novo",
										command=self.__newFile)
		
		# Open a already existing file
		self.__thisFileMenu.add_command(label="Abrir",
										command=self.__openFile)
		
		# Save current file
		self.__thisFileMenu.add_command(label="Salvar",
										command=self.__saveFile)

		# Create a line in the dialog	
		self.__thisFileMenu.add_separator()										
		self.__thisFileMenu.add_command(label="Sair",
										command=self.__quitApplication)
		self.__thisMenuBar.add_cascade(label="Arquivo",
									menu=self.__thisFileMenu)	
		
		# Give a feature of cut
		self.__thisEditMenu.add_command(label="Cortar",
										command=self.__cut)			
	
		# Give a feature of copy
		self.__thisEditMenu.add_command(label="Copiar",
										command=self.__copy)		
		
		# Give a feature of paste
		self.__thisEditMenu.add_command(label="Colar",
										command=self.__paste)		
		
		# Give a feature of editing
		self.__thisMenuBar.add_cascade(label="Editar",
									menu=self.__thisEditMenu)	
		
		# Create a feature of description of the notepad
		self.__thisHelpMenu.add_command(label="Sobre Xpad",
										command=self.__showAbout)
		self.__thisMenuBar.add_cascade(label="Ajuda",
									menu=self.__thisHelpMenu)

		self.__root.config(menu=self.__thisMenuBar)

		self.__thisScrollBar.pack(side=RIGHT,fill=Y)				
		
		# Scrollbar will adjust automatically according to the content	
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)	
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
	
		
	def __quitApplication(self):
		self.__root.destroy()
	

	def __showAbout(self):
		showinfo("Xpad","Victor Nascimento")

	def __openFile(self):
		
		self.__file = askopenfilename(defaultextension=".txt",
									filetypes=[("All Files","*.*"),
										("Text Documents","*.txt")])

		if self.__file == "":
			
			# No file to open
			self.__file = None
		else:
			
			# Try to open the file
			# set the window title
			self.__root.title(os.path.basename(self.__file) + " - Xpad")
			self.__thisTextArea.delete(1.0,END)

			file = open(self.__file,"r")

			self.__thisTextArea.insert(1.0,file.read())

			file.close()

		
	def __newFile(self):
		self.__root.title("Untitled - Xpad")
		self.__file = None
		self.__thisTextArea.delete(1.0,END)

	def __saveFile(self):

		if self.__file == None:
			# Save as new file
			self.__file = asksaveasfilename(initialfile='Xpad.txt',
											defaultextension=".txt",
											filetypes=[("All Files","*.*"),
												("Text Documents","*.txt")])

			if self.__file == "":
				self.__file = None
			else:
				
				# Try to save the file
				file = open(self.__file,"w")
				file.write(self.__thisTextArea.get(1.0,END))
				file.close()
				
				# Change the window title
				self.__root.title(os.path.basename(self.__file) + " - Xpad")
				
			
		else:
			file = open(self.__file,"w")
			file.write(self.__thisTextArea.get(1.0,END))
			file.close()

	def __cut(self):
		self.__thisTextArea.event_generate("<<Cut>>")

	def __copy(self):
		self.__thisTextArea.event_generate("<<Copy>>")

	def __paste(self):
		self.__thisTextArea.event_generate("<<Paste>>")

	def run(self):

		# Run main application
		self.__root.mainloop()




# Run main application
xpad = Notepad(width=600,height=400)
xpad.run()
