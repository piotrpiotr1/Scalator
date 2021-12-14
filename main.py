# Import the required libraries
# coding: utf8
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
import tkinter as tk
from tkinter.simpledialog import askstring
import PyPDF2
from tkinter import messagebox
from fpdf import FPDF
from barcode import EAN13
from barcode.writer import ImageWriter
import os



# Generate new cover PDF
def coverPDF():
    
    pdf = FPDF()
  
    # Add a page
    pdf.add_page()
      
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
      
    # create a cell
    pdf.cell(200, 10, txt = str(my_entry.get()), 
             ln = 1, align = 'C')

    pdf.cell(200, 10, txt = str(my_entry2.get()), 
             ln = 2, align = 'C')

    number = my_barcode.get()
    my_code = EAN13(number, writer=ImageWriter())
    my_code.save("new_code1")
  
    # Our barcode is ready. Let's save it.
    

      
    pdf.image("new_code1.png", x = None, y = None, w = 0, h = 0, type = '', link = '')
    
    # save the pdf with name .pdf
    pdf.output("okladka.pdf")
    messagebox.showinfo("showinfo", "Utworzono okładkę")
    window.destroy()



    
# New Cover Window
def NewCover():
    global Button
    global my_entry
    global my_entry2
    global my_barcode
    global window
    window = Toplevel()
    window.geometry('300x150')
    newCoverlabel = Label(window, text = "Stwórz nową okładkę")
    newCoverlabel.pack()
 
    my_entry = Entry(window, width = 50)
    my_entry.insert(0,'Head')
    my_entry.pack(padx = 5, pady = 5)   

    my_entry2 = Entry(window, width = 20)
    my_entry2.insert(0,'Body')
    my_entry2.pack(padx = 5, pady = 5)


    my_barcode = Entry(window, width = 20)
    my_barcode.insert(0,'5901234123457')
    my_barcode.pack(padx = 5, pady = 5)

    Button = Button(window, text = "Zapisz", command = coverPDF)
    Button.pack(padx = 5, pady = 5)
 
# FAQ windows
def faq():
    window = Toplevel()
    window.geometry('300x150')
    faqLabel = Label(window, text = "FAQ")
    faqText = Label(window, text = "Tutaj bedzie FAQ")
    faqText.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')
    faqLabel.pack()
    
    T = Text(window, height = 5, width = 52)

# Contact window   
def contact():
    window = Toplevel()
    window.geometry('300x150')
    contactLabel = Label(window, text = "Kontakt")
    contactText = Label(window, text = "p.borowiec@wobee.pl")
    contactText.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')
    contactLabel.pack()
    
    T = Text(window, height = 5, width = 52)
    
# Error window
def error():
    window = Toplevel()
    window.geometry('300x150')
    errorLabel = Label(window, text = "Zgłoś błąd")
    errorText = Label(window, text = "Zgłoś błąd na adres email: p.borowiec@wobee.pl")
    errorText.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')
    errorLabel.pack()
    
    T = Text(window, height = 5, width = 52)    
    

# Create an instance of tkinter frame or window
win = Tk()
frame = Frame(win)
frame.pack()
leftframe = Frame(win)
leftframe.pack(side=TOP, anchor=NW)

rightframe = Frame(win)
rightframe.pack(side=TOP, anchor=NW)


# Title
win.title('Scalator 1.0')


)

# Set the geometry of tkinter frame
win.geometry("700x350")

# Creating Menubar
menubar = Menu(win)

cover = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Okładka', menu = cover)
cover.add_command(label ='Generuj okładkę', command = NewCover)

cover.add_separator()
cover.add_command(label ='Koniec', command = win.destroy)


pdfMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Scalanie', menu = pdfMenu)
pdfMenu.add_command(label ='Scal pliki', command = None)

help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Pomoc', menu = help_)
help_.add_command(label ='FAQ', command = faq)
help_.add_command(label ='Kontakt', command = contact)
help_.add_separator()
help_.add_command(label ='Zgłość błąd', command = error)


# Merge PDF document into one
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
   file = fd.askopenfilenames(parent=win, title='Wybierz plik',filetypes=[('PDF Files', '*.pdf')])
   pdfs = win.splitlist(file)
   #print(file)
   output = 'combined_example.pdf'
   
   #lbl = Label(rightframe, text="Lokalizacja plików: " + str(pdfs))
   #lbl.pack(side = LEFT)
   #print(*pdfs, sep='\n')
   scrollbar = Scrollbar(win, orient="vertical")
   Lb1 = Listbox(win,width=100, height=10, yscrollcommand=scrollbar.set)
   
   Lb1.insert(END, *pdfs)
   Lb1.pack(side=LEFT)
   

   PDFmerge(pdfs=pdfs, output=output)


def open_cover():
    global coverPdf
    cover = fd.askopenfilenames(parent=win, title='Wybierz plik',filetypes=[('PDF Files', '*.pdf')])
    #cover = fd.askopenfile(mode='r', filetypes=[('PDF Files', '*.pdf')])
    coverPdf = win.splitlist(cover)
    #print(coverPdf)


    #scrollbar = Scrollbar(win, orient="vertical")
    #Lb1 = Listbox(win,width=100, height=1, yscrollcommand=scrollbar.set)
    #Lb1.insert(END, *coverPdf)
    #Lb1.pack()
    #filepath = os.path.abspath(cover.name)
    
    lbl = Label(leftframe, text=str(coverPdf))
    lbl.pack()

 





# Add a Button Widget

button1 = Button(leftframe, text="Zaznacz okładkę", command=open_cover)
button1.pack(padx = 3, pady = 3,side = LEFT)
button2 = Button(rightframe, text="Zaznacz wiele plików PDF", command=open_file)
button2.pack(padx = 3, pady = 3, side=LEFT)



#ttk.Button(win, text="Zaznacz okładkę", command=open_cover).pack()

#ttk.Button(win, text="Zaznacz wiele plików PDF", command=open_file).pack()


win.config(menu = menubar)
win.mainloop()








  
