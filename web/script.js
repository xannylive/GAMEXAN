async function updateHardwareStats() {
    let stats = await eel.get_system_stats()();
    document.getElementById("hardware-stats").innerText = 
        `💻 CPU: %${stats.cpu}\n🧠 RAM: %${stats.ram}`;
}
setInterval(updateHardwareStats, 1000);

async function startBoost() {
    let btn = document.querySelector(".btn-action");
    let originalText = btn.innerText;
    btn.innerText = "İşleniyor...";
    let result = await eel.optimize_system()();
    btn.innerText = result;
    setTimeout(() => { btn.innerText = originalText; }, 2000);
}
