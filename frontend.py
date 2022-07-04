from tkinter import *
import backend
import re

def errormessage(error_field):
    '''Error fo'''
    error=Tk()
    error.wm_title("Error")
    error_lable = Label(error,text=f"Invalid {error_field}")
    error_lable.grid(row=1,column=0)
    error.mainloop()
    

def viewcommand():
    """
    It deletes all the items in the listbox, then inserts the rows returned by the view() function in
    the backend.py file.
    """
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
    
def searchcommand():
    """
    It deletes all the items in the listbox, then inserts the results of the search function into the
    listbox.
    """
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),Price_text.get()):
        list1.insert(END,row)

def add_command():
    """
    It takes the data from the entry boxes and passes it to the backend.insert function
    """
    if len(re.findall("\d{4}",year_text.get()))==0:
       errormessage("Year")
    elif len(re.findall("\d+", Price_text.get()))==0:
       errormessage("Price")
    elif len(re.findall("^[a-zA-Z0-9 ]*$", author_text.get()))==0:
       errormessage("Author")
    elif len(re.findall("^[a-zA-Z0-9 ]*$", title_text.get()))==0:
       errormessage("Title")
    
    
    else:
        backend.insert(title_text.get(),author_text.get(),year_text.get(),Price_text.get())
        list1.delete(0,END)
        list1.insert(END,"Press View all to see the new entry")
    
   
def get_selected_row(event):
    """
    It gets the selected row from the listbox and inserts the values into the entry boxes

    :param event: The event is a tkinter event
    """
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple=list1.get(index)
        
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])

        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])

        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])

        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
    

def delete_command():
    """
    It deletes the selected tuple from the database
    """
    try:
        backend.delete(selected_tuple[0])
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        viewcommand()
    except NameError:
        errormessage("(No field selected)")
        

def update_command():
    try:
        backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),Price_text.get())
        viewcommand()
    except NameError:
        errormessage("(No field selected)")
    


window=Tk()


window.wm_title("Bookstore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="Price")
l4.grid(row=1,column=2)


title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)


author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)


year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)


Price_text=StringVar()
e4=Entry(window,textvariable=Price_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6,)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


list1.bind('<<ListboxSelect>>',get_selected_row)



b1=Button(window,text="View all",width=12,command=viewcommand)
b1.grid(row=2,column=3)


b2=Button(window,text="Search Entry",width=12,command=searchcommand)
b2.grid(row=3,column=3)


b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)


b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)


b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)


b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()