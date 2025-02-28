from gc import disable
from tkinter import *
from tkinter import filedialog, messagebox
import RBConfig as rbc
import os
import shutil


root = Tk()
root.title(rbc.title)
root.resizable(0,0)
root.wm_attributes('-transparentcolor','gray26')
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
def upload_image():
    upload_folder = "uploadedimages"
    os.makedirs(upload_folder, exist_ok=True)
    file_path = filedialog.askopenfilename(
        title="Select a media file",
        filetypes=[("Media Files", "*.png;*.jpg;*.jpeg;")]
    )

    if not file_path:
        return

    filename = os.path.basename(file_path)
    destination_path = os.path.join(upload_folder, filename)

    try:
        shutil.copy(file_path, destination_path)
        messagebox.showinfo("Success!", f"File uploaded successfully!\nSaved at: {destination_path}")
    except Exception as e:
        messagebox.showerror("Error!", f"Failed to upload file: {e}")
def upload_audio():
    upload_folder = "uploadedaudio"
    os.makedirs(upload_folder, exist_ok=True)
    file_path = filedialog.askopenfilename(
        title="Select an audio file",
        filetypes=[("Audio Files", "*.wav;*.mp3;")]
    )

    if not file_path:
        return

    filename = os.path.basename(file_path)
    destination_path = os.path.join(upload_folder, filename)

    try:
        shutil.copy(file_path, destination_path)
        messagebox.showinfo("Success!", f"File uploaded successfully!\nSaved at: {destination_path}")
    except Exception as e:
        messagebox.showerror("Error!", f"Failed to upload file: {e}")

def page_handling(selection):
    pages = ['homepage','audiopage','imagepage','datapage','helppage']
    for ch in root.children:
        if ch in pages:
            root.children.get(ch).destroy()
            break;
    if (selection == 'audio'):
        audiopage = Frame(root,name="audiopage",bg='lightsteelblue', width=(root.winfo_width()-frame.winfo_width()), height=root.winfo_height())
        aptitle = Label(audiopage, name='aptitle',bg='lightsteelblue',text="Audio Transcription", font=('Bauhaus 93',50))
        atbox = Text(audiopage,name='atbox', font=('Default','12'))
        upload = Button(audiopage, text='Upload Audio',relief='flat', command=upload_audio, width=40)
        aptitle.place(x=280,y=100)
        audiopage.grid(row=0,column=1)
        upload.place(x=400,y=250)
        atbox.place(x=200,y=300)
        atbox.insert("end-1c",'text')
        atbox.config(state='disabled')
        audiopage.grid_propagate(False)

    elif (selection == 'image'):
        imagepage = Frame(root,bg='palegreen3',name='imagepage', width=(root.winfo_width()-frame.winfo_width()), height=root.winfo_height())
        imtitle = Label(imagepage, name='imtitle',bg='palegreen3',text="Image Classification", font=('Bauhaus 93',50))
        upload = Button(imagepage, text='Upload Image',relief='flat', command=upload_image, width=40)
        itbox = Text(imagepage,name='itbox', font=('Default','12'),state='disabled', width=50)
        image = PhotoImage(file='Assets/testimage.png')
        img = Label(imagepage, image=image, width=450, height=400)
        img.place(x=50,y=300)
        itbox.place(x=550,y=300)
        imtitle.place(x=280,y=100)
        upload.place(x=400,y=250)

        imagepage.grid(row=0,column=1)
        imagepage.grid_propagate(False)

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
    page_handling('home')
    root.mainloop()