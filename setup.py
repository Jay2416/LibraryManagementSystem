import cx_Freeze
import os
import sys
base=None

if sys.platform=="win32":
    base="Win32GUI"

os.environ["TCL_LIBRARY"]=r"C:\Users\Hp\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
os.environ["Tk_LIBRARY"]=r"C:\Users\Hp\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"

executables= [cx_Freeze.Executable("library management.py", base=base, icon="icons\\library icon.ico")]

cx_Freeze.setup(
    name="Library Management System",
    options={"build_exe" : {"packages":["tkinter", "getpass", "random", "time", "datetime", "mysql.connector", "os"], "include_files":["feedback.txt", "icons", "books", "tcl86t.dll", "tk86t.dll"]}},
    version="2.4.16",
    description="Library Management System - Jay and Harsh",
    executables=executables
)

