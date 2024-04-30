import tkinter as tk
from tkinter import messagebox

# Oda verileri
rooms = {
    "software team": [],
    "management team": [],
    "general community": []
}

# Seçilen oda adı
selected_room = None

# Mesaj gönderme işlevi
def send_message():
    global selected_room
    if selected_room:
        message = message_entry.get()
        rooms[selected_room].append("Ben: " + message)
        update_message_list(selected_room)
        messagebox.showinfo("Mesaj Gönderildi", "Mesaj gönderildi!")
    else:
        messagebox.showerror("Hata", "Lütfen bir oda seçin.")

# Seçilen odayı güncelleme işlevi
def update_message_list(room):
    global messages_listbox
    messages_listbox.delete(0, tk.END)
    for msg in rooms[room]:
        messages_listbox.insert(tk.END, msg)

# Oda değiştirme işlevi
def change_room(event):
    global selected_room
    selected_room = rooms_listbox.get(tk.ACTIVE)
    update_message_list(selected_room)

# Ana pencereyi oluşturma işlevi
def main_window():
    global rooms_listbox, messages_listbox, message_entry

    # Ana pencereyi oluştur
    root = tk.Tk()
    root.title("Topluluk Mesajlaşma Uygulaması")

    # Oda listesi
    rooms_listbox = tk.Listbox(root, width=20)
    for room in rooms:
        rooms_listbox.insert(tk.END, room)
    rooms_listbox.pack(side=tk.LEFT, padx=10)
    rooms_listbox.bind("<<ListboxSelect>>", change_room)

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
