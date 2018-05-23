# generate_source_page.py
import os
import datetime


# meta
project_name = "__PROJEKTNAME__"
project = "== [[Projects/{}]] ==".format(project_name)
version = "1.0.0 {}".format(datetime.date.today())
file_types = [".py", ".csv"]


# script
files = [file for file in os.listdir() if os.path.isfile(file) and "." + file.rsplit(".", 1)[1] in file_types]

# TUI - die while Schleife ist nötig,
# so dass der Benutzer entscheiden kann,
# ob er alle Dateien erfasst sehen möchte
while files:
    for i, file in enumerate(files, 1):
        print("{:3d} -- {}".format(i, file))
       
    number = input("Do you want to remove a file? (e = break) ")

    if number == "e" or number == "" :
        print("\n\n")
        break
    else:
        files.pop(int(number) - 1)

# Der eigentliche Vorgang, um eine Seite für den Source Code des Programms zu erzeugen
if files:

    print(";{}".format(project))
    print("<tt>Version: {}</tt>".format(version))
    print("[[Kategorie:__Bereich__|__PFAD__]]")

    print("= Quelldateien =")
    
    for file in files:

        print("== {} ==".format(file))

        with open(file, encoding="utf-8") as f:
            code_lines = f.readlines()

        print("{} Codezeilen".format(len(code_lines)))

        print("<source lang='python'>")
        for code_line in code_lines:
            print(code_line.replace("\n", ""))
        print("<source>\n")

input("\n\n>>> Fertig!")
