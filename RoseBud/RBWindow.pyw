from tkinter import *
from tkinter import filedialog, messagebox
import RBConfig as rbc
import os
import shutil

#Setup for upload folder
upload_folder = "uploads"
os.makedirs(upload_folder, exist_ok=True)


root = Tk()
root.title(rbc.title)
root.geometry(f"{rbc.screenWidth}x{rbc.screenHeight}")


# Side panel following https://stackoverflow.com/a/66859503
def expand():
    rbc.cur_width += 10 # Increase the width by 10
    rep = root.after(5,expand)
    frame.config(width=rbc.cur_width) # Change the width to new increase width
    if rbc.cur_width >= rbc.max_frame_w: # If width is greater than maximum width 
        rbc.expanded = True # Frame is expended
        root.after_cancel(rep)
        menu_b.config(command=contract, text="X", anchor="w")
        fill()

def contract():
    rbc.cur_width -= 10 # Reduce the width by 10 
    rep = root.after(5,contract) # Call this func every 5 ms
    frame.config(width=rbc.cur_width) # Change the width to new reduced width
    if rbc.cur_width <= rbc.min_frame_w: # If it is back to normal width
        rbc.expanded = False # Frame is not expanded
        root.after_cancel(rep) # Stop repeating the func
        menu_b.config(command=expand,  text='≡', anchor="center")
        fill()

def fill():
    if rbc.expanded: # If the frame is exanded
        # Show a text, and remove the image
        hbwidth = home_b.winfo_width();
        ibwidth = imgclass_b.winfo_width;
        abwidth = audiotxt_b.winfo_width;
        dbwidth = datasearch_b.winfo_width;
        home_b.config(text='Home',image='',font=(0,21),padx=hbwidth)
        imgclass_b.config(text='Image Module',image='',font=(0,21))
        audiotxt_b.config(text='Audio Module',image='',font=(0,21))
        datasearch_b.config(text='Data Module',image='',font=(0,21))
    else:
        # Bring the image back
        home_b.config(image=home,font=(0,21))
        imgclass_b.config(image=imageclassing,font=(0,21))
        audiotxt_b.config(image=audiotext,font=(0,21))
        datasearch_b.config(image=datasearch,font=(0,21))


def page_handling(selection):
    pages = ['homepage','audiopage','imagepage','datapage','helppage']
    for ch in root.children:
        if ch in pages:
            root.children.get(ch).destroy()
            break;
    if (selection == 'audio'):
        audiopage = Frame(root,name="audiopage",bg='lightsteelblue', width=(root.winfo_width()-frame.winfo_width()), height=root.winfo_height())
        upload = Button(audiopage, text='Upload File',relief='flat')
        audiopage.grid(row=0,column=1)

    elif (selection == 'image'):
        imagepage = Frame(root,bg='palegreen3',name='imagepage', width=(root.winfo_width()-frame.winfo_width()), height=root.winfo_height())
        imagepage.grid(row=0,column=1)

    elif (selection == 'data'):
        datapage = Frame(root,bg='pink1',name='datapage', width=(root.winfo_width()-frame.winfo_width()), height=root.winfo_height())
        datapage.grid(row=0,column=1)

    elif (selection == 'help'):
        helppage = Frame(root,bg='azure3',name='helppage', width=(root.winfo_width()-frame.winfo_width()), height=root.winfo_height())
        helppage.grid(row=0,column=1)

    else:
        homepage = Frame(root,bg='lightgray',name='homepage', width=(root.winfo_width()-frame.winfo_width()), height=root.winfo_height())
        homepage.grid(row=0,column=1)


def setHome():
    page_handling('home')
def setAudio():
    page_handling('audio')
def setImage():
    page_handling('image')
def setData():
    page_handling('data')
def setHelp():
    page_handling('help')

bigTitle = Label(root, text=rbc.title)
bigTitle.place(anchor='center',relx=0.6,rely=0.05)



home = PhotoImage(file='Assets/home.png')
imageclassing = PhotoImage(file='Assets/imgup.png')
audiotext = PhotoImage(file='Assets/microphone-icon.png')
datasearch = PhotoImage(file='Assets/dbase.png')

root.update()
frame = Frame(root,name='sidepanel',bg='red3',width=50,height=root.winfo_height())
frame.grid(row=0,column=0) 

menu_b = Button(frame, text='≡', bg='red2',relief='flat', font=(0,21), command=expand)
home_b = Button(frame,image=home,bg='red2',relief='flat', command=setHome)
imgclass_b = Button(frame,image=imageclassing,bg='red2',relief='flat', command=setImage)
audiotxt_b = Button(frame,image=audiotext,bg='red2',relief='flat', command=setAudio)
datasearch_b = Button(frame,image=datasearch,bg='red2',relief='flat', command=setData)

menu_b.grid(row=0,column=0)
home_b.grid(row=1,column=0,pady=10)
imgclass_b.grid(row=2,column=0,pady=10)
audiotxt_b.grid(row=3,column=0, pady=10)
datasearch_b.grid(row=4,column=0, pady=10)

# So that it does not depend on the widgets inside the frame
frame.grid_propagate(False)

def start():
    root.mainloop()