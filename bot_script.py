import os
import time
import subprocess

def run_adb(command):
    subprocess.run(f"adb shell {command}", shell=True)

# 1. App එක Launch කිරීම
print("OnStream ඇප් එක විවෘත කරයි...")
run_adb("monkey -p com.onstream.app -c android.intent.category.LAUNCHER 1")
time.sleep(30)

# 2. Movies ටැබ් එක Click කිරීම
run_adb("input tap 300 1500") 
time.sleep(5)

# 3. Filter Icon එක Click කිරීම
run_adb("input tap 950 150")
time.sleep(5)

# 4. Filter Submit කිරීම
run_adb("input tap 500 1800")
time.sleep(10)

# 5. පළමු result එක තේරීම
run_adb("input tap 300 500")
time.sleep(15)

# 6. ඩවුන්ලෝඩ් කර Google Drive වෙත යැවීම
# මෙහිදී 'rclone' භාවිතයෙන් 2GB ට වැඩි ෆයිල් Drive එකට යැවේ
# ඔබ සෑදූ 'gdrive' config එක මෙහිදී භාවිතා වේ
def upload_process(filename):
    size_gb = os.path.getsize(filename) / (1024**3)
    if size_gb > 2:
        print(f"ප්‍රමාණය {size_gb:.2f}GB - Google Drive වෙත යවයි...")
        os.system(f"rclone copy {filename} gdrive:Movies/")
    else:
        print("Telegram වෙත යවයි...")
    if size_gb > 2:
        print(f"ප්‍රමාණය {size_gb:.2f}GB - Google Drive වෙත යවයි...")
        os.system(f"rclone copy {file_path} gdrive:Movies/")
    else:
        print("Telegram වෙත යවයි...")
        # Telegram logic here
    # Telegram upload logic
