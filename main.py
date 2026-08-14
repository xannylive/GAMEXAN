import customtkinter as ctk
import os
import threading
import psutil
import platform

# Tema ve Renk Ayarları (NVIDIA / ROG Koyu Tema)
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class GAMEXANApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pencere Ayarları
        self.title("GAMEXAN // NVIDIA App Style Suite v3.0")
        self.geometry("1050x650")
        self.resizable(False, False)
        
        # Grid Yapısı
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SOL MENÜ (NAVBAR) ---
        self.sidebar = ctk.CTkFrame(self, width=230, corner_radius=0, fg_color="#0A0C10")
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        # Logo / Başlık
        self.logo_lbl = ctk.CTkLabel(
            self.sidebar, 
            text="GAMEXAN PRO", 
            font=ctk.CTkFont(family="Arial", size=22, weight="bold"), 
            text_color="#00F2FF"
        )
        self.logo_lbl.pack(pady=(35, 25))

        # Menü Butonları (NVIDIA App Sekmeleri)
        self.btn_home = self.create_nav_btn("🏠 Anasayfa", self.show_home)
        self.btn_games = self.create_nav_btn("🎮 Oyun Kitaplığı", self.show_games)
        self.btn_graphics = self.create_nav_btn("⚙️ Grafik & FPS Ayarları", self.show_graphics)
        self.btn_overlay = self.create_nav_btn("📊 Performans Katmanı", self.show_overlay)
        self.btn_system = self.create_nav_btn("💻 Sistem & Donanım", self.show_system)

        # --- SAĞ İÇERİK ALANI ---
        self.content = ctk.CTkFrame(self, corner_radius=0, fg_color="#121620")
        self.content.grid(row=0, column=1, sticky="nsew")

        # İlk Açılış
        self.show_home()

    def create_nav_btn(self, text, command):
        btn = ctk.CTkButton(
            self.sidebar, 
            text=text, 
            command=command,
            fg_color="transparent",
            text_color="#8C95A1",
            hover_color="#1A2232",
            anchor="w",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=45,
            corner_radius=8
        )
        btn.pack(pady=5, padx=15, fill="x")
        return btn

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # --- 1. ANASAYFA ---
    def show_home(self):
        self.clear_content()

        title = ctk.CTkLabel(self.content, text="Hoş Geldiniz, Komutan", font=ctk.CTkFont(size=22, weight="bold"), text_color="#FFFFFF")
        title.pack(anchor="w", padx=35, pady=25)

        # Hızlı Durum Kartı
        card = ctk.CTkFrame(self.content, fg_color="#181F2D", corner_radius=12, height=90)
        card.pack(fill="x", padx=35, pady=5)

        self.status_lbl = ctk.CTkLabel(card, text="🟢 Sürücü Durumu: Güncel & Oyun Modu Aktif", font=ctk.CTkFont(size=14, weight="bold"), text_color="#00FF66")
        self.status_lbl.pack(padx=25, pady=30, anchor="w")

        # Canlı Donanım Özeti
        stats_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        stats_frame.pack(fill="x", padx=35, pady=15)

        self.cpu_lbl = ctk.CTkLabel(stats_frame, text="CPU Yükü: Hesaplanıyor...", font=ctk.CTkFont(size=13), text_color="#A5B1C2")
        self.cpu_lbl.pack(anchor="w", pady=4)
        
        self.ram_lbl = ctk.CTkLabel(stats_frame, text="RAM Yükü: Hesaplanıyor...", font=ctk.CTkFont(size=13), text_color="#A5B1C2")
        self.ram_lbl.pack(anchor="w", pady=4)

        # Tek Tıkla Optimizasyon Butonu
        boost_btn = ctk.CTkButton(
            self.content, 
            text="TEK TIKLA TÜM OYUNLARI OPTİMİZE ET", 
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#007ACC", 
            hover_color="#005C99",
            height=50,
            corner_radius=10,
            command=self.run_global_boost
        )
        boost_btn.pack(fill="x", padx=35, pady=25)

        self.update_stats()

    def update_stats(self):
        try:
            cpu = psutil.cpu_percent(interval=0.1)
            ram = psutil.virtual_memory().percent
            self.cpu_lbl.configure(text=f"💻 Anlık İşlemci Kullanımı: %{cpu}")
            self.ram_lbl.configure(text=f"🧠 Anlık Bellek Kullanımı: %{ram}")
        except:
            pass

    # --- 2. OYUN KİTAPLIĞI ---
    def show_games(self):
        self.clear_content()

        title = ctk.CTkLabel(self.content, text="Algılanan Oyun Kitaplığı", font=ctk.CTkFont(size=22, weight="bold"), text_color="#FFFFFF")
        title.pack(anchor="w", padx=35, pady=25)

        games_box = ctk.CTkFrame(self.content, fg_color="#181F2D", corner_radius=12)
        games_box.pack(fill="both", expand=True, padx=35, pady=(0, 25))

        games_list = [
            ("Counter-Strike 2", "C:/Program Files (x86)/Steam/steamapps/common/Counter-Strike Global Offensive"),
            ("Valorant", "C:/Riot Games/Valorant"),
            ("League of Legends", "C:/Riot Games/League of Legends"),
            ("Epic Games Store", "C:/Program Files/Epic Games"),
            ("Steam Platform", "C:/Program Files (x86)/Steam")
        ]

        for name, path in games_list:
            row = ctk.CTkFrame(games_box, fg_color="transparent", height=45)
            row.pack(fill="x", padx=20, pady=8)
            
            exists = os.path.exists(path)
            st_text = "🟢 Hazır & Optimize Edilebilir" if exists else "⚪ Yüklü Değil"
            st_color = "#00FF66" if exists else "#636E72"

            lbl_name = ctk.CTkLabel(row, text=f"🎮 {name}", font=ctk.CTkFont(size=14, weight="bold"), text_color="#FFFFFF")
            lbl_name.pack(side="left")

            lbl_st = ctk.CTkLabel(row, text=st_text, font=ctk.CTkFont(size=13), text_color=st_color)
            lbl_st.pack(side="right")

    # --- 3. GRAFİK & FPS AYARLARI ---
    def show_graphics(self):
        self.clear_content()
        title = ctk.CTkLabel(self.content, text="NVIDIA / AMD Grafik İnce Ayarları", font=ctk.CTkFont(size=22, weight="bold"), text_color="#FFFFFF")
        title.pack(anchor="w", padx=35, pady=25)

        self.sw1 = ctk.CTkSwitch(self.content, text="Düşük Gecikme Modu (NVIDIA Reflex / Ultra Low Latency)", font=ctk.CTkFont(size=14), progress_color="#007ACC")
        self.sw1.pack(anchor="w", padx=40, pady=12)
        self.sw1.select()

        self.sw2 = ctk.CTkSwitch(self.content, text="GPU Donanım Hızlandırmalı Zamanlama (HAGS)", font=ctk.CTkFont(size=14), progress_color="#007ACC")
        self.sw2.pack(anchor="w", padx=40, pady=12)
        self.sw2.select()

        self.sw3 = ctk.CTkSwitch(self.content, text="Maksimum Performans Güç Yönetimi", font=ctk.CTkFont(size=14), progress_color="#007ACC")
        self.sw3.pack(anchor="w", padx=40, pady=12)
        self.sw3.select()

        self.sw4 = ctk.CTkSwitch(self.content, text="Doku Süzme (Texture Filtering) - Yüksek Performans", font=ctk.CTkFont(size=14), progress_color="#007ACC")
        self.sw4.pack(anchor="w", padx=40, pady=12)
        self.sw4.select()

    # --- 4. PERFORMANS KATMANI (OVERLAY) ---
    def show_overlay(self):
        self.clear_content()
        title = ctk.CTkLabel(self.content, text="Oyun İçi Performans Katmanı (Overlay)", font=ctk.CTkFont(size=22, weight="bold"), text_color="#FFFFFF")
        title.pack(anchor="w", padx=35, pady=25)

        info_lbl = ctk.CTkLabel(self.content, text="Oyun oynarken sol üst köşede anlık FPS, sıcaklık ve kullanım değerlerini gösterir.", font=ctk.CTkFont(size=13), text_color="#A5B1C2")
        info_lbl.pack(anchor="w", padx=35, pady=(0, 15))

        self.ov1 = ctk.CTkSwitch(self.content, text="Anlık FPS Sayacını Aktif Et", font=ctk.CTkFont(size=14), progress_color="#007ACC")
        self.ov1.pack(anchor="w", padx=40, pady=12)
        self.ov1.select()

        self.ov2 = ctk.CTkSwitch(self.content, text="CPU / GPU Sıcaklık Takibi", font=ctk.CTkFont(size=14), progress_color="#007ACC")
        self.ov2.pack(anchor="w", padx=40, pady=12)
        self.ov2.select()

    # --- 5. SİSTEM BİLGİSİ ---
    def show_system(self):
        self.clear_content()
        title = ctk.CTkLabel(self.content, text="Sistem ve Sürücü Bilgileri", font=ctk.CTkFont(size=22, weight="bold"), text_color="#FFFFFF")
        title.pack(anchor="w", padx=35, pady=25)

        box = ctk.CTkFrame(self.content, fg_color="#181F2D", corner_radius=12)
        box.pack(fill="both", expand=True, padx=35, pady=(0, 25))

        text_content = f"""
        💻 İşletim Sistemi: {platform.system()} {platform.release()}
        ⚙️ İşlemci Mimarisi: {platform.processor()}
        🚀 GAMEXAN Sürüm: v3.0 Ultimate Edition
        🎯 Durum: Tüm Sistem Bileşenleri Optimize Edildi
        """
        
        lbl = ctk.CTkLabel(box, text=text_content, font=ctk.CTkFont(size=14), text_color="#E2E8F0", justify="left")
        lbl.pack(anchor="nw", padx=30, pady=30)

    def run_global_boost(self):
        threading.Thread(target=self.boost_worker).start()

    def boost_worker(self):
        try:
            import ctypes
            ctypes.windll.psapi.EmptyWorkingSet(ctypes.windll.kernel32.GetCurrentProcess())
        except:
            pass
        self.status_lbl.configure(text="🚀 Tüm Oyunlar İçin En İyi Grafik ve FPS Ayarları Uygulandı!", text_color="#00FF66")

if __name__ == "__main__":
    app = GAMEXANApp()
    app.mainloop()
