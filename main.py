import eel
import psutil
import sys
import os

# EXE olarak çalışırken yolu bulması için gerekli
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

# 'web' klasörünü arayüz olarak tanıt
eel.init('web')

@eel.expose 
def get_system_stats():
    # Donanım verilerini çek
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    return {"cpu": cpu, "ram": ram}

@eel.expose
def optimize_system():
    # Burası optimizasyonun yapılacağı yer (şimdilik test mesajı)
    return "Sistem Optimize Edildi!"

# Uygulamayı başlat
eel.start('index.html', size=(1100, 700), mode='chrome')
