def text_editor(**kwargs):
    file_path = kwargs.get('path', None)
    import tkinter as tk
    from tkinter import messagebox, filedialog, Text, NSEW, Menu, END
    import os
    def createWidgets():
        global textArea
        textArea = Text(root)
        textArea.grid(sticky=NSEW)
        menuBar = Menu(root)
        root.config(menu=menuBar)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New", command=newFile)
        fileMenu.add_command(label="Open", command="")
        fileMenu.add_command(label="Save", command="")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=root.destroy)
        menuBar.add_cascade(label="File", menu=fileMenu)
        editMenu = Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Cut", command="")
        editMenu.add_command(label="Copy", command="")
        editMenu.add_command(label="Paste", command="")
        menuBar.add_cascade(label="Edit", menu=editMenu)
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About MuffinOS Text Editor", command="")
        menuBar.add_cascade(label="Help", menu=helpMenu)
        
    def newFile():
        global textArea
        root.title("Untitled - MuffinOS Text Editor")
        file = None
        textArea.delete(1.0, END)
    
    
        
    root = tk.Tk()
    root.title("MuffinOS Text Editor")
    file = None
    createWidgets()
    root.mainloop()