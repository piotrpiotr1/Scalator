# Import the required libraries
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
import PyPDF2
from tkinter import messagebox

# Create an instance of tkinter frame or window
win = Tk()

# Set the geometry of tkinter frame
win.geometry("700x350")


# Set title menu bar

H1 = Label(win, text = "Scalator 0.1")
H2 = Label(win, text = "Oprogramowanie służy do scalania plików PDF."\
           "Naciśnij przycisk przytrzymując przycisk CTRL na klawiaturze dokonaj zaznaczenia. Program automatycznie wygeneruje plik i powiadomi o sukcesie.")

H1.config(font =("Arial", 14))
H2.config(font =("Arial", 8))

H1.pack()
# H2.pack()




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

win.mainloop()








  
