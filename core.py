import os
import sys
import socket
import urllib.request
config = open("settings.muffinconfig", '+r')
settings = config.readlines()
current_dir = os.getcwd()
if settings[7] == "yes\n":
    print("Checking for updates...")
    current_version = settings[5].removesuffix("\\n")
    current_version_comparable = int(current_version.split(".")[0] + current_version.split(".")[1] + current_version.split(".")[2])
    url = "https://raw.githubusercontent.com/Cohejh/MuffinOS/backend/latest.update"
    update_query_request = urllib.request.Request(url)
    update_query_reply = urllib.request.urlopen(update_query_request)
    update_query = update_query_reply.readlines()
    latest_version = str(update_query[0]).removeprefix("b'").removesuffix("\\n'")
    latest_version_comparable = int(latest_version.split(".")[0] + latest_version.split(".")[1] + latest_version.split(".")[2])
    if settings[5] == "yes\n":
        print("Latest version is " + latest_version)
        print("Installed version is " + current_version)
    if latest_version_comparable > current_version_comparable:
        print("Update Avaliable!")
    else:
        print("No avaliable updates found.")
shell_path = current_dir + "/shell"
sys.path.insert(0, shell_path)
from shell import shell
user = os.getlogin() + "@" + socket.gethostname()
shell(user, current_dir)