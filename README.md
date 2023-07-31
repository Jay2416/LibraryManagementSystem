
# Library Management System 📚

This project's objective is to develop a MIS system with a user friendly GUI interface.

This software project also aims to improve the existing record keeping system, which will assist managers in retrieving the most recent information at the appropriate time and in the appropriate manner.


## Tech Stack 👨‍💻

- Front-End: Python (tkinter for GUI) 🐍
- Back-End: MySQL 📑
## Features ✨

- Both employee and customer can access to the database and work accordingly.
- Deleteed records are also being stored to retrieve it for future use.


## Modules Used 💻

- **tkinter** - to create GUI
- **random** - to get the random numbers and choices
- **time** - to fetch the time
- **datetime** - to fetch the date and time
- **getpass** - to hide the password for security purpose
- **mysql.connector**, to install it, use the following command on your command prompt. You can use an alternative module **pymysql** to is getting an error while importing it.

```bash
pip install mysql-connector
pip install pymysql
```


## Event Bindings ⛓️

The most important part to make a better GUI is to learn the event binding process. The most used key bindings in tkinter with their uses are:

|Event Key | Key Binded |
|----------|------------|
|Button-1  |Single left click |
|Button-3  |Single right click |
|Return    |Enter key |
|ButtonRelease|Release mouse button |
|Enter     |Mouse cursor entering in the widget |
|Double-Button-1  |Double left click |
|Double-Button-3  |Double right click |
|Leave |Mouse cursor leaving the widget |


## How to convert .py to .exe 🔀

By converting into a executable file, you can run this program on any computer irrespective the system has python installed or not. 

You can convert this project(.py) into a executable file(.exe) by following the steps mentioned: 

- Open the command prompt and run command given below.
- First command to make both.exe file with MicroSoft Installer(MSI) setup. 
- Second command to make only .exe file.
```bash
setup.py bsdit_msi
setup.py build
```

**Note:** 
- All the files must be in the same directory.
- CX_Freeze module must be installed. To install it write the following command on your command prompt.

```bash
pip install cx_freeze
```
## Installation of setup file(.msi) ⏬

- Open the setup file.
- Select the directory, make sure that a folder is been selected where you install the software
- Click on Install and the Notepad will be successfully installed.

