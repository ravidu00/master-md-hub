import os
import time
import subprocess

def run_adb(command):
    subprocess.run(f"adb {command}", shell=True)

print("Starting OnStream Bot...")
# ඇප් එක විවෘත කිරීම
run_adb("shell monkey -p com.onstream.app -c android.intent.category.LAUNCHER 1")
time.sleep(15)

# Movies අංශයට යාම (පින්තූරය අනුව)
run_adb("shell input tap 540 2000") 
time.sleep(5)

# Filter සහ All Time තේරීම
print("Filtering movies...")
run_adb("shell input tap 900 150") # Filter icon
time.sleep(2)
run_adb("shell input tap 300 800") # All Time option
run_adb("shell input tap 540 1800") # Submit button

time.sleep(10)
# මූවී එක ඩවුන්ලෝඩ් කර ප්‍රමාණය පරීක්ෂා කිරීම (Logic)
file_size_gb = 2.5 # මෙය උදාහරණයක් ලෙස, ඇත්තටම බොට් මෙය පරීක්ෂා කරයි

if file_size_gb > 2:
    print("Size > 2GB. Uploading to Google Drive...")
    os.system("rclone copy movie.mp4 gdrive:Movies -P")
else:
    print("Size < 2GB. Sending to Telegram...")
    # Telegram upload logic here using TG_TOKEN
