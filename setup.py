import cx_Freeze

# base = "Win32GUI" allows your application to open without a console window
executables = [cx_Freeze.Executable('principal.py', base = "Win32GUI", target_name = 'Escondida', icon = 'resources/img/icon.png')]

cx_Freeze.setup(
    name = "My Example Exe App",
    options = {"build_exe" : 
        {"packages" : ["pygame"], "include_files" : ['principal.py', 'extras.py', 'funcionesVACIAS.py' , 'configuracion.py', 'lemario.txt', 'records.txt', 'puntajes.txt', 'resources']}},
    executables = executables
)