from tkinter import Tk, StringVar, BOTH, W, E, ttk
from tkinter.ttk import Frame, Label,Entry,Button
from lxml import etree as et
class PopUpMessage:

	@staticmethod
	def popupMsg(msg):
		popup = Tk()
		popup.wm_title("Diagnosis")
		popup.geometry("250x100")
		label = ttk.Label(popup, text=msg, font=("Helvetica", 10))
		label.config(anchor="center")
		label.pack(side="top", fill="x", pady=10)
		B1 = ttk.Button(popup, text="Understood", command = popup.destroy)
		B1.pack(expand=1)
		popup.mainloop()
	
	@staticmethod
	def errorMsg(msg, message_size="450x100"):
		popup = Tk()
		popup.wm_title("Error")
		popup.geometry(message_size)
		label = ttk.Label(popup, text=msg, font=("Helvetica", 10))
		label.config(anchor="center")
		label.pack(side="top", fill="x", pady=10)
		B1 = ttk.Button(popup, text="Understood", command = popup.destroy)
		B1.pack(expand=1)
		popup.mainloop()

class Application(Frame):

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

		self.initUI()

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
		self.rowconfigure (10, pad=30)

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

		# create OK button
		button1 = Button (self, text="OK", command=self.onOK )
		button1.grid(row = 10,column=0,sticky=E)

		# create Cancel button
		button2 = Button (self, text="Cancel", command=self.onCancel )
		button2.grid(row = 10,column=1,sticky=E)

	def onOK(self):
		errorsFound = False

		# dataset root element
		dataset_root = et.Element('Dataset')
		# patient root element
		patient_root = et.SubElement(dataset_root, 'Patient')
		# validate error message
		if (self.id.get() == '' and not errorsFound):
			PopUpMessage.errorMsg("Input a numeric Patient value")
			errorsFound = True
		# Values for patient id
		patient_root.set('id', self.id.get())

		# for item in app.grid_slaves():
		for i in range(1,10):
			current_widget = self.grid_slaves(i, 0)[0]
			stripped_label = current_widget.cget("text").strip(" :")
			final_label = stripped_label.replace(" ", "_")
			input_val = self.grid_slaves(i, 1)[0].get()
			if (input_val == "" or not input_val.isdigit() ):
				PopUpMessage.errorMsg("Input a numeric value for " + final_label)
				errorsFound = True
				break
			else:
				et.SubElement(patient_root, str(final_label) ).text = input_val
		
		if not errorsFound:
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

			patient_xml = et.tostring(dataset_root)
			with open("test.xml","wb") as f:
				f.write(patient_xml)

	def onCancel(self):
		# exit program
		self.quit()

def main():

	root = Tk()
	root.geometry("400x290")
	app = Application(root)
	root.mainloop()

	# for item in app.grid_slaves():
	# for i in range(10):
	# 	print("row is {} value is {}".format(app.grid_slaves(i, 0)[0].cget("text"), app.grid_slaves(i, 1)[0].get() ) )
	# 	print(app.grid_slaves(i, 0)[0].cget("text").strip(" :") )
		
if __name__ == '__main__':
	main ()