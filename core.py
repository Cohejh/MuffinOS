import os
import sys
import socket
config = open("settings.muffinconfig", '+r')
settings = config.readlines()
current_dir = os.getcwd()
if settings[5] == "yes\n":
    print("Starting OS")
    print("OS is running in \""+ current_dir + "\".")
    print("\n\n\n\n")
shell_path = current_dir + "/shell"
sys.path.insert(0, shell_path)
from shell import shell
user = os.getlogin() + "@" + socket.gethostname()
shell(user)
print("\n")
print("Shutting down...")
print("Thank you for using MuffinOS")