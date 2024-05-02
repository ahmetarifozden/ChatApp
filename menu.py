import tkinter as tk
from tkinter import messagebox
#import BB
#import BT 


# Bireysel sohbet işlevi
def individual_chat():
    messagebox.showinfo("Bireysel Sohbet", "Bireysel sohbet seçildi.")
    str  = "individual_chat"
    import BB
# Bireysel-topluluk sohbet işlevi
def group_chat():
    import BT
    messagebox.showinfo("Bireysel-Topluluk Sohbet", "Bireysel-topluluk sohbet seçildi.")
    str = "group_chat"
    import BT

# Ana pencereyi oluşturma işlevi
def main_window():
    # Ana pencereyi oluştur
    root = tk.Tk()
    root.title("Sohbet Seçimi")

    # Başlık etiketi
    title_label = tk.Label(root, text="Lütfen bir sohbet seçeneği seçin:")
    title_label.pack(pady=10)

    # Bireysel sohbet düğmesi
    individual_button = tk.Button(root, text="Bireysel Sohbet", command=individual_chat)
    individual_button.pack(pady=5)

    # Bireysel-topluluk sohbet düğmesi
    group_button = tk.Button(root, text="Bireysel-Topluluk Sohbet", command=group_chat)
    group_button.pack(pady=5)

    root.mainloop()

# Ana pencereyi oluştur
main_window()
