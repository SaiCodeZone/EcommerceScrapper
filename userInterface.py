from tkinter import *
import tkinter.font as tkFont
import scraper


def startScrapingAgent():
    keyword=value.get()
    filename=NameOfTheFile.get()
    scraper.startScraping(keyword,filename)


parent=Tk()
parent.geometry("500x400")
parent.title("Scraping agent for ecommerce websites")
parent.configure(background="#404040")

#icon=PhotoImage(file='C:\Python37\Scripts\project\scraper.png')
#parent.iconphoto(False, icon)



#Heading for the window
Heading=Label(parent, text="Scrapes data from flipkart and snapdeal",height=4,font="Calibri 20 normal",bg="#404040",fg="floral white")
Heading.config(anchor=CENTER)
Heading.pack()

#Remaining labels for window
Label(parent, text="Enter a Keyword to search and scrape",font="Calibri 11 normal",bg="#404040",fg="floral white").place(x=30,y=130)
Label(parent,text="Enter a file name to store data(csv file)",font="Calibri 11 normal",bg="#404040",fg="floral white").place(x=30,y=180)

#text field
value=StringVar()
NameOfTheFile=StringVar()

Entry(parent,text=value,width=30,highlightthickness=1,highlightcolor="blue").place(x=270,y=130)
Entry(parent,text=NameOfTheFile,width=30,highlightthickness=1,highlightcolor="blue").place(x=274,y=180)

#submit button
Button(parent,text="Scrape",command=startScrapingAgent,bg="floral white",activebackground="blue").place(x=230,y=230)

#mainloop
parent.mainloop()
