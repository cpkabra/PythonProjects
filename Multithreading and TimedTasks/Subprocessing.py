import subprocess, time

aotm_path = "/Users/neelpatel/Desktop/Atom.app/Contents/MacOS/Atom"
timer = int(input("Please enter the countdown time: "))

for i in range(timer, 0, -1):
    print(i)
    time.sleep(1)

subprocess.Popen(aotm_path)