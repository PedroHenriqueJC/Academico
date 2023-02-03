import os
def criar_arquivos():

    user_f = open("user.txt","r")
    curso = user_f.read().split("\n")

    if curso[-1] == "TIPI":
        materia_f = open("materia_tipi.txt","r")
        materias = materia_f.read().split("\n")
    elif curso[-1] == "MA":
        materia_f = open("materia_ma.txt","r")
        materias = materia_f.read().split("\n")
    elif curso[-1] == "ADM":
        materia_f = open("materia_adm.txt","r")
        materias = materia_f.read().split("\n")
    elif curso[-1] ==  "EDF":
        materia_f = open("materia_edf.txt","r")
        materias = materia_f.read().split("\n")
    

    for i in range(0, len(materias)-1):
        try:
            arquivo = open("{}.txt".format(materias[i]),"x")
        except:
            pass
        else:
            arquivo.close
            arquivo = open("{}.txt".format(materias[i]),"w")
            arquivo.write("0")
            arquivo.close


criar_arquivos()