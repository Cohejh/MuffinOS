def shell(username, path):
    import zipfile, shutil, sys, os
    current_dir = os.getcwd()
    current_dir = current_dir.removesuffix("\\\\shell").removesuffix("/shell").removesuffix("\\shell").removesuffix("//shell")
    sys.path.insert(1, (current_dir + "/default_apps") )
    from text_editor import text_editor
    sys.path.insert(2, (current_dir + "/pkg"))
    from pkg import pkg
    os.chdir(path + "/home")
    terminate = 0
    def size_conversion(bytes):
        final = bytes
        unit = 0
        while final >= 1024:
            final = final / 1024
            unit += 1
        sizes = ["b", "KB", "MB", "GB", "TB"]
        return (str(round(final, 2)) + sizes[unit])
    def relative_path(path):
        left_path = str(path).removeprefix(current_dir).removeprefix("\home").removeprefix("/home")
        if path == current_dir:
            return "/"
        elif (current_dir + "/home") not in path and (current_dir + "\home") not in path:
            return str(path).removeprefix(current_dir).replace("\\", "/")
        elif left_path == "":
            return "~"
        else:
            return "~/" + left_path.removeprefix("\\").replace("\\", "/")
    while terminate == 0:
        command = input(f"{username} ({relative_path(os.getcwd())}) $ ")
        split_cmd = command.split()
        # Quit Command
        if command == "quit":
            terminate = 1
        # Zip Command
        if split_cmd[0] == "zip":
            if "--help" in split_cmd:
                print("[Usage]: Zips a directory or folder\nzip <path to directory/folder> --output_name (optional) <output_name (optional)>\ne.g. zip ~/directory1/folder")
            else:
                try:
                    print("Zipping File...")
                    if "--output_name" in split_cmd:
                        output_filename = split_cmd[split_cmd.index("--output_name") + 1]
                    else:
                        output_filename = os.path.basename(os.path.normpath(split_cmd[1]))
                    shutil.make_archive(output_filename, 'zip', split_cmd[1])
                    print("File Zipped.")
                except FileNotFoundError:
                    print("[Error] The folder you specified could not be found. Are you sure you entered the path correctly, and this folder exists?")
        # Unzip Command
        if split_cmd[0] == "unzip":
            if "--help" in split_cmd:
                print("[Usage]: Unzips a .zip archive\nunzip <path to file> --output_name (optional) <output_name (optional)>\ne.g. unzip ~/directory1/file.zip")
            else:
                try:
                    print("Unzipping File...")
                    if "--output_name" in split_cmd:
                        output_filename = split_cmd[split_cmd.index("--output_name") + 1]
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
            if "--help" in split_cmd:
                print("[Usage]: Creates a file or folder\nnew --file/--folder <name>\ne.g. new --file example.txt")
            elif split_cmd[1] == "--file":
                try:
                    file = open(split_cmd[2],"x")
                    file.close()
                except FileExistsError:
                    print("[Error]: This file already exists! Please choose a different name or delete this file.")
            elif split_cmd[1] == "--folder":
                try:
                    os.mkdir(split_cmd[2])
                except FileExistsError:
                    print("[Error]: This folder already exists! Please choose a different name or delete this folder")
            else:
                print("[Error]: Flag \"" + split_cmd[1] + "\" is invalid. Are you sure you typed it correctly?")
        # Make a directory
        if split_cmd[0] == "mkdir":
            if "--help" in split_cmd:
                print("[Usage]: Creates a directory\nmkdir <name>\ne.f. mkdir myDirectory")
            else:
                try:
                    os.mkdir(split_cmd[1])
                except FileExistsError:
                    print("[Error]: This directory already exists! Please choose a different name or delete this directory")
        # Remove files/folders
        if split_cmd[0] == "rmv":
            if "--help" in split_cmd:
                print("[Usage]: Deletes a file or folder\nrmv <name>\ne.g. rmv example.txt")
            elif len(split_cmd) > 1:
                if os.path.isfile(split_cmd[1]) == True:
                    os.remove(split_cmd[1])
                else:
                    shutil.rmtree(split_cmd[1])
            else:
                print("[Error]: This file/folder does not exist. Are you sure you typed this command correctly")
        # Python Implementation
        if split_cmd[0] == "python":
            if "--help" in split_cmd:
                print("[Usage]: Runs python or a python script\npython <file (optional>\nee.g python script.py")
            elif len(split_cmd) > 1:
                try:
                    exec(open(split_cmd[1]).read())
                except:
                    print("[Error]: The file specified could not be found. Are you sure you typed it correctly?")
            else:
                try:
                    eval(os.system("python"))
                except TypeError:
                    print("[Python]: Closed Python. Resuming Terminal session.")
        # Text Editor
        if split_cmd[0] == "text":
            text_editor()
        # Change Directory
        if split_cmd[0] == "cd":
            active_dir = os.getcwd()
            try:
                if "--help" in split_cmd:
                    print("[Usage]: Changes the current directory\ncd -r (optional, enables root access) <path>\ne.g. cd MyDir")
                elif "-r" in split_cmd:
                    if split_cmd[2] == "/":
                        os.chdir(current_dir)
                    else:
                        os.chdir(current_dir + "/" + split_cmd[2])
                else:
                    if split_cmd[1] == "~":
                        os.chdir(current_dir + "/home")
                    else:
                        os.chdir(active_dir + "/" + split_cmd[1])
            except IndexError:
                print("[Error]: No path specified, please provide a path.")
            except FileNotFoundError:
                print("[Error]: This directory does not exist, are you sure you typed the name correctly?")
        # List Items
        if split_cmd[0] == "ldir":
            if "--help" in split_cmd:
                print("[Usage]: Lists all the items in the current working directory\nldir\ne.g. ldir")
            else:
                items = os.listdir()
                files = []
                folders = []
                files_size = 0
                folders_size = 0
                folders_count = 0
                for item in items:
                    if os.path.isfile(item):
                        files.append(item)
                        files_size = files_size + os.path.getsize(item)
                    else:
                        folders.append(item)
                        folders_size = folders_size + os.path.getsize(item)
                        folders_count += 1
                if files_size + folders_size == 0 and folders_count == 0:
                    print("This directory is currently empty.")
                else:
                    if files_size != 0:
                        print(f"Files ({size_conversion(files_size)} total size.):")
                        for file in files:
                            print(f"    {file} - {size_conversion(os.path.getsize(file))}")
                    if folders_size != 0:
                        print(f"Folders ({size_conversion(folders_size)} total size.):")
                        for folder in folders:
                            if os.path.getsize(folder) != 0:
                                print(f"    {folder} - {size_conversion(os.path.getsize(folder))}")
                            else:
                                print(f"    {folder} - Empty")
                    elif folders_size == 0 and folders_count != 0:
                        print(f"Folders:")
                        for folder in folders:
                            print(f"    {folder} - Empty")
        # Directory Info
        
        # PKG
        if split_cmd[0] == "tide":
            os.system("python C:/Users/jcohe/Desktop/MuffinOS/pkg/pkgs/tide.py")
        if split_cmd[0] == "pkg":
            pkg(["upgrade"], os.getcwd())
