import subprocess
import time
import random

os.system("figle MAC CHANGER")

inteface = input("Enter Your Interface > ")
new_mac = input("Enter Your New Mac > ")

print("-" * 50)
time.sleep(5)
print("Chainging Your Mac Address...")
time.sleep(5)
print("-" * 50)
time.sleep(5)
subprocess.call("ifconfig" + inteface + "down")
subprocess.call("ifconfig" + inteface + "hw" + "ether" + new_mac)
subprocess.call("ifconfig" + inteface + "up")
print("Successfully Chaged Your Mac To > " + new_mac)
