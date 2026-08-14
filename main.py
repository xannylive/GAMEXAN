import tkinter as tk
from tkinter import messagebox

class GAMEXANApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GAMEXAN // PC Optimizer & FPS Booster")
        self.root.geometry("950x580")
        self.root.configure(bg="#0B0E14")
        self.root.resizable(False, False)

        # Üst Başlık
        title_lbl = tk.Label(root, text="GAMEXAN OPTIMIZER", font=("Arial", 18, "bold"), bg="#0B0E14", fg="#00F0FF")
        title_lbl.pack(pady=25)

        # Sol Menü / Buton Alanı
        self.create_sidebar()

    def create_sidebar(self):
        # Ana Çerçeve
        main_frame = tk.Frame(self.root, bg="#121824", bd=0)
        main_frame.place(x=30, y=80, width=890, height=460)

        # Durum Yazısı
        status_lbl = tk.Label(main_frame, text="🟢 Sistem Durumu: Optimize Edilmeye Hazır", font=("Arial", 12), bg="#121824", fg="#00FF66")
        status_lbl.pack(anchor="w", padx=30, pady=25)

        # FPS Boost Butonu
        boost_btn = tk.Button(
            main_frame, 
            text="OTOMATİK OYUNLARI ALGILA & BOOST BAŞLAT", 
            font=("Arial", 12, "bold"), 
            bg="#007ACC", 
            fg="#FFFFFF", 
            activebackground="#005C99",
            activeforeground="#FFFFFF",
            relief="flat",
            cursor="hand2",
            command=self.boost_action
        )
        boost_btn.pack(padx=30, pady=10, fill="x", ipady=12)

    def boost_action(self):
        messagebox.showinfo("GAMEXAN", "Oyunlar tarandı! Sistem performansı en üst düzeye çıkarıldı.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GAMEXANApp(root)
    root.mainloop()
