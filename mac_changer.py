import subprocess
import optparse

inteface = input("Enter Your Interface > ")
new_mac = input("Enter Your New Mac > ")

subprocess.call("ifconfig" + inteface + "down")
subprocess.call("ifconfig" + inteface + "hw" + "ether" + new_mac)
subprocess.call("ifconfig" + inteface + "up")
print("Successfully Chaged Your Mac To > " + new_mac)