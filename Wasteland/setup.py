from cx_Freeze import setup, Executable
import sys
 
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.
 
executables = [Executable("C:\\Users\\Caeta\\Downloads\\Desktop\\Senac Ensino Médio\\Matérias\\Técnico Profissionalizante\\Python\\Projetos\\Wasteland\\GUI Wasteland\\Wasteland2.0_GUI.py", base=base)]
 
packages = ["tkinter", "time", "random", "os", "pygame","PIL"]
files = ["C:\\Users\\Caeta\\Downloads\\Desktop\\Senac Ensino Médio\\Matérias\\Técnico Profissionalizante\\Python\\Projetos\\Wasteland\\GUI Wasteland\\pistol.png", "C:\\Users\\Caeta\\Downloads\\Desktop\\Senac Ensino Médio\\Matérias\\Técnico Profissionalizante\\Python\\Projetos\\Wasteland\\GUI Wasteland\\The_Last_Of_us_Theme_song.mp3"]
options = {
    'build_exe': {
 
        'packages':packages,
        'include_files': files,
    },
 
}
 
setup(
    name = "Wasteland",
    options = options,
    version = "1.0",
    description = 'Trabalho: Jogo em Python',
    executables = executables
)