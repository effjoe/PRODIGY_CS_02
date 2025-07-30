# 🖼️ Simple Image Encryptor/Decryptor (Tkinter GUI)

This is a beginner-friendly GUI application built with Python and Tkinter that allows you to **encrypt and decrypt images** using **color inversion**.

> 🔐 **Encryption Logic:** Each pixel color (R, G, B) is inverted using `255 - value`. Since inversion is reversible, the same process decrypts it.

---

## 📸 Features

* ✅ Load any `.png`, `.jpg`, or `.jpeg` image
* 🔐 Encrypt the image with a click (using color inversion)
* 🔓 Decrypt the image using the same logic
* 🖼️ Preview original and result images
* 🖤 Minimal dark-themed interface

---

## 🛠️ How It Works

1. **Load Image:** Select an image file from your system.
2. **Encrypt:** Click the `Encrypt` button. It will invert the RGB values and save a new file with `_encrypted.png` suffix.
3. **Decrypt:** Load the encrypted image and click `Decrypt` to restore the original colors.

---

## 🧑‍💻 Tech Stack

* **Python 3**
* **Tkinter** (GUI)
* **Pillow (PIL)** for image processing

---

## 📦 Installation

1. **Clone or Download** this repo.
2. Make sure Python is installed.
3. Install Pillow:

```bash
pip install pillow
```

4. Run the script:

```bash
python your_script_name.py
```

---

## 👨‍🎓 Made for Learning & Fun

This project is a simple way to learn about:

* GUI design using Tkinter
* Image manipulation using PIL
* Basic encryption logic
