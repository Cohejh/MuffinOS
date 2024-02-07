def shell(username):
    import zipfile
    import shutil
    import os
    terminate = 0
    while terminate == 0:
        command = input(username + " $ ")
        split_cmd = command.split()

        # Quit Command
        if command == "quit":
            terminate = 1

        # Zip Command
        if split_cmd[0] == "zip":
            if split_cmd[1] == "--help":
                print("[Usage]: Zips a directory or folder\nzip <path to directory/folder> --output_name (optional) <output_name (optional)>\ne.g. zip ~/directory1/folder")
            else:
                try:
                    print("Zipping File...")
                    if len(split_cmd) >= 3 and split_cmd[2] == "--output_name":
                        output_filename = split_cmd[3]
                    else:
                        output_filename = os.path.basename(os.path.normpath(split_cmd[1]))
                    shutil.make_archive(output_filename, 'zip', split_cmd[1])
                    print("File Zipped.")
                except FileNotFoundError:
                    print("[Error] The folder you specified could not be found. Are you sure you entered the path correctly, and this folder exists?")

        # Unzip Command
        if split_cmd[0] == "unzip":
            if split_cmd[1] == "--help":
                print("[Usage]: Unzips a .zip archive\nunzip <path to file> --output_name (optional) <output_name (optional)>\ne.g. unzip ~/directory1/file.zip")
            else:
                try:
                    print("Unzipping File...")
                    if len(split_cmd) >= 3 and split_cmd[2] == "--output_name":
                        output_filename = split_cmd[3]
                    else:
                        output_filename = split_cmd[1].split(".")
                    shutil.unpack_archive(split_cmd[1], output_filename[0])
                    print("File Unzipped.")
                except FileNotFoundError:
                    print("[Error] The file you specified could not be found. Are you sure you entered the path correctly, and this file exists?")
                except shutil.ReadError:
                    print("[Error] The file you specified could not be found. Are you sure you entered the path correctly, and this file exists?")
        
        # Create files/folders
        if split_cmd[0] == "new":
            if split_cmd[1] == "--help":
                print("[Usage]: Creates a file or folder\nnew --file/--folder <name>\ne.g. new --file example.txt")
            if split_cmd[1] == "--file":
                try:
                    file = open(split_cmd[2],"x")
                    file.close()
                except FileExistsError:
                    print("[Error]: This file already exists! Please choose a different name or delete this file.")
            if split_cmd[1] == "--folder":
                try:
                    os.mkdir(split_cmd[2])
                except FileExistsError:
                    print("[Error]: This folder already exists! Please choose a different name or delete this folder")
