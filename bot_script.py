import os
import time
import subprocess

def run_adb(command):
    subprocess.run(f"adb shell {command}", shell=True)

# 1. App එක Open කිරීම
print("OnStream විවෘත වේ...")
run_adb("monkey -p com.onstream.app -c android.intent.category.LAUNCHER 1")
time.sleep(25)

# 2. Movies ටැබ් එකට යාම
print("Movies ටැබ් එක තෝරා ගනී...")
run_adb("input tap 300 1500") 
time.sleep(5)

# 3. Filter මෙනුවට යාම
print("Filter මෙනුවට පිවිසේ...")
run_adb("input tap 950 150")
time.sleep(5)

# 4. Filter Submit කිරීම
print("සැකසුම් Submit කරයි...")
run_adb("input tap 500 1800")
time.sleep(10)

# 5. පළමු මූවී එක තේරීම
print("මූවී එක තෝරා ගනී...")
run_adb("input tap 300 500")
time.sleep(10)

# 6. ඩවුන්ලෝඩ් කර Google Drive වෙත යැවීම
# (මෙහිදී මූවී එක ඩවුන්ලෝඩ් වූ පසු rclone හරහා යැවීම සිදුවේ)
def upload_to_drive(file_path):
    size_gb = os.path.getsize(file_path) / (1024**3)
    if size_gb > 2:
        print(f"ප්‍රමාණය {size_gb:.2f}GB - Google Drive වෙත යවයි...")
        os.system(f"rclone copy {file_path} gdrive:Movies/")
    else:
        print("Telegram වෙත යවයි...")
        # Telegram logic here
    # Telegram upload logic
