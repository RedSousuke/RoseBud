import RBWindow

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

RBWindow.start()