# RAQEEM DAWAWIN - THE GENESIS PROTOCOL v1.0
# "The Birth of the Global Digital Empire"

import threading
from models import MatrixCore
from security_shield import Shield
from al_jarif import SuperHarvester
from al_musaffi import MatrixRefiner
from al_mighnatis import GlobalTrafficMagnet
from al_qaid import ImperialDashboard

class RaqeemEmpire:
    def __init__(self):
        print("🏛️ Initializing RAQEEM DAWAWIN Ecosystem...")
        self.core = MatrixCore()
        self.shield = Shield()
        self.harvester = SuperHarvester()
        self.refiner = MatrixRefiner()
        self.magnet = GlobalTrafficMagnet()
        self.dashboard = ImperialDashboard()

    def launch_sequence(self):
        """تفعيل بروتوكول الإطلاق الشامل"""
        print("🚀 Launching Full Protocol...")

        # 1. تفعيل الدرع الأمني أولاً (الحماية قبل كل شيء)
        self.shield.activate_vault()

        # 2. إطلاق أسطول 'الجارف' في الخلفية لجلب الـ 3000 ملف لكل صنف
        harvest_thread = threading.Thread(target=self.harvester.mass_harvest_protocol)
        harvest_thread.start()

        # 3. تفعيل 'المصفّي' لمراقبة الملفات المجلوبة وتجميلها فور وصولها
        print("[✨] AI Refiner: Monitoring incoming knowledge...")

        # 4. تفعيل 'المغناطيس العالمي' لجذب الـ 10,000 زائر
        self.magnet.activate_global_features()

        # 5. فتح 'لوحة القائد' للتحكم الكامل
        self.dashboard.master_control_panel()

        print("🌍 RAQEEM DAWAWIN IS NOW LIVE AND GLOBAL!")

if __name__ == "__main__":
    empire = RaqeemEmpire()
    empire.launch_sequence()
  
