from tkinter import *
from tkinter import filedialog, messagebox
import RBConfig as rbc
import os
import shutil

#Setup for upload folder
upload_folder = "uploads"
os.makedirs(upload_folder, exist_ok=True)

#Upload File Function
def upload_file():
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

root = Tk()
root.title(rbc.title)
root.geometry(f"{rbc.screenWidth}x{rbc.screenHeight}")
w = Label(root, text="Welcome To RoseBud!", font={'Times', 24})
w.pack()

# Upload button
upload_button = Button(root, text="Upload Media File", command=upload_file)
upload_button.pack(pady=20)



def start():
    root.mainloop()