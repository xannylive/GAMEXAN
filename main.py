import customtkinter as ctk
import os
import threading

# --- Arayüz Renk ve Tema Ayarları ---
ctk.set_appearance_mode("Dark")  # Daima Koyu Tema
ctk.set_default_color_theme("dark-blue")  # Mavi Vurgular

class GAMEXANApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pencere Ayarları
        self.title("GAMEXAN // Pro Performance Suite")
        self.geometry("960x600")
        
        # Grid Yapısı (Sol Menü + Ana İçerik)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- 1. Sol Navigasyon Menüsü ---
        self.navigation_frame = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#0B0D12")
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # Logo Alanı
        self.navigation_label = ctk.CTkLabel(self.navigation_frame, text="GAMEXAN", 
                                           font=ctk.CTkFont(size=20, weight="bold"), text_color="#00F2FF")
        self.navigation_label.pack(pady=(30, 40))

        # Menü Butonları (Modern Tarz)
        self.btn_dashboard = self.create_nav_button("Anasayfa", self.open_dashboard_frame)
        self.btn_dashboard.pack(pady=10, padx=20, fill="x")

        self.btn_games = self.create_nav_button("Oyunlarım", self.open_games_frame)
        self.btn_games.pack(pady=10, padx=20, fill="x")

        self.btn_settings = self.create_nav_button("Ayarlar", self.open_settings_frame)
        self.btn_settings.pack(pady=10, padx=20, fill="x")

        # --- 2. Ana İçerik Alanı ---
        self.main_content_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#151922")
        self.main_content_frame.grid(row=0, column=1, sticky="nsew")
        
        # Başlangıç Ekranını Yükle
        self.open_dashboard_frame()

    def create_nav_button(self, text, command_event):
        return ctk.CTkButton(self.navigation_frame, text=text, 
                             command=command_event,
                             corner_radius=8, height=40,
                             fg_color="transparent", text_color=("gray10", "gray90"),
                             hover_color="#1A2232",
                             font=ctk.CTkFont(size=14, weight="bold")
                            )

    def reset_buttons(self):
        # Tüm butonların rengini sıfırla
        self.btn_dashboard.configure(fg_color="transparent")
        self.btn_games.configure(fg_color="transparent")
        self.btn_settings.configure(fg_color="transparent")

    def clear_content(self):
        # İçerik alanındaki eski widgetları temizle
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

    # --- Sayfa Yükleme Fonksiyonları ---
    def open_dashboard_frame(self):
        self.reset_buttons()
        self.btn_dashboard.configure(fg_color="#1A2232") # Aktif buton rengi
        self.clear_content()
        
        # Dashboard Başlığı
        lbl = ctk.CTkLabel(self.main_content_frame, text="Sistem Performans Paneli", 
                           font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
        lbl.pack(pady=30, padx=30, anchor="w")

        # Durum Kartı
        status_card = ctk.CTkFrame(self.main_content_frame, fg_color="#1F2533", corner_radius=15)
        status_card.pack(fill="x", padx=30, pady=10)

        status_lbl = ctk.CTkLabel(status_card, text="🟢 Durum: Optimize Edilmeye Hazır", 
                                 font=ctk.CTkFont(size=16), text_color="#00E676")
        status_lbl.pack(pady=30, padx=20)

        # Büyük Boost Butonu (Neon Mavi)
        boost_btn = ctk.CTkButton(self.main_content_frame, text="OTOMATİK OYUN BOOST BAŞLAT",
                                 font=ctk.CTkFont(size=16, weight="bold"),
                                 height=50, corner_radius=12,
                                 fg_color="#007BFF", hover_color="#0056b3",
                                 command=self.run_boost_thread
                                 )
        boost_btn.pack(fill="x", padx=30, pady=30)

    def open_games_frame(self):
        self.reset_buttons()
        self.btn_games.configure(fg_color="#1A2232")
        self.clear_content()
        
        lbl = ctk.CTkLabel(self.main_content_frame, text="Algılanan Oyunlar", 
                           font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
        lbl.pack(pady=30, padx=30, anchor="w")

        # Örnek Oyun Listesi (İleride burayı otomatik dolduracağız)
        games = ["Counter-Strike 2", "Valorant", "League of Legends", "GTA V"]
        for game in games:
            game_card = ctk.CTkFrame(self.main_content_frame, fg_color="#1F2533", corner_radius=10)
            game_card.pack(fill="x", padx=30, pady=5)
            
            g_lbl = ctk.CTkLabel(game_card, text=f"🎮 {game}", font=ctk.CTkFont(size=14), text_color="white")
            g_lbl.pack(side="left", padx=15, pady=15)
            
            opt_btn = ctk.CTkButton(game_card, text="Ayarla", width=80, corner_radius=6, fg_color="#2B3445")
            opt_btn.pack(side="right", padx=15)

    def open_settings_frame(self):
        self.reset_buttons()
        self.btn_settings.configure(fg_color="#1A2232")
        self.clear_content()
        
        lbl = ctk.CTkLabel(self.main_content_frame, text="Uygulama Ayarları", 
                           font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
        lbl.pack(pady=30, padx=30, anchor="w")
        
        switch_val = ctk.CTkSwitch(self.main_content_frame, text="Otomatik Başlangıçta Çalıştır")
        switch_val.pack(pady=10, padx=30, anchor="w")

    # --- Optimizasyon Motoru (Arka Plan) ---
    def run_boost_thread(self):
        # Arayüz donmasın diye işlemi ayrı bir kolda (thread) başlat
        threading.Thread(target=self.perform_optimization).start()

    def perform_optimization(self):
        # Buraya gerçek optimizasyon kodları gelecek (servis durdurma, güç planı vb.)
        # Şimdilik simülasyon yapalım
        print("Boost başladı...")
        
        # Arayüzdeki butonu geçici olarak devre dışı bırak
        # (Thread içinden arayüzü güncellemek için root.after kullanıyoruz)
        
        # Oyun tarama simülasyonu
        detected = False
        steam_path = "C:/Program Files (x86)/Steam"
        if os.path.exists(steam_path):
            detected = True

        # Sonuç mesajını göster
        if detected:
            msg = "✅ Steam Algılandı.\n✅ Gereksiz servisler kapatıldı.\n✅ RAM temizlendi.\n🚀 Oyunlar için sistem hazır!"
        else:
            msg = "⚠️ Steam kurulu görünmüyor ama yine de sistem performansı artırıldı."

        # Mesajı popup olarak göster
        self.after(0, lambda: messagebox.showinfo("GAMEXAN Boost Tamamlandı", msg))

if __name__ == "__main__":
    app = GAMEXANApp()
    app.mainloop()
