from gc import disable
from operator import contains
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import font
import RBConfig as rbc
from TranscriptionResource import RBTranscriptor
import os
from os import listdir
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
        help_b.config(text='Help',image='',font=(0,21))
    else:
        # Bring the image back
        home_b.config(image=home,font=(0,21))
        imgclass_b.config(image=imageclassing,font=(0,21))
        audiotxt_b.config(image=audiotext,font=(0,21))
        datasearch_b.config(image=datasearch,font=(0,21))
        help_b.config(image=helpimage,font=(0,21))
def upload_image():
    upload_folder = "uploads/images"
    file = listdir(upload_folder+'/')[-1]
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
        messagebox.showinfo("Success!", f"File uploaded successfully!\n")
    except Exception as e:
        messagebox.showerror("Error!", f"Failed to upload file: {e}")
def upload_audio():
    upload_folder = "uploads/audio"
    file = listdir(upload_folder+'/')[-1]
    os.remove(f"uploads/audio/{file}")
    os.makedirs(upload_folder, exist_ok=True)
    file_path = filedialog.askopenfilename(
        title="Select an audio file",
        filetypes=[("Audio Files", "*.wav;*.flac;")]
    )

    if not file_path:
        return

    filename = os.path.basename(file_path)
    destination_path = os.path.join(upload_folder, filename)

    try:
        shutil.copy(file_path, destination_path)
        messagebox.showinfo("Success!", f"File uploaded successfully!\n")
    except Exception as e:
        messagebox.showerror("Error!", f"Failed to upload file: {e}")
def upload_sheet():
    upload_folder = "uploads/sheets"
    os.makedirs(upload_folder, exist_ok=True)
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not file_path:
        return

    filename = os.path.basename(file_path)
    destination_path = os.path.join(upload_folder, filename)

    try:
        shutil.copy(file_path, destination_path)
        messagebox.showinfo("Success!", f"File uploaded successfully!")
    except Exception as e:
        messagebox.showerror("Error!", f"Failed to upload file: {e}")
    


def page_handling(selection):
    def generate_imagedisplay(image):
        img = Label(imagepage, image=image, width=450, height=440)
        img.image = image
        img.place(x=50,y=300)
    def run_transcribe(): 
        if (len(listdir("uploads/audio/")) == 0):
            messagebox.showerror("File Read Error", "No audio file uploaded")
            return
        file = listdir("uploads/audio/")[-1]
        atbox.config(state='normal')
        atbox.delete('1.0', END)
        transcription = RBTranscriptor.transcribe(file)
        print(transcription)
        atbox.insert("end-1c", transcription)
        atbox.config(state='disabled')
    def run_classify():
        if (len(listdir("uploads/images/"))== 0):
            messagebox.showerror("File Read Error", "No image file uploaded")
            return
        file = listdir("uploads/images/")[-1]
        requestimage = PhotoImage(file,width=450,height=440)
        itbox.config(state='normal')
        itbox.delete('1.0', END)
        generate_imagedisplay(requestimage)
        imagetext = "" # connect result of image classification to this variable
        print(imagetext)
        itbox.insert('end-1c',imagetext)

    pages = ['homepage','audiopage','imagepage','datapage','helppage']
    for ch in root.children:
        if ch in pages:
            root.children.get(ch).destroy()
            break;
    if (selection == 'audio'):
        global atbox
        audiopage = Frame(root,name="audiopage",bg='lightsteelblue', width=(root.winfo_width()-frame.winfo_width()), height=root.winfo_height())
        aptitle = Label(audiopage, name='aptitle',bg='lightsteelblue',text="Audio Transcription", font=('Bauhaus 93',50))
        atbox = Text(audiopage,name='atbox', font=('Default','12'))
        upload = Button(audiopage, text='Upload Audio',relief='flat', command=upload_audio, width=40)
        go = Button(audiopage, text='Transcribe',relief='flat', command=run_transcribe)
        aptitle.place(x=280,y=100)
        audiopage.grid(row=0,column=1)
        upload.place(x=400,y=250)
        atbox.place(x=200,y=300)
        go.place(x=800,y=250)
        atbox.insert("end-1c", "Transcripted audio goes here")
        atbox.config(state='disabled')
        audiopage.grid_propagate(False)

    elif (selection == 'image'):
        imagepage = Frame(root,bg='palegreen3',name='imagepage', width=(root.winfo_width()-frame.winfo_width()), height=root.winfo_height())
        imtitle = Label(imagepage, name='imtitle',bg='palegreen3',text="Image Classification", font=('Bauhaus 93',50))
        upload = Button(imagepage, text='Upload Image',relief='flat', command=upload_image, width=40)
        itbox = Text(imagepage,name='itbox', font=('Default','12'),state='disabled', width=50)
        image = PhotoImage(file='Assets/testimage.png',width=450, height=440)
        go = Button(imagepage, text='Classify',relief='flat', command=run_classify)
        generate_imagedisplay(image)
        go.place(x=800,y=250)
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
        helppage.grid_propagate(False)
        helpfaqtitle = Label(helppage,bg='azure3',text='Additional Information', font=('Bauhaus 93', 50))
        helpside = Frame(helppage,bg='azure2', width=400, height=500)
        faqside = Frame(helppage,bg='azure2', width=400, height=500)
        helpside.grid_propagate(False)
        faqside.grid_propagate(False)
        helpfaqtitle.place(x=220,y=100)
        helpside.place(x=100,y=200)
        helptitle = Label(helpside,bg='azure2',text='Help', font=('Bauhaus 93', 30))
        faqtitle = Label(faqside,bg='azure2',text='FAQ', font=('Bauhaus 93', 30))
        contacttitle = Label(helpside,bg='azure2',text='Contact Us', font=('Bauhaus 93', 30))
        helptitle.place(x=150,y=20)
        faqtitle.place(x=150,y=20)
        contacttitle.place(x=100,y=220)
        contactinforyan = Label(helpside,bg='azure2',wraplength=350, text="Ryan M:        rmeeks@student.neumont.edu", font=('Default',14))
        contactinfologan = Label(helpside,bg='azure2',wraplength=350, text="Logan S: lostevens@student.neumont.edu", font=('Default',14))
        faqinfo = Label(faqside,bg='azure2',wraplength=350, text="Q: What is this app for?\nA: This app is designed to assist users with audio transcription, image classification and data searching.\n\nQ: How do I use the audio transcription feature?\nA: Click on the 'Audio Module' button in the sidebar, then click 'Upload Audio' to upload an audio file. Once uploaded, click 'Transcribe' to generate a transcript.\n\nQ: How do I use the image classification feature?\nA: Click on the 'Image Module' button in the sidebar, then click 'Upload Image' to upload an image file. The image will be displayed on the screen, and the classification will be displayed in the text box.\n\nQ: How do I use the data search feature?\nA: Click on the 'Data Module' button in the sidebar to access the data search feature. Enter your search query in the search box and click 'Search' to retrieve the results.", font=('Default','12'))
        helpinfo = Label(helpside,bg='azure2',wraplength=350, text="This app is designed to assist users with audio transcription, image classification and data searching. If you have any questions or need help, please refer to the FAQ section or contact us.", font=('Default','14'))
        faqside.place(x=650,y=200)
        helpinfo.place(x=25,y=80)
        faqinfo.place(x=25,y=80)
        contactinforyan.place(x=25,y=300)
        contactinfologan.place(x=25,y=380)

    else:
        homepage = Frame(root,bg='lightgray',name='homepage', width=(root.winfo_width()-frame.winfo_width()), height=root.winfo_height())
        hometitle = Label(homepage, name='hometitle',bg='lightgray',text=rbc.title, font=('Harlow Solid Italic',50))
        audioinfo = Frame(homepage,bg='steelblue4', width=300, height=400)
        audioinfo.grid_propagate(False)
        imageinfo = Frame(homepage,bg='steelblue4', width=300, height=400)
        imageinfo.grid_propagate(False)
        datainfo = Frame(homepage,bg='steelblue4', width=300, height=400)
        datainfo.grid_propagate(False)
        hyperaudio = Button(audioinfo,bg='sea green', text='Audio Transcription',relief='flat', width=23, font=('Bauhaus 93', 18), command=setAudio)
        hyperimage = Button(imageinfo,bg='sea green', text='Image Classification',relief='flat', width=23, font=('Bauhaus 93', 18), command=setImage)
        hyperdata = Button(datainfo,bg='sea green', text='Data Search',relief='flat', width=23, font=('Bauhaus 93', 18), command=setData)
        audiobrief = Label(audioinfo,bg='steelblue4', wraplength=250, text="'What did they say?' If you find yourself in need of a text form of recorded speech, this app offers a tool to to generate a transcript", font=('Default','14'))
        imagebrief = Label(imageinfo,bg='steelblue4', wraplength=250, text="Identify contents of an image", font=('Default','14'))
        databrief = Label(datainfo,bg='steelblue4', wraplength=250, text="AI assisted data searching", font=('Default','14'))
        hometitle.place(x=80,y=100)
        audioinfo.place(x=100,y=300)
        imageinfo.place(x=410,y=300)
        datainfo.place(x=720,y=300)
        hyperaudio.grid(row=0,column=0)
        hyperimage.grid(row=0,column=0)
        hyperdata.grid(row=0,column=0)
        audiobrief.place(x=25,y=60)
        imagebrief.place(x=25,y=60)
        databrief.place(x=25,y=60)

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
helpimage = PhotoImage(file='Assets/helpicon.png')

root.update()
frame = Frame(root,name='sidepanel',bg='red3',width=50,height=root.winfo_height())
frame.grid(row=0,column=0) 

menu_b = Button(frame, text='≡', bg='red2',relief='flat', font=(0,21), command=expand)
home_b = Button(frame,image=home,bg='red2',relief='flat', command=setHome)
imgclass_b = Button(frame,image=imageclassing,bg='red2',relief='flat', command=setImage)
audiotxt_b = Button(frame,image=audiotext,bg='red2',relief='flat', command=setAudio)
datasearch_b = Button(frame,image=datasearch,bg='red2',relief='flat', command=setData)
help_b = Button(frame,image=helpimage,bg='red2',relief='flat', command=setHelp)

menu_b.grid(row=0,column=0)
home_b.grid(row=1,column=0,pady=10)
imgclass_b.grid(row=2,column=0,pady=10)
audiotxt_b.grid(row=3,column=0, pady=10)
datasearch_b.grid(row=4,column=0, pady=10)
help_b.grid(row=5,column=0, pady=10)

# So that it does not depend on the widgets inside the frame
frame.grid_propagate(False)

def start():
    page_handling('home')
    root.mainloop()