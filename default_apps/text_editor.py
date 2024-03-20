def text_editor():
    global file
    import tkinter as tk
    from tkinter import messagebox, filedialog, Text, NSEW, Menu, END, N, S, E, W
    import os
    def createWidgets():
        global textArea
        textArea = Text(root)
        textArea.grid(sticky=NSEW)
        menuBar = Menu(root)
        root.config(menu=menuBar)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New", command=newFile)
        fileMenu.add_command(label="Open", command=openFile)
        fileMenu.add_command(label="Save", command=saveFile)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=root.destroy)
        menuBar.add_cascade(label="File", menu=fileMenu)
        editMenu = Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Cut", command=cut)
        editMenu.add_command(label="Copy", command=copy)
        editMenu.add_command(label="Paste", command=paste)
        menuBar.add_cascade(label="Edit", menu=editMenu)
    def newFile():
        global textArea
        root.title("Untitled - MuffinOS Text Editor")
        file = None
        textArea.delete(1.0, END)
    def openFile():
        global textArea
        file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents", "*.txt")])
        file = file.name
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - NanoMuffin")
            textArea.delete(1.0, END)
            file = open(file, "rb")
            textArea.insert(1.0, file.read())
            file.close()
    def saveFile():
        global textArea, file
        if file == None:
            try:
                file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents", "*.txt")])
            except FileNotFoundError:
                print("[Error]: No save path specified. File was not saved.")
            if file == None:
                file == None
            else:
                file = open(file, "w")
                file.write(textArea.get(1.0, END))
                file.close()
                file = file.name
                root.title(os.path.basename(file) + " - NanoMuffin")
        else:
            file = open(file, "w")
            file.write(textArea.get(1.0, END))
            file.close()
    def cut():
        global textArea
        textArea.event_generate("<<Cut>>")        
    def copy():
        global textArea
        textArea.event_generate("<<Copy>>")        
    def paste():
        global textArea
        textArea.event_generate("<<Paste>>")        
    root = tk.Tk()
    root.title("NanoMuffin Text Editor")
    file = None
    createWidgets()
    root.mainloop()