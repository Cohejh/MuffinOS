def pkg(inputs, cdir):
    import os
    import importlib.util
    print("MuffinOS Package Manager")
    print(" v1.0.0 (C) 2024 COHEJH ")
    if "--help" in inputs:
        print('''[Usage]: Install/Uninstall/Manages Packages
pkg install
    uninstall
    upgrade
    search
    load''')
    elif inputs[0] == "upgrade":
        print("[Info]: You have requested to upgrade to the full version of MuffinOS.")
        print("[Info]: This process requires admin permission to perform.")
        admin_permit = input("Do you wish to continue? (Y/N) ")
        if admin_permit.upper() == "Y":
            print("[Info]: Installing \"Progress\" Package")
            import os
            if os.name == "posix":
                os.system("sudo pip install progress &> /dev/null")
            else:
                os.system("pip install progress > nul")
            installed = importlib.util.find_spec("progress")
            if installed is None:
                print("[Error]: \"Progress\" could not be installed.")
                return
            print("[Info]: \"Progress\" installed successfully.")
            from progress.bar import IncrementalBar
            print("[Info]: Installing Packages...")
            bar = IncrementalBar('', max=5,  suffix='%(percent)d%%')
            if os.name == "posix":
                os.system("sudo pip install PyQt5 &> /dev/null")
                bar.next()
                os.system("pip install PyQtWebEngine &> /dev/null")
                bar.next()
                os.system("pip install wget &> /dev/null")
                bar.next()
                os.system("pip install py_cui &> /dev/null")
                bar.next()
            else:
                os.system("pip install PyQt5 > nul")
                bar.next()
                os.system("pip install PyQtWebEngine > nul")
                bar.next()
                os.system("pip install wget > nul")
                bar.next()
                os.system("pip install py_cui > nul")
                bar.next()
            pkgdir = (str(cdir).removesuffix("home") + "pkg/pkgs/")
            import wget
            wget.download("https://raw.githubusercontent.com/t1m3togr1nd/Tide/master/tide.py", pkgdir + "tide.py")
            bar.next()
            bar.finish()
            
            
            
        else:
            print("[Info]: Operation Cancelled.")
