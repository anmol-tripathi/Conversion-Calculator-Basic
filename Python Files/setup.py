#setup.py
#To create executable run ' python setup.py build '
#To create setup msi file run ''
import cx_Freeze
import sys
import tkinter
from PIL import Image, ImageTk
import tkinter.font as font
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("app.py", base=base, icon="app.ico")]

cx_Freeze.setup(
    name = "Conversion-App",
    options = {"build_exe": {"packages":["tkinter"], "includes":["tkinter"], "include_files":["ico/area.png","ico/convert.png","ico/len.png","ico/temp.png","ico/vol.png","ico/wght.png"]}},
    version = "0.01",
    description = "Conversion App",
    executables = executables
    )