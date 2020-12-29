import cx_Freeze
import sys
import traceback
import os

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("gui2.py", base=base, icon="connectfor_logo.ico")]

cx_Freeze.setup(
    name = "Auto-message",
    options = {"build_exe": {"packages":["tkinter","selenium","pandas","numpy","autoit","argparse","os","traceback"], "include_files":["connectfor_logo.ico"]}},
    version = "0.01",
    description = "Send message automatically",
    executables = executables
    )