from tkinter import *
import RBConfig as rbc

root = Tk()
root.title(rbc.title)
root.geometry(f"{rbc.screenWidth}x{rbc.screenHeight}")

# Side panel following https://stackoverflow.com/a/66859503
def expand():
    rbc.cur_width = rbc.max_frame_w
    frame.config(width=rbc.cur_width) # Change the width to new increase width
    if rbc.cur_width >= rbc.max_frame_w: # If width is greater than maximum width 
        rbc.expanded = True # Frame is expended
        fill()

def contract():
    rbc.cur_width = rbc.min_frame_w
    frame.config(width=rbc.cur_width) # Change the width to new reduced width
    if rbc.cur_width <= rbc.min_frame_w: # If it is back to normal width
        rbc.expanded = False # Frame is not expanded
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

bigTitle = Label(root, text=rbc.title)
bigTitle.place(anchor='center',relx=0.6,rely=0.05)



home = PhotoImage(file='Assets/home.png')
imageclassing = PhotoImage(file='Assets/imgup.png')
audiotext = PhotoImage(file='Assets/microphone-icon.png')
datasearch = PhotoImage(file='Assets/dbase.png')

root.update()
frame = Frame(root,bg='red3',width=50,height=root.winfo_height())
frame.grid(row=0,column=0) 

menu_b = Button(frame, text='≡', bg='red2',relief='flat', command=expand)
home_b = Button(frame,image=home,bg='red2',relief='flat')
imgclass_b = Button(frame,image=imageclassing,bg='red2',relief='flat')
audiotxt_b = Button(frame,image=audiotext,bg='red2',relief='flat')
datasearch_b = Button(frame,image=datasearch,bg='red2',relief='flat')

menu_b.grid(row=0,column=0)
home_b.grid(row=1,column=0,pady=10)
imgclass_b.grid(row=2,column=0,pady=50)
audiotxt_b.grid(row=3,column=0)

# So that it does not depend on the widgets inside the frame
frame.grid_propagate(False)

def start():
    root.mainloop()