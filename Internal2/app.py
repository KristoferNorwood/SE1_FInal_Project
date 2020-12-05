#!/usr/bin/python
from tkinter import Tk, StringVar, BOTH, W, E, ttk
from tkinter.ttk import Frame, Label,Entry,Button
from lxml import etree as et
import socket
import time
import tkinter.font as tkFont
from typing import List
import pinkServer
import processClientData
import logging


class PopUpMessage:
	@staticmethod
	def popupMsg(cancer):
		popup = Tk()
		popup.wm_title("Diagnosis")
		popup.geometry("250x100")
		if(cancer):
			msg = 'Sorry to inform you the diagnosis is Cancer'
		else:
			msg = 'Happy to inform you the diagnosis is non-cancerous'
		label = ttk.Label(popup, text=msg, font=("Helvetica", 10))
		label.config(anchor="center")
		label.pack(side="top", fill="x", pady=10)
		B1 = ttk.Button(popup, text="Understood", command = popup.destroy)
		B1.pack(expand=1)
		popup.mainloop()

class guiApplication(Frame):
	def __init__(self, parent):

		Frame.__init__(self,parent)

		self.parent = parent
		
		# Form list defaults
		self.id = StringVar()
		self.clump_thickness = StringVar()
		self.uniformity_cell_size = StringVar()
		self.uniformity_cell_shape = StringVar()
		self.marginal_adhesion = StringVar()
		self.single_epithelial_cell_size = StringVar()
		self.bare_nuclei = StringVar()
		self.bland_chromatin = StringVar()
		self.normal_nucleoli = StringVar()
		self.mitoses = StringVar()
		self.cancer_class = StringVar()

		self.initUI()
		# self.main()

	def initUI(self):

		# Set frame title
		self.parent.title("PinkRay")

		# pack frame
		self.pack (fill=BOTH, expand=1)

		# configure grid columns
		self.columnconfigure (0, pad=3)
		self.columnconfigure (1, pad=3)

		# configure grid rows
		self.rowconfigure (0, pad=3)
		self.rowconfigure (1, pad=3)
		self.rowconfigure (2, pad=3)
		self.rowconfigure (3, pad=3)
		self.rowconfigure (4, pad=3)
		self.rowconfigure (6, pad=3)
		self.rowconfigure (7, pad=3)
		self.rowconfigure (8, pad=3)
		self.rowconfigure (9, pad=3)
		self.rowconfigure (10, pad=3)
		self.rowconfigure (11, pad=30)

		# Patient ID Label
		id_text = Label(self,text="id: ", font="Mono 10 bold")
		id_text.grid(row = 0, column=0, sticky=W)
		
		# Patient ID Form
		id_form = Entry(self,width=30, textvariable = self.id, font="Mono 10 bold")
		id_form.grid(row=0, column=1)

		# Clump Thickness Label
		clump_thickness_text = Label(self,text="clump thickness: ", font="Mono 10 bold")
		clump_thickness_text.grid(row = 1, column = 0, sticky=W)
		
		# Clump Thickness Form
		clump_thickness_form = Entry(self,width=30, textvariable=self.clump_thickness, font="Mono 10 bold")
		clump_thickness_form.grid(row=1, column=1)

		# Uniformity Cell Size Label
		uniformity_cell_size_text = Label(self,text="uniformity cell size: ", font="Mono 10 bold")
		uniformity_cell_size_text.grid(row = 2, column = 0, sticky=W)

		# Uniformty Cell Size Form
		uniformity_cell_size_form = Entry(self,width=30,textvariable=self.uniformity_cell_size, font="Mono 10 bold")
		uniformity_cell_size_form.grid(row=2, column = 1)

		# Uniformity Cell Shape Label
		uniformity_cell_shape_text = Label(self,text="uniformity cell shape: ", font="Mono 10 bold")
		uniformity_cell_shape_text.grid(row=3, column = 0, sticky=W)
		
		# uniformity_cell_shape form
		uniformity_cell_shape_form = Entry(self,width=30,textvariable=self.uniformity_cell_shape, font="Mono 10 bold")
		uniformity_cell_shape_form.grid(row=3, column = 1)

		marginal_adhesion_text = Label(self, text="marginal adhesion: ", font="Mono 10 bold")
		marginal_adhesion_text.grid(row=4, column = 0, sticky=W)
		
		# marginal_adhesion form
		marginal_adhesion_form = Entry(self,width=30,textvariable=self.marginal_adhesion, font="Mono 10 bold")
		marginal_adhesion_form.grid(row=4, column = 1)

		# single_epithelial_cell_size_text
		single_epithelial_cell_size_text = Label(self, text="single epithelial cell size: ", font="Mono 10 bold")
		single_epithelial_cell_size_text.grid(row=5, column = 0, sticky=W)
		
		# single_epithelial_cell_size form
		single_epithelial_cell_size_form = Entry(self,width=30,textvariable=self.single_epithelial_cell_size, font="Mono 10 bold")
		single_epithelial_cell_size_form.grid(row=5, column = 1)

		# bare_nuclei_text
		bare_nuclei_text = Label(self, text="bare nuclei: ", font="Mono 10 bold")
		bare_nuclei_text.grid(row=6, column = 0, sticky=W)
		
		# bare_nuclei form
		bare_nuclei_form = Entry(self,width=30,textvariable=self.bare_nuclei, font="Mono 10 bold")
		bare_nuclei_form.grid(row=6, column = 1)

		# bland_chromatin_text
		bland_chromatin_text = Label(self, text="bland_chromatin: ", font="Mono 10 bold")
		bland_chromatin_text.grid(row=7, column = 0, sticky=W)
		
		# bland_chromatin form
		bland_chromatin_form = Entry(self,width=30,textvariable=self.bland_chromatin, font="Mono 10 bold")
		bland_chromatin_form.grid(row=7, column = 1)

		# normal_nucleoli_text
		normal_nucleoli_text = Label(self, text="normal nucleoli: ", font="Mono 10 bold")
		normal_nucleoli_text.grid(row=8, column = 0, sticky=W)
		
		# normal_nucleoli form
		normal_nucleoli_form = Entry(self,width=30,textvariable=self.normal_nucleoli, font="Mono 10 bold")
		normal_nucleoli_form.grid(row=8, column = 1)

		# mitoses_text
		mitoses_text = Label(self, text="mitoses: ", font="Mono 10 bold")
		mitoses_text.grid(row=9, column = 0, sticky=W)
		
		# mitoses form
		mitoses_form = Entry(self,width=30,textvariable=self.mitoses, font="Mono 10 bold")
		mitoses_form.grid(row=9, column = 1)
		
		# cancer_class_text
		cancer_class_text = Label(self, text="class: ", font="Mono 10 bold")
		cancer_class_text.grid(row=10, column = 0, sticky=W)
		
		# cancer_class form
		cancer_class_form = Entry(self,width=30,textvariable=self.cancer_class, font="Mono 10 bold")
		cancer_class_form.grid(row=10, column = 1)

		# create OK button
		button1 = Button (self, text="OK", command=self.onOK )
		button1.grid(row = 11,column=0,sticky=E)

		# create Cancel button
		button2 = Button (self, text="Cancel", command=self.onCancel )
		button2.grid(row = 11,column=1,sticky=E)

	def onOK(self):

		# dataset root element
		dataset_root = et.Element('Dataset')
		
		# patient root element
		patient_root = et.SubElement(dataset_root, 'Patient')
		patient_root.set('id', self.id.get())

		# Subtag Clump_thickness inside of root element Patient
		clump_thickness_elem = et.SubElement(patient_root, 'clump_thickness')
		# Values for subtag clump_thickness
		clump_thickness_elem.text = self.clump_thickness.get()

		# Subtag uniformity_cell_size inside of root element Patient
		uniformity_cell_size_elem = et.SubElement(patient_root, 'uniformity_cell_size')
		# Values for uniformity_cell_size
		uniformity_cell_size_elem.text = self.uniformity_cell_size.get()

		# Subtag uniformity_cell_shape inside of root element Patient
		uniformity_cell_shape_elem = et.SubElement(patient_root, 'uniformity_cell_shape')
		# Values for uniformity_cell_shape
		uniformity_cell_shape_elem.text = self.uniformity_cell_shape.get()

		# Subtag marginal_adhesion inside of root element Patient
		marginal_adhesion_elem = et.SubElement(patient_root, 'marginal_adhesion')
		# Values for marginal_adhesion
		marginal_adhesion_elem.text = self.marginal_adhesion.get()

		# Subtag single_epithelial_cell_size inside of root element Patient
		single_epithelial_cell_size_elem = et.SubElement(patient_root, 'single_epithelial_cell_size')
		# Values for single_epithelial_cell_size
		single_epithelial_cell_size_elem.text = self.single_epithelial_cell_size.get()

		# Subtag bare_nuclei inside of root element Patient
		bare_nuclei_elem = et.SubElement(patient_root, 'bare_nuclei')
		# Values for bare_nuclei
		bare_nuclei_elem.text = self.bare_nuclei.get()

		# Subtag bland_chromatin inside of root element Patient
		bland_chromatin_elem = et.SubElement(patient_root, 'bland_chromatin')
		# Values for bland_chromatin
		bland_chromatin_elem.text = self.bland_chromatin.get()

		# Subtag normal_nucleoli inside of root element Patient
		normal_nucleoli_elem = et.SubElement(patient_root, 'normal_nucleoli')
		# Values for normal_nucleoli
		normal_nucleoli_elem.text = self.normal_nucleoli.get()

		# Subtag mitoses inside of root element Patient
		mitoses_elem = et.SubElement(patient_root, 'mitoses')
		# Values for mitoses
		mitoses_elem.text = self.mitoses.get()

		# Subtag cancer_class inside of root element Patient
		cancer_class_elem = et.SubElement(patient_root, 'class')
		# Values for cancer_class
		# cancer_class_elem.text = self.cancer_class.get()
		

		# Clear form after confirmation
		self.id.set("")
		self.clump_thickness.set("")
		self.uniformity_cell_size.set("")
		self.uniformity_cell_size.set("")
		self.uniformity_cell_shape.set("")
		self.marginal_adhesion.set("")
		self.single_epithelial_cell_size.set("")
		self.bare_nuclei.set("")
		self.bland_chromatin.set("")
		self.normal_nucleoli.set("")
		self.mitoses.set("")
		# self.cancer_class.set("")

		patient_xml = et.tostring(dataset_root)
		with open("test.xml","wb") as f:
			f.write(patient_xml)
		file = open(r"test.xml", "rb")
		stream = file.read(65536)
		cancer = processClientData.clientDiag(stream)
		PopUpMessage.popupMsg(cancer)

		# s = socket.socket()
		# s.connect(("98.168.143.109", 7123))
		# s.settimeout(30)
		# while stream:
		# 	flag = "myapp"
		# 	myFlag = str.encode(flag)
		# 	s.send(myFlag)
		# 	if(s.recv(32)):
		# 		s.send(stream)
		# 	data = s.recv(65536)
		# 	myData = data.decode("utf8")
		# 	print(myData)
		# 	result = 0
		# 	root = et.fromstring(myData)
		# 	for patient in root: 
		# 		result = patient.find('class').text
		# 	if int(result) == 2:
		# 		print("\nYOU'RE GONNA DIE")
		# 	else:
		# 		print("\nYou're probably gonna be ok.")
		# 	if "/Dataset".encode('utf-8') in data:
		# 		break
		# s.close()
   
	def onCancel(self):

		# exit program
		self.quit()

def get_logger(name):
    log_format = '%(asctime)s  %(name)8s  %(levelname)5s  %(message)s'
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        filename='PinkRayLog.log',
                        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter(log_format))
    logging.getLogger(name).addHandler(console)
    return logging.getLogger(name)

def main():
	myLogger = get_logger('myLogger')
	pinkServer.startServer()
	myLogger.info('Pink Ray Ready to Serve')
	root = Tk()
	font = tkFont.Font(family="Helvetica",weight="bold")
	root.geometry("400x320")
	app = guiApplication(root)
	root.mainloop()


if __name__ == '__main__':
	main ()