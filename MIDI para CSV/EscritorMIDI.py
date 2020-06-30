import subprocess

notes = {'1':60,
        '2':62,
        '3':64,
        '4':65,
        '5':67,
        '6':69,
        '7':71,
        'q':72,
        'w':74,
        'e':76,
        'r':77,
        't':79,
        'y':81,
        'u':83,
        '0': 0
        }

parte1 = ['5','6','7','w','w','7','q','q','0']
parte2 = ['5','6','7','w','w','q','7','0']
parte3 = ['5','5','6','7','w','0','w','q','7','5','q','0']
parte4 = ['7','7','6','6','7','0','6','6','5','5']
parte5 = ['r','w','e','q','w','7','q','6','7','5','6','5','3','5','5','0']

asaBranca = []
asaBranca.extend(parte1)
asaBranca.extend(parte2)
asaBranca.extend(parte3)
asaBranca.extend(parte4)
asaBranca.extend(parte3)
asaBranca.extend(parte4)
asaBranca.extend(parte5)
asaBranca.extend(parte5)

parte1 = ['7','7','q','w','w','q','7','6','5','5','6','7']
parte2 = ['7','6','6','0']
parte3 = ['6','5','5','0']
parte4 = ['6','6','7','5']
parte5 = ['6','7','q','7','5']
parte6 = ['6','7','q','7','6','5','6','2']
parte7 = ['6','5','5']

sinfonia = []
sinfonia.extend(parte1)
sinfonia.extend(parte2)
sinfonia.extend(parte1)
sinfonia.extend(parte3)
sinfonia.extend(parte4)
sinfonia.extend(parte5)
sinfonia.extend(parte6)
sinfonia.extend(parte1)
sinfonia.extend(parte7)

nomeArq = input("Insira o nome do arquivo: ")
arq = open(nomeArq+".csv","w+") 
tempo = 480
inc = 240
fim = True

# Cabeçario minimo para escrever
arq.write("0, 0, Header, 1, 2, 480\n")
arq.write("1, 0, Start_track\n")
arq.write("1, 90242, End_track\n")
arq.write("2, 0, Start_track\n")
arq.write("2, 0, Title_t, Piano right\n")
arq.write("2, 0, Program_c, 0, 0\n")
arq.write("2, 0, Control_c, 0, 7, 100\n")
arq.write("2, 0, Control_c, 0, 10, 64\n")
arq.write("2, 0, Control_c, 0, 91, 127\n")

while(fim):
    print("Insira a nota desejada ou se deseja passar para o proximo tempo:\n")
    note = input("0 - pula nota\n1 - do\n2 - re\n3 - mi\n4 - fa\n5 - sol\n6 - la\n7 - si\nq - do#\nw - re#\ne - mi#\nr - fa#\nt - sol#\ny - la#\nu - si#\nQualquer outro valor e acaba a música\n")
    
    if note in notes:
        line = "2, " + str(tempo) + ", Note_on_c, 0, " + str(notes[note]) +", 36\n"
        arq.write(line)
        tempo += inc
        line = "2, " + str(tempo) + ", Note_on_c, 0, " + str(notes[note]) +", 0\n"
        arq.write(line)
    elif note == 'asa':
        for i in asaBranca:
            line = "2, " + str(tempo) + ", Note_on_c, 0, " + str(notes[i]) +", 36\n"
            arq.write(line)
            tempo += inc
            line = "2, " + str(tempo) + ", Note_on_c, 0, " + str(notes[i]) +", 0\n"
            arq.write(line)
        break
    elif note == 'sin':
        for i in sinfonia:
            line = "2, " + str(tempo) + ", Note_on_c, 0, " + str(notes[i]) +", 36\n"
            arq.write(line)
            tempo += inc
            line = "2, " + str(tempo) + ", Note_on_c, 0, " + str(notes[i]) +", 0\n"
            arq.write(line)
        break
    else:
        fim = False
        tempo += inc
        
line = "2, " + str(tempo + inc) + ", End_track\n"
arq.write(line) 
line = "0, 0, End_of_file"
arq.write(line) 

arq.close()

command = ".\Csvmidi.exe " + nomeArq + ".csv " + nomeArq + ".mid "
subprocess.run(command)

