﻿# Committer

## Descripción

This project is a CLI (Command Line Interface) tool to facilitate the creation of commits in Git following the “Conventional Commits” style, allowing the addition of emojis in the commit messages in a simple and fast way.
The tool interacts with the user to request information about the type of commit, the description, body and footer of the message, and then executes the commit with the generated message.

---

## Steps to create a virtual environment and run the tool

### 1. Create a directory and clone the repository

```
    git clone https://github.com/JoseLeviRivera/Committer.git
```

### 2. Create a virtual environment in python
En Windows:
```
   .\venv\Scripts\activate
```
En Linux/Mac:
```
   source venv/bin/activate
```

### 3. Install the necessary dependencies
Once the virtual environment is active, it installs all the dependencies required for the project. Instead of installing libraries one by one, we have a requirements.txt file that contains all the dependencies.
To install the dependencies, simply run:

```
   pip install -r requirements.txt
```

### 4. Generate a binary(Optionally)
Once the libraries are installed you can run the following command which will create a folder /dist with the name of a gcz file which is the name of the program tool in binary. 
```
   pyinstaller --onefile --name gcz main.py
```

### 5. Create a global command (gcz)
If you want to run the gcz command from any location on your system (without having to navigate to the executable directory), you can add the dist/ directory to your PATH environment variable. Here's how to do it: 
#### Linux/Mac:
1. Copy the executable file to a directory such as /usr/local/bin: 
```
  sudo cp dist/gcz /usr/local/bin/
```
2. Make sure the file has execute permissions:
```
 sudo chmod +x /usr/local/bin/gcz
```
#### In Windows:
You can install `gcz` automatically via PowerShell, or manually if you prefer.

##  Automatic Installation via PowerShell

### 1. Open PowerShell as Administrator

- Press `Windows` key, type **PowerShell**.
- Right-click on **Windows PowerShell** and select **Run as administrator**.

### 2. Allow script execution (one-time setup)

Run this command to allow script execution:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
### 3. Verify installation
```powershell
gcz --help
```

3. You will now be able to run `gcz` from any Windows terminal.

### Warning about creating the executable:

- **External dependencies**: If your script uses external libraries, make sure they are included correctly. `PyInstaller` generally handles this well, but in some cases it may be necessary to specify additional paths for some libraries. Make sure all dependencies are correctly configured in your virtual environment before creating the executable.

- Cross-operating system compatibility**: If you need to generate executables for different operating systems from a single machine (e.g. for both Windows and Linux), we recommend using a **virtual machine** or **Docker**. This way, you can compile the executable in the specific environment of each operating system, ensuring that they work correctly.

These points ensure that the process of creating executables is easier and that your tool is compatible with different platforms.
