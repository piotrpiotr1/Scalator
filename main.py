# Import the required libraries
# coding: utf8
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
from tkinter.simpledialog import askstring
import PyPDF2
from tkinter import messagebox
from fpdf import FPDF


def retrieve():
    
    pdf = FPDF()
  
    # Add a page
    pdf.add_page()
      
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
      
    # create a cell
    pdf.cell(200, 10, txt = str(my_entry.get()), 
             ln = 1, align = 'C')

    pdf.cell(200, 10, txt = str(my_entry.get()), 
             ln = 2, align = 'C')
      
    pdf.cell(200, 10, txt = str(my_entry.get()), 
             ln = 3, align = 'C')
 
    # save the pdf with name .pdf
    pdf.output("okladka.pdf")
    messagebox.showinfo("showinfo", "Utworzono okładkę")
    window.destroy()

def NewCover():
    global Button
    global my_entry
    global my_entry2
    global my_entry3
    global window
    window = Toplevel()
    window.geometry('300x150')
    newCoverlabel = Label(window, text = "Stwórz nową okładkę")
    newCoverlabel.pack()
 
    my_entry = Entry(window, width = 50)
    my_entry.insert(0,'Tytuł')
    my_entry.pack(padx = 5, pady = 5)   

    my_entry2 = Entry(window, width = 20)
    my_entry2.insert(0,'Podtytuł')
    my_entry2.pack(padx = 5, pady = 5)


    my_entry3 = Entry(window, width = 20)
    my_entry3.insert(0,'EAN')
    my_entry3.pack(padx = 5, pady = 5)

    Button = Button(window, text = "Zapisz", command = retrieve)
    Button.pack(padx = 5, pady = 5)
 
   
    

# Create an instance of tkinter frame or window
win = Tk()

# Title
win.title('Scalator 1.0')


# Set the geometry of tkinter frame
win.geometry("700x350")

# Creating Menubar
menubar = Menu(win)

cover = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Okładka', menu = cover)
cover.add_command(label ='Nowa okładka', command = NewCover)

cover.add_separator()
cover.add_command(label ='Koniec', command = win.destroy)


pdfMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Scalanie', menu = pdfMenu)
pdfMenu.add_command(label ='Scal pliki', command = None)

help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Pomoc', menu = help_)
help_.add_command(label ='FAQ', command = None)
help_.add_command(label ='Kontakt', command = None)
help_.add_separator()
help_.add_command(label ='Zgłość błąd', command = None)



def PDFmerge(pdfs, output):
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()

    # appending pdfs one by one
    for pdf in pdfs:
        pdfMerger.append(pdf)

    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)
    messagebox.showinfo("showinfo", "Scalanie plików zakończone sukcesem")


def open_file():
   file = fd.askopenfilenames(parent=win, title='Wybierz plik')
   pdfs = win.splitlist(file)
   output = 'combined_example.pdf'
   PDFmerge(pdfs=pdfs, output=output)
   



 





# Add a Button Widget

ttk.Button(win, text="Zaznacz wiele plików PDF", command=open_file).pack()
win.config(menu = menubar)
win.mainloop()








  
