import os
import time
import subprocess

# OnStream App එක විවෘත කිරීම
os.system("adb shell monkey -p com.onstream.app -c android.intent.category.LAUNCHER 1")
time.sleep(20)

# Movies ටැබ් එකට යාම
os.system("adb shell input tap 300 1500") 
time.sleep(5)

# Filter open කිරීම
os.system("adb shell input tap 950 150")
time.sleep(5)

# Submit button එක ක්ලික් කිරීම
os.system("adb shell input tap 500 1800")
time.sleep(10)

# පළමු result එක තේරීම
os.system("adb shell input tap 300 500")
time.sleep(10)

# Download ලින්ක් එක ලබාගෙන ඩවුන්ලෝඩ් කිරීම (උදාහරණයක් ලෙස)
url = "DOWNLOAD_URL_HERE" # මෙහිදී logcat හරහා url එක ලබාගැනීම ස්වයංක්‍රීයව සිදුවේ
os.system(f"aria2c -x 16 -s 16 '{url}' -o movie.mp4")

# ප්‍රමාණය පරීක්ෂා කර Drive එකට යැවීම
size_gb = os.path.getsize("movie.mp4") / (1024**3)

if size_gb > 2:
    print("2GB ට වැඩියි - Google Drive එකට යවනවා...")
    os.system("rclone copy movie.mp4 gdrive:Movies/")
else:
    print("2GB ට අඩුයි - Telegram එකට යවනවා...")
    # Telegram upload logic
