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
from barcode import *
from barcode.writer import ImageWriter
import os
from datetime import datetime


now = datetime.now()
date_time = now.strftime("%m/%d/%Y")
# Generate new cover PDF
def coverPDF():
    
    pdf = FPDF()
    barType = barcodeType.get()
    vFont = vFontTitle.get()
   
    number = my_barcode.get()
    pdf.add_page()
    pdf.set_font(vFont, size = 15)
          
        # create a cell
    pdf.cell(200, 10, txt = str(my_entry.get()), 
                 ln = 1, align = 'C')

    pdf.cell(200, 10, txt = str(my_entry2.get()), 
                 ln = 2, align = 'C')
    
    if barType == 'EAN113':

        my_code = EAN13(number, writer=ImageWriter())


        my_code.save("new_code1")

    elif barType == 'EAN8':


        my_code = EAN8(number, writer=ImageWriter())


        my_code.save("new_code1")
        # Our barcode is ready. Let's save it.
        

          
    pdf.image("new_code1.png", x = None, y = None, w = 0, h = 0, type = '', link = '')
        
        # save the pdf with name .pdf
    pdf.output("okladka.pdf")
    messagebox.showinfo("showinfo", "Utworzono okładkę")
    #window.destroy()



    
# New Cover Window
def NewCover():
    global Button2
    global my_entry
    global my_entry2
    global my_barcode
    global window
    global barcodeType
    global vFontTitle
   # global vFontSubTitle

        
    window = Toplevel()
    window.geometry('600x300')
    #newCoverlabel = Label(window, text = "Stwórz nową okładkę")
    #newCoverlabel.pack()
    
    
    #my_entry = Entry(leftframe, width = 50)
    #my_entry.insert(0,'')
    #label_my_entry = Label(leftframe, text = "Nagłówek")
    #label_my_entry.pack()
    #my_entry.pack(padx = 5, pady = 5)   
    
    frame1 = Frame(window, padx=5, pady=5)
    frame1.grid(row=0, column=1)

    Label(frame1, text='Tytuł', padx=5, pady=5).pack()
    Label(frame1, text='Podtytuł', padx=5, pady=5).pack()
    Label(frame1, text='Kod kreskowy', padx=5, pady=5).pack()
 

    frame2 = Frame(window, padx=5, pady=5)
    frame2.grid(row=0, column=2)

    my_entry = Entry(frame2,width = 50)
    my_entry.insert(0,'')
    my_entry.pack(padx = 5, pady = 5)


    my_entry2 = Entry(frame2,width = 50)
    my_entry2.insert(0,'')
    my_entry2.pack(padx = 5, pady = 5)


    my_barcode = Entry(frame2,width = 50)
    my_barcode.insert(0,'')
    my_barcode.pack(padx = 5, pady = 5)


    frame3 = Frame(window, padx=5, pady=5)
    frame3.grid(row=0, column=3)

    
    vFontTitle = ["Arial","Courier","Helvetica","Times"]
    vFontTitle = ttk.Combobox(frame3, values = vFontTitle)
    vFontTitle.set("Wybierz czcionkę")
    vFontTitle.pack(padx = 5, pady = 5)

    vbarcode = ["EAN13", "EAN8"]
    barcodeType = ttk.Combobox(frame3, values = vbarcode)
    barcodeType.set("Wybierz format kodu kreskowego")
    barcodeType.pack(padx = 5, pady = 5)

    frame3 = Frame(window, padx=5, pady=5)
    frame3.grid(row=1, column=1)
    Button2 = Button(frame3, text = "Zapisz", command= coverPDF)
    Button2.pack(padx = 5, pady = 5)

"""

    
     ssnn
    Button2 = Button(window, text = "Zapisz", command= coverPDF)
    Button2.pack(padx = 5, pady = 5)

    
    barcodeType = StringVar()
 
    RBttn = Radiobutton(window, text = "EAN13", variable = barcodeType,
                    value = "EAN13",tristatevalue=0)
    RBttn.pack(padx = 5, pady = 5)
 
    RBttn2 = Radiobutton(window, text = "EAN8", variable = barcodeType,
                     value = "EAN8",tristatevalue=0)
    RBttn2.pack(padx = 5, pady = 5)
    
    

    
    """
 
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

left2frame = Frame(win)
left2frame.pack(side=TOP, anchor=SW)


bottomframe = Frame(win)
bottomframe.pack(side=BOTTOM, anchor=SW)

# Title
win.title('Scalator 1.0')




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
def PDFmerge():
    MsgBox = tk.messagebox.askquestion ('Scalanie','Czy jesteś pewien aby rozpocząć scalanie plików? Proces może zająć parę chwil w zależności od wielkości plików oraz pamięci RAM komputera',icon = 'warning')
    if MsgBox == 'yes':
       # creating pdf file merger object
        pdfMerger = PyPDF2.PdfFileMerger()

        # appending pdfs one by one
        for pdf in pdfs:
            pdfMerger.append(pdf)

    
        

    # writing combined pdf to output pdf file
        with open(os.path.join(folder_selected,output), 'wb') as f:
            pdfMerger.write(f)
        
            messagebox.showinfo("showinfo", "Scalanie plików zakończone sukcesem! Nazwa pliku "+output)
    
            
    

def deletePDF():
   #Lb1.delete(0,END)
   Lb1.delete(ANCHOR)
   
def deleteCover():
   lbl.after(100, lbl.destroy())
   


    

def open_file():
   global Lb1
   global pdfs
   global output
   file = fd.askopenfilenames(parent=win, title='Wybierz plik',filetypes=[('PDF Files', '*.pdf')])
   pdfs = win.splitlist(file)
   
   output = 'combined_example.pdf'
   
  

   #scrollbar = Scrollbar(win, orient="vertical")
  # Lb1 = Listbox(win,width=100, height=10, yscrollcommand=scrollbar.set)
   #ttk.Button(win, text="Delete", command=delete).pack()
   Lb1.insert(END, *pdfs)
   
  # Lb1.pack(side=LEFT)
   

   #PDFmerge(pdfs=pdfs, output=output)


def open_cover():
    global coverPdf
    global lbl
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

 
def pdfLocation():
    
    global folder_selected
    folder_selected = fd.askdirectory()
    lbl = Label(left2frame, text=str(folder_selected))
    lbl.pack()
    



# Add a Button Widget

button1 = Button(leftframe, text="Zaznacz okładkę", command=open_cover)
button1.pack(padx = 3, pady = 3,side = LEFT)
button2 = Button(rightframe, text="Zaznacz wiele plików PDF", command=open_file)
button2.pack(padx = 3, pady = 3, side=LEFT)
button3 = Button(rightframe, text="Usuń PDF", command=deletePDF)
button3.pack(padx = 3, pady = 3, side=LEFT)
button4 = Button(leftframe, text="Usuń okładkę", command=deleteCover)
button4.pack(padx = 3, pady = 3,side = LEFT)
button5 = Button(bottomframe, text="Scalaj", command=PDFmerge)
button5.pack(padx = 3, pady = 3)
button6 = Button(left2frame, text="Lokalizacja pliku wynikowego", command=pdfLocation)
button6.pack(padx = 3, pady = 3,side=LEFT)


#entry1 = tk.Entry(win) .pack()

scrollbar = Scrollbar(win, orient="vertical")
Lb1 = Listbox(win,width=100, height=10, yscrollcommand=scrollbar.set,selectmode=SINGLE)

   
Lb1.pack(side=LEFT)







#ttk.Button(win, text="Zaznacz okładkę", command=open_cover).pack()

#ttk.Button(win, text="Zaznacz wiele plików PDF", command=open_file).pack()


win.config(menu = menubar)
win.mainloop()








  
