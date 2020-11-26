import cx_Freeze

executables = [cx_Freeze.Executable(script="game_main.py",icon="assets/abc.ico")]
cx_Freeze.setup(
    name="Abecedário",
    options={"build_exe": {"packages":["pygame"],
                            "include_files":["assets","game_functions.py"]}},
 executables = executables
 ) 
