import tkinter as tk
from tkinter import messagebox

# Kullanıcılar
users = ["Ahmet", "Mehmet", "Ayşe", "Fatma"]

# Mesajlar
messages = {
    "Ahmet": [],
    "Mehmet": [],
    "Ayşe": [],
    "Fatma": []
}

# Seçilen kullanıcı
selected_user = None

# Mesaj gönderme işlevi
def send_message():
    global selected_user
    if selected_user:
        message = message_entry.get()
        messages[selected_user].append("Ben: " + message)
        update_message_list(selected_user)
        messagebox.showinfo("Mesaj Gönderildi", "Mesaj gönderildi!")
    else:
        messagebox.showerror("Hata", "Lütfen bir kullanıcı seçin.")

# Kullanıcıyı güncelleme işlevi
def update_user(event):
    global selected_user
    selected_user = users_listbox.get(tk.ACTIVE)
    update_message_list(selected_user)

# Mesajları güncelleme işlevi
def update_message_list(user):
    messages_listbox.delete(0, tk.END)
    for msg in messages[user]:
        messages_listbox.insert(tk.END, msg)

# Ana pencereyi oluşturma işlevi
def main_window():
    global users_listbox, messages_listbox, message_entry

    # Ana pencereyi oluştur
    root = tk.Tk()
    root.title("Bireysel Mesajlaşma Uygulaması")

    # Kullanıcılar listesi
    users_listbox = tk.Listbox(root, width=20)
    for user in users:
        users_listbox.insert(tk.END, user)
    users_listbox.pack(side=tk.LEFT, padx=10)
    users_listbox.bind("<<ListboxSelect>>", update_user)

    # Mesajlar listesi
    messages_listbox = tk.Listbox(root, width=50, height=20)
    messages_listbox.pack(side=tk.RIGHT, padx=10)

    # Mesaj gönderme alanı
    message_entry = tk.Entry(root, width=50)
    message_entry.pack(side=tk.BOTTOM, padx=10, pady=10)

    # Gönder düğmesi
    send_button = tk.Button(root, text="Gönder", command=send_message)
    send_button.pack(side=tk.BOTTOM, padx=10, pady=5)

    root.mainloop()

# Ana pencereyi oluştur
main_window()
