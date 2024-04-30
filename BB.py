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


# Kullanıcı mesajlarını gönderme işlevi
def send_message():
    selected_user = users_listbox.get(tk.ACTIVE)
    message = message_entry.get()
    messages[selected_user].append("Ben: " + message)
    messagebox.showinfo("Mesaj Gönderildi", "Mesaj gönderildi!")
    update_message_list(selected_user)

# Seçilen kullanıcının mesajlarını güncelleme işlevi
def update_message_list(user):
    messages_listbox.delete(0, tk.END)
    for msg in messages[user]:
        messages_listbox.insert(tk.END, msg)

# Kullanıcı girişi işlevi
def login():
    username = username_entry.get()
    if username in users:
        messagebox.showinfo("Giriş Başarılı", "Hoş geldiniz, " + username + "!")
        main_window(username)
    else:
        messagebox.showerror("Giriş Başarısız", "Geçersiz kullanıcı adı!")

# Ana pencereyi oluşturma işlevi
def main_window(username):
    login_window.destroy()

    # Ana pencereyi oluştur
    main_window = tk.Tk()
    main_window.title("Ana Sayfa")

    # Kullanıcı adını görüntüle
    username_label = tk.Label(main_window, text="Kullanıcı Adı: " + username)
    username_label.pack(pady=10)

    # Mesaj gönderme alanı
    message_entry = tk.Entry(main_window, width=50)
    message_entry.pack(pady=5)

    # Gönder düğmesi
    send_button = tk.Button(main_window, text="Gönder", command=send_message)
    send_button.pack(pady=5)

    # Kullanıcılar listesi
    users_listbox = tk.Listbox(main_window, width=20)
    for user in users:
        users_listbox.insert(tk.END, user)
    users_listbox.pack(side=tk.LEFT, padx=10)

    # Mesajlar listesi
    messages_listbox = tk.Listbox(main_window, width=50, height=20)
    messages_listbox.pack(side=tk.RIGHT, padx=10)

    # Seçilen kullanıcının mesajlarını güncelle
    def on_select(event):
        selected_user = users_listbox.get(tk.ACTIVE)
        update_message_list(selected_user)

    users_listbox.bind("<<ListboxSelect>>", on_select)

    main_window.mainloop()

# Giriş penceresini oluştur
login_window = tk.Tk()
login_window.title("Giriş Ekranı")

# Kullanıcı adı etiketi ve giriş alanı
username_label = tk.Label(login_window, text="Kullanıcı Adı:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(login_window)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Giriş düğmesi
login_button = tk.Button(login_window, text="Giriş Yap", command=login)
login_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

users_listbox.bind("<<ListboxSelect>>", on_select)

# Ana döngüyü başlat
login_window.mainloop()
