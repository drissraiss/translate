from tkinter import *
import messagebox
from textblob import TextBlob
from tkinter import filedialog


def translate():
    file = input1.get()
    folder = input2.get()
    formLang = input3.get()
    toLang = input4.get()
    if len(file) == 0 or len(folder) == 0 or len(formLang) == 0 or len(toLang) == 0:
        return messagebox.showwarning('DRS-Translate', 'Please fill in the fields')

    with open(file, 'rt', encoding='utf-8') as f1:
        oreginal = f1.read()

    translateText = TextBlob(oreginal).translate(from_lang=formLang, to=toLang)

    with open(folder + '/NewText.txt', 'wt', encoding='utf-8') as f2:
        f2.write(str(translateText))

    messagebox.showinfo('DRS-Translate', 'Translate sucsefull')


def selectfile():
    file = filedialog.askopenfilename()
    input1.set(file)
    


def selectfolder():
    folder = filedialog.askdirectory()
    input2.set(folder)


appTranslate = Tk()
appTranslate.title('DRS-Translate')
appTranslate.geometry('810x400+480+230')


styleLabel = ('Verdana', 20, 'bold')
styleInput = ('ariel', 15, 'italic')
styleButton = (10)
Label(text='Original text : ', font=styleLabel).grid(
    row=0, column=0, padx=10, pady=20)
Label(text='Translation  : ', font=styleLabel).grid(
    row=1, column=0, padx=10, pady=20)
Label(text='Language : ', font=styleLabel).grid(
    row=2, column=0, padx=10, pady=20)
Label(text='From : ', font=('verdana', 16)).grid(row=2, column=1)
Label(text='To : ', font=('verdana', 16)).grid(row=2, column=3)

input1 = StringVar()
input2 = StringVar()
input3 = StringVar()
input4 = StringVar()


locationOriginalText = Entry(
    textvariable=input1, width=40, font=styleInput, state='disabled', cursor='arrow',)
locationOriginalText.grid(row=0, column=1, columnspan=4)
locationNewText = Entry(textvariable=input2, width=40,
                        font=styleInput, state='disabled', cursor='arrow')
locationNewText.grid(row=1, column=1, columnspan=4)

langFrom = Entry(textvariable=input3, font=styleInput, width=2)
langFrom.grid(row=2, column=2)
langTo = Entry(textvariable=input4, font=styleInput, width=2)
langTo.grid(row=2, column=4)


Button(text='Select file', width=10, font=styleButton,
       relief=GROOVE,
       cursor='hand2',
       command=selectfile).grid(row=0, column=5, padx=10, pady=10)
Button(text='Select folder', width=10, font=styleButton,
       relief=GROOVE,
       cursor='hand2',
       command=selectfolder).grid(row=1, column=5, padx=10, pady=10)
Button(text='Translate', font=('verdana', 30), highlightthickness=5,
       fg='#fff',
       bg='#025fff',
       activebackground='#0275d8',
       activeforeground='#fff',
       cursor='hand2',
       command=translate
       ).grid(columnspan=6, padx=20, pady=30)


appTranslate.mainloop()
