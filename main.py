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
from PyPDF2 import PdfFileWriter, PdfFileReader
import pycpdflib
import sys
sys.path.insert(0,'..')


if  sys.platform.startswith('win64'):
    
    pycpdflib.loadDLL("libpycpdf.dll")


datename = datetime.now().strftime("%Y_%m_%d-%H_%M_%S ")


# Generate new cover PDF


class PDF(FPDF):
    def header(self):
        # Logo
        
        self.image(fileImage, 80, 30, 33)


        
        vFont = vFontTitle.get()
        sizeTitlea= sizeTitle.get()
        
        # Arial bold 15
        self.set_font(vFont, 'B', int(sizeTitlea))
        # Move to the right
        #self.cell(50,10)
        self.set_xy(50, 70)
        # Title
        #self.cell(30, 10, str(my_entry.get()), 1, 0, 'C')

        self.multi_cell(120,20, str(my_entry.get()),0,'C')
        
        # Line break
        self.ln(20)

    
        

   
  




    # Page footer
    #def footer(self):
        # Position at 1.5 cm from bottom
     #   self.set_y(-15)
        # Arial italic 8
      #  self.set_font('Arial', 'I', 8)
        # Page number
       # self.cell(0, 10, 'Stro ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
def coverPDF():

    try:
        val = int(sizeSubTitle.get())
        val = int(sizeTitle.get())
    except ValueError:
        messagebox.showerror("showerror",'Wprowadź poprawne dane')
        raise
        
    
   
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    barType = barcodeType.get()
    number = my_barcode.get()
    
    sizeSubTitlea = sizeSubTitle.get()
    vFontSub = vFontSubTitle.get()
    pdf.set_font(vFontSub, '', int(sizeSubTitlea))
    pdf.set_xy(50, 150)
    pdf.multi_cell(120,20, str(my_entry2.get()),0,'C')

    if barType == 'EAN113':

        my_code = EAN13(number, writer=ImageWriter())


        my_code.save("new_code1")

    elif barType == 'EAN8':


        my_code = EAN8(number, writer=ImageWriter())


        my_code.save("new_code1")
        # Our barcode is ready. Let's save it.
        

          
    pdf.image("new_code1.png", x = 50, y = 210,  h = 50, type = '', link = '')

    
    pdf.output('okladka.pdf', 'F')
    messagebox.showinfo("showinfo", "Utworzono okładkę")


"""
def coverPDF():
    
    pdf = FPDF()
    
    vFont = vFontTitle.get()
   
    
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

"""

def imagesCover():
    global fileImage
    fileImage = fd.askopenfilename(parent=win, title='Wybierz plik',filetypes=[('image files', ('.png', '.jpg')),])
    #imageFileurl.instert(0,file)
    imageFileurl.delete(0,END)
    imageFileurl.insert(0,fileImage)

    
# New Cover Window
def NewCover():
    global Button2
    global my_entry
    global my_entry2
    global my_barcode
    global window
    global barcodeType
    global vFontTitle
    global vFontSubTitle
    global sizeTitle
    global sizeSubTitle
    global frame2
    global imageFileurl
        
    window = Toplevel()
    window.geometry('900x300')
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
    Label(frame1, text='Logotyp', padx=5, pady=5).pack()
 

    frame2 = Frame(window, padx=5, pady=5)
    frame2.grid(row=0, column=2)

    my_entry = Entry(frame2,width = 50)
    my_entry.insert(0,'STAROSTWO POWIATOWE W CIESZYNIE')
    my_entry.pack(padx = 5, pady = 5)
    


    my_entry2 = Entry(frame2,width = 50)
    my_entry2.insert(0,'OPERAT SZACUNKOWY')
    my_entry2.pack(padx = 5, pady = 5)


    my_barcode = Entry(frame2,width = 50)
    my_barcode.insert(0,'')
    my_barcode.pack(padx = 5, pady = 5)


    
    frame3 = Frame(window, padx=5, pady=5)
    frame3.grid(row=0, column=4)
    
        

    sizeTitle = Entry(frame3,width = 5)
    sizeTitle.insert(0,'35')
    sizeTitle.pack(padx = 5, pady = 5)
    
    sizeSubTitle = Entry(frame3,width = 5)
    sizeSubTitle.insert(0,'12')
    sizeSubTitle.pack(padx = 5, pady = 5)


    Label(frame3, text='', padx=5, pady=5).pack()
    Label(frame3, text='', padx=5, pady=5).pack()


    frame4 = Frame(window, padx=5, pady=5)
    frame4.grid(row=0, column=5)

    
    vFontTitle = ["Arial","Courier","Helvetica","Times"]
    vFontTitle = ttk.Combobox(frame4, values = vFontTitle)
    vFontTitle.set("Wybierz czcionkę")
    vFontTitle.pack(padx = 5, pady = 5)

    vFontSubTitle = ["Arial","Courier","Helvetica","Times"]
    vFontSubTitle = ttk.Combobox(frame4, values = vFontSubTitle)
    vFontSubTitle.set("Wybierz czcionkę")
    vFontSubTitle.pack(padx = 5, pady = 5)

    vbarcode = ["EAN13", "EAN8"]
    barcodeType = ttk.Combobox(frame4, values = vbarcode)
    barcodeType.set("Wybierz format kodu kreskowego")
    barcodeType.pack(padx = 5, pady = 5)

    Label(frame4, text='', padx=5, pady=5).pack()

    frame3 = Frame(window, padx=5, pady=5)
    frame3.grid(row=1, column=1)

    frame5 = Frame(window, padx=5, pady=5)
    frame5.grid(row=0, column=3)

    Label(frame5, text='Czcionka wielkość', padx=5, pady=5).pack()
    Label(frame5, text='Czcionka wielkość', padx=5, pady=5).pack()
    Label(frame5, text='', padx=5, pady=5).pack()
    Label(frame5, text='', padx=5, pady=5).pack()
     
    
    
    Button2 = Button(frame3, text = "Generują okładkę", command= coverPDF)
    Button2.pack(padx = 5, pady = 5)


    Button3 = Button(frame2, text = "Wybierz", command= imagesCover)
    Button3.pack(padx = 5, pady = 5,side =LEFT)


    imageFileurl = Entry(frame2,width = 40)
    
    imageFileurl.pack(padx = 5, pady = 5)
    

"""

    
     
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
style = ttk.Style()
win.tk.call("source", "azure.tcl")
win.tk.call("set_theme", "light")
win.geometry("700x350")



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
    try: folder_selected      
    except NameError: messagebox.showerror("showerror",'Nie wybrałeś folderu docelowego')
    else:


        pdf = PDF()
        
        MsgBox = tk.messagebox.askquestion ('Scalanie','Czy jesteś pewien aby rozpocząć scalanie plików? Proces może zająć parę chwil w zależności od wielkości plików oraz pamięci RAM komputera',icon = 'warning')
        if MsgBox == 'yes':
           # creating pdf file merger object
            
            pdfMerger = PyPDF2.PdfFileMerger(strict=True)
            #pdfWriter = PyPDF2.PdfFileWriter()
            
            #pdf.set_compression(True)
            
            # appending pdfs one by one
            for pdf in pdfs:
                pdfMerger.append(pdf)
            
            
            

         #writing combined pdf to output pdf file
            with open(os.path.join(folder_selected,output), 'wb') as f:
                pdfMerger.write(f)
                
                messagebox.showinfo("showinfo", "Scalanie plików zakończone sukcesem! Nazwa pliku "+output)
             
                
                f.close()
                
                fromFile(output=output)
def fromFile(output):


    
    pdf = pycpdflib.fromFile('../1.pdf','')
    #pycpdflib.compress(pdf)
    #pycpdflib.toFileExt(pdf, 'compress.pdf', False, False, True, True, True)


        
     
 

def deletePDF():
   #Lb1.delete(0,END)
   Lb1.delete(ANCHOR)
   
def deleteCover():
   #coverPDFurl.after(100, coverPDFurl.destroy())
   coverPDFurl.delete(0,END)
   


    

def open_file():
   global Lb1
   global pdfsInsert
   global pdfs
   global output


   file = fd.askopenfilenames(parent=win, title='Wybierz plik',filetypes=[('PDF Files', '*.pdf'),])
   


  

   pdfsInsert = win.splitlist(file)

   try: coverTuple
   except NameError: pdfs = pdfsInsert
       
   else:
       pdfs = coverTuple+pdfsInsert
   
   #output =  datename+' Eksport.pdf'
   output =  'Eksport.pdf'
   
  

   #scrollbar = Scrollbar(win, orient="vertical")
  # Lb1 = Listbox(win,width=100, height=10, yscrollcommand=scrollbar.set)
   #ttk.Button(win, text="Delete", command=delete).pack()

   Lb1.insert(END, *pdfsInsert)
       
  # Lb1.pack(side=LEFT)
   

   #PDFmerge(pdfs=pdfs, output=output)


def open_cover():

    global coverTuple
    global cover
    global lbl
   
    cover = fd.askopenfilename(parent=win, title='Wybierz plik',filetypes=[('PDF Files', '*.pdf')])
    #cover = fd.askopenfile(mode='r', filetypes=[('PDF Files', '*.pdf')])
    #coverPdf = win.splitlist(cover)
    #print(cover)
    #print(coverPdf)
    coverTuple = tuple(map(str, cover.split(', ')))
    
    
    
    #scrollbar = Scrollbar(win, orient="vertical")
    #Lb1 = Listbox(win,width=100, height=1, yscrollcommand=scrollbar.set)
    #Lb1.insert(END, *coverPdf)
    #Lb1.pack()
    #filepath = os.path.abspath(cover.name)
    coverPDFurl.delete(0,END)
    coverPDFurl.insert(0,cover)
    #Lb2.insert(0, cover)
    

    #lbl = Label(leftframe, text=str(cover))
    
    
    #my_entry.insert(0,'STAROSTWO POWIATOWE W CIESZYNIE')
    #my_entry.pack(padx = 5, pady = 5)
  

 
def pdfLocation():
    
    global folder_selected
    folder_selected = fd.askdirectory()
    #lbl = Label(left2frame, text=str(folder_selected))
    pdfLocationurl.delete(0,END)
    pdfLocationurl.insert(0,str(folder_selected))
    
    #lbl.pack()
    



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





coverPDFurl = Entry(leftframe,width = 80)
coverPDFurl.pack(padx = 5, pady = 5)



pdfLocationurl = Entry(left2frame,width = 50)
pdfLocationurl.pack(padx = 5, pady = 5)


#entry1 = tk.Entry(win) .pack()


#Lb2 = Listbox(win,width=10, height=10,yscrollcommand=scrollbar.set,selectmode=SINGLE)

   

#Lb2.pack(side=RIGHT)






#ttk.Button(win, text="Zaznacz okładkę", command=open_cover).pack()

#ttk.Button(win, text="Zaznacz wiele plików PDF", command=open_file).pack()


win.config(menu = menubar)
win.mainloop()








  
