import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

def load_image():
    global img, img_display, img_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img_path = file_path
        img = Image.open(img_path)
        img_display = ImageTk.PhotoImage(img.resize((250, 250)))
        image_label.config(image=img_display)
        status_label.config(text=f"Loaded: {os.path.basename(file_path)}")

def encrypt_image():
    if img_path is None:
        messagebox.showwarning("No Image", "Please load an image first.")
        return

    image = Image.open(img_path).convert("RGB")
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)

    encrypted_path = os.path.splitext(img_path)[0] + "_encrypted.png"
    image.save(encrypted_path)
    show_output_image(encrypted_path)
    status_label.config(text="Image Encrypted and Saved")

def decrypt_image():
    if img_path is None:
        messagebox.showwarning("No Image", "Please load an image first.")
        return

    image = Image.open(img_path).convert("RGB")
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)

    decrypted_path = os.path.splitext(img_path)[0] + "_decrypted.png"
    image.save(decrypted_path)
    show_output_image(decrypted_path)
    status_label.config(text="Image Decrypted and Saved")

def show_output_image(output_path):
    output_img = Image.open(output_path)
    output_img_display = ImageTk.PhotoImage(output_img.resize((250, 250)))
    output_label.config(image=output_img_display)
    output_label.image = output_img_display  # Keep reference

# GUI Setup
root = tk.Tk()
root.title("Image Encryptor/Decryptor")
root.geometry("600x550")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="Simple Image Encryptor/Decryptor", font=("Helvetica", 16, "bold"), fg="white", bg="#1e1e1e")
title.pack(pady=10)

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=5)

load_btn = tk.Button(btn_frame, text="Load Image", command=load_image, width=20, bg="#4a90e2", fg="white")
load_btn.grid(row=0, column=0, padx=10)

encrypt_btn = tk.Button(btn_frame, text="Encrypt", command=encrypt_image, width=20, bg="#27ae60", fg="white")
encrypt_btn.grid(row=0, column=1, padx=10)

decrypt_btn = tk.Button(btn_frame, text="Decrypt", command=decrypt_image, width=20, bg="#e67e22", fg="white")
decrypt_btn.grid(row=0, column=2, padx=10)

image_label = tk.Label(root, bg="#1e1e1e")
image_label.pack(pady=10)

output_label = tk.Label(root, bg="#1e1e1e")
output_label.pack(pady=10)

status_label = tk.Label(root, text="", bg="#1e1e1e", fg="lightgray")
status_label.pack()

# Global variables
img = None
img_display = None
img_path = None

root.mainloop()