import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import hashlib
import os

def get_key_from_password(password):
    hashed = hashlib.sha256(password.encode()).digest()
    return list(hashed)

def process_image(mode, input_path, password, output_path):
    if not input_path or not password:
        return "Missing image or password!"

    try:
        key = get_key_from_password(password)
        img = Image.open(input_path).convert("RGB")
        pixels = img.load()
        width, height = img.size
        k = 0

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]

                if mode == 'encrypt':
                    r = (r + key[k % len(key)]) % 256
                    g = (g + key[(k + 1) % len(key)]) % 256
                    b = (b + key[(k + 2) % len(key)]) % 256
                else:
                    r = (r - key[k % len(key)]) % 256
                    g = (g - key[(k + 1) % len(key)]) % 256
                    b = (b - key[(k + 2) % len(key)]) % 256

                pixels[x, y] = (r, g, b)
                k += 3

        img.save(output_path)
        display_output_preview(output_path)
        return f"Image {mode}ed and saved to:\n{output_path}"
    except Exception as e:
        return f"Error: {str(e)}"

def browse_image():
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    image_path.set(path)
    display_image_preview(path)

def choose_output_location():
    filename = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg")])
    output_path.set(filename)

def display_image_preview(path):
    try:
        img = Image.open(path)
        img.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(img)
        input_image_label.config(image=photo)
        input_image_label.image = photo
    except Exception as e:
        status_label.config(text=f"Preview error: {e}")

def display_output_preview(path):
    try:
        img = Image.open(path)
        img.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(img)
        output_image_label.config(image=photo)
        output_image_label.image = photo
    except Exception as e:
        status_label.config(text=f"Output preview error: {e}")

def encrypt_image():
    if not output_path.get():
        choose_output_location()
    result = process_image('encrypt', image_path.get(), password.get(), output_path.get())
    status_label.config(text=result)

def decrypt_image():
    if not output_path.get():
        choose_output_location()
    result = process_image('decrypt', image_path.get(), password.get(), output_path.get())
    status_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("Image Encryptor & Decryptor with Preview")
root.geometry("600x500")
root.resizable(False, False)

image_path = tk.StringVar()
password = tk.StringVar()
output_path = tk.StringVar()

# Top input section
tk.Label(root, text="Select Image:").pack(pady=5)
tk.Entry(root, textvariable=image_path, width=50).pack()
tk.Button(root, text="Browse", command=browse_image).pack(pady=5)

tk.Label(root, text="Enter Password:").pack()
tk.Entry(root, textvariable=password, show="*", width=30).pack()

# Image Preview Section
preview_frame = tk.Frame(root)
preview_frame.pack(pady=10)

tk.Label(preview_frame, text="Original Image").grid(row=0, column=0)
tk.Label(preview_frame, text="Processed Image").grid(row=0, column=1)

input_image_label = tk.Label(preview_frame)
input_image_label.grid(row=1, column=0, padx=10)

output_image_label = tk.Label(preview_frame)
output_image_label.grid(row=1, column=1, padx=10)

# Buttons and status
tk.Button(root, text="Encrypt Image", bg="#4CAF50", fg="white", command=encrypt_image).pack(pady=10)
tk.Button(root, text="Decrypt Image", bg="#f44336", fg="white", command=decrypt_image).pack()

status_label = tk.Label(root, text="", wraplength=500, fg="blue")
status_label.pack(pady=10)

root.mainloop()