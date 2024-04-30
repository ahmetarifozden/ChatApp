import sqlite3
import tkinter as tk
from tkinter import messagebox

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Kullanıcı tablosunu oluştur (eğer daha önce oluşturulmadıysa)
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

# Kullanıcı doğrulama fonksiyonu
def authenticate(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    if user:
        return True
    else:
        return False

# Kullanıcı girişi işlevi
def login():
    # Kullanıcı adı ve parolayı al
    username = username_entry.get()
    password = password_entry.get()

    # Kullanıcı doğrulama
    if authenticate(username, password):
        messagebox.showinfo("Giriş Başarılı", "Hoş geldiniz, " + username + "!")
    else:
        messagebox.showerror("Giriş Başarısız", "Geçersiz kullanıcı adı veya parola!")

# Ana uygulama penceresini oluştur
root = tk.Tk()
root.title("Giriş Ekranı")

# Kullanıcı adı etiketi ve giriş alanı
username_label = tk.Label(root, text="Kullanıcı Adı:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Parola etiketi ve giriş alanı
password_label = tk.Label(root, text="Parola:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Giriş düğmesi
login_button = tk.Button(root, text="Giriş Yap", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Ana döngüyü başlat
root.mainloop()

# Veritabanı bağlantısını kapat
conn.close()
