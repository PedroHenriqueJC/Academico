import time
import random
import os
from datetime import datetime

meses_tu = ['01','03','05','07','08','10','12']
meses_s_tu = ['04','06','09','11']

caracteres_especiais = ["@","$","-","_","!","#","%","¨","&","*","(",")","+","=","§","{","[","ª","´","`", "^","~","}","]","<",",",">",".",";",":","|","?","/","'"]
carac_espc_str = "".join(caracteres_especiais)
algarismos = ["0","1","2","3","4","5","6","7","8","9"]
algarismos_str = "".join(algarismos)
acentos = ['à','á','â','é','í','õ','ã','ê',"ô"]


cursos = ['MA', 'TIPI', 'ADM', 'EDF']

mes = time.strftime('%m', time.localtime()) #captura o mes atual para checar se ele fez ou não aniversario para usar no argumento idade, para ver se a idade corresponde aos requisitos
ano = time.ctime() #Capturando a data atual pela biblioteca time
ano = ano.split() #Convertendo o string da data atual para lista

mes = datetime.now().month

#Implementação apos a apresentação: Usuário ter acesso à seus dados, como cpf, email, etc

def criar_arquivos():
    cpf_f = open("cpf.txt","a")
    email_f = open("email.txt","a")
    matricula_f = open("matricula.txt","a")
    nascimento_f = open("nascimento.txt","a")
    nome_f = open("nome.txt","a")
    senha_f = open("senha.txt","a")

    cpf_f.close()
    email_f.close()
    matricula_f.close()
    nascimento_f.close()
    nome_f.close()
    senha_f.close()

    for i in range(0, len(cursos)):
        try:
            arquivo = open("materia_{}.txt".format(cursos[i].lower().strip()),"x")
        except:
            pass

def cadastro():
    global nome
    global cpf
    global nascimento
    global email
    global curso
    global senha
    global matricula_final
    nome = str(input("Digite seu nome: "))
    while validar_nome() == False: #nome.strip().isalnum() Para evitar entradas com números, usando o strip pois se houver espaço ele não considera como número(Por exemplo: Pedro 1)
        nome = str(input("Entrada inválida!\nDigite seu nome: "))
    cpf = str(input("Digite seu CPF(sem pontos ou traços): "))
    while validar_cpf() == False:
        cpf = str(input("Entrada inválida!\nDigite seu CPF(sem pontos ou traços): "))
    nascimento = str(input("Digite seu nascimento(DD MM YYYY): "))
    while validar_nascimento() == False:
        nascimento = str(input("Entrada inválida!\nDigite seu nascimento(DD MM YYYY): "))
        
    email = str(input("Digite seu email: "))
    while validar_email() == False:
        email = str(input("Email inválido!\nDigite seu email: "))
    curso = str(input("Digite seu curso(MA, TIPI, ADM ou EDF): "))
    curso.strip().upper()
    while validar_curso() == False:
        curso = str(input("Entrada inválida.\n Digite seu curso(MA, TIPI, ADM ou EDF): "))
        curso.strip().upper()
        
    matricula_final = gerar_matricula(curso)
    senha = str(input("Digite sua senha(Somente números e letras): "))
    while validar_senha() == False:
        senha = str(input("Entrada inválida! Digite sua senha(Somente números e letras): "))



def validar_nome(): 
    global nome
    for i in range(0, len(nome)): #Percorrendo a varíavel nome e checando se os seus dígitos são algarismos númericos, caso sejam, apresenta erro
        if nome[i] in algarismos_str:
            return False
    if len(nome)<3: #Não permite um nome menor que 3 digitos
        return False
    else:
        return True

def validar_cpf():
    global cpf
    cpf = str(cpf)
    if len(cpf) != 11: #Verificando se o cpf tem 11 dígitos
        return False

    cpf_f = open("cpf.txt","r")
    cpfs = cpf_f.read().split(",")
    #cpfs = cpfs.pop(-1)

    #print(cpfs)
    for i in range(0, len(cpfs)):
        if str(cpf) == str(cpfs[i]):
            print("Cpf já cadastrado!")
            return False

def validar_nascimento():
    global nascimento
    l_nascimento = [] #Criando uma lista l_nascimento para armazenar dados temporários
    l_nascimento.clear() #Limpando a lista
    l_nascimento.extend(nascimento.split()) #Colocando os dados passados do nascimento dentro da lista
    if len(l_nascimento) < 3: #Como os dados passados tem que ser no formato (DD MM YYYY) caso o tamanho da lista seja menor que 3 o usuário passou os dados de forma errada
        return False
        
    if int(l_nascimento[1]) < int(mes): #Se o mês do nascimento for menor que o mês atual o usuário ja fez aniversário
        idade = (int(ano[4]) - int(l_nascimento[2])) #Passando sua variável idade de acordo com o IF proposto
    elif int(l_nascimento[1]) == int(mes) and int(l_nascimento[0]) <= int(ano[2]): #Se os meses forem iguais porém o dia de nascimento for menor que o dia atual o usuário ja fez aniversário
        idade = (int(ano[4]) - int(l_nascimento[2])) #Passando sua variável idade de acordo com o IF proposto
    else:
        idade = (int(ano[4]) - int(l_nascimento[2])) - 1 #Considerando o else sabemos que o usuário não fez aniversário por isso descontamos um na sua idade
    
    if idade > 17 or idade < 14: #Verificando se a idade do usuário atende aos requisitos
        print("Entrada inválida!O usuário não atende os requisitos de idade(Entre 14 e 17 anos)")
        return False 
            
    if int(l_nascimento[2]) > int(ano[4]) or int(l_nascimento[2]) < 1 or len(l_nascimento[2]) != 4 or int(l_nascimento[1]) > 12 or int(l_nascimento[1]) < 1 or len(l_nascimento[1]) != 2 or len(l_nascimento[0]) != 2: #Verificando a passagem dos dados na forma pedida(DD MM YYYY) e verificando casos de meses maior que 12 ou menores que 1 e anos maiores que o ano atual ou menores que 1
        return False

    if(l_nascimento[1] in meses_s_tu): #Se o mês estiver na lista de meses sem 31 ele checara se o dia for maior que 30 ou menor que 1 encontrará um erro
        if int(l_nascimento[0]) > 30 or int(l_nascimento[0]) < 1:
            return False
    elif(l_nascimento[1] in meses_tu): #Se o mês estiver na lista de meses com 31 ele checara se o dia for maior que 31 e menor que 1 e encontrará um erro
        if int(l_nascimento[0]) > 31 or int(l_nascimento[0]) < 1:
            return False
    elif l_nascimento[1] == '02': #Se o mês for 2
        if int(l_nascimento[2]) % 4 == 0: #Se o ano for divisivel exato por 4 isso quer dizer que ele é bi-sexto, logo se o dia for maior que 29 e menor que 1 encontrará um erro
            if int(l_nascimento[0]) > 29 or int(l_nascimento[0]) < 1:
                return False
        else: #Se o ano não for divisivel exato po 4 ele encontrará um erro caso o dia seja maior que 28 e menor que 1
            if int(l_nascimento[0]) > 28 or int(l_nascimento[0]) < 1:
                return False
    nascimento_redigitado = str(l_nascimento[0]) + "/" + str(l_nascimento[1]) + "/" + str(l_nascimento[2]) #Concatenando o nascimento visando deixar mais bonito para mostrar ao usuário
    return nascimento_redigitado

def validar_email():
    global email
    if not("@outlook.com" in email or "@hotmail.com" in email or "@gmail.com" in email or "@outlook.com.br" in email): #Verificando a existencia de dominios no email indicado
        return False

    email_f = open("email.txt","r")
    emails = email_f.read().split(",")
    #emails = emails.pop(-1)

    for i in range(0, len(emails)):
        if str(email) == str(emails[i]):
            print("Email já cadastrado")
            return False


def validar_curso():
    global curso
    
    if not(curso in cursos): #Verificando se o curso digitado é um dos cursos válidos
        return False
    else:
        return True

def gerar_matricula(curso):
    final_matricula = [] #Lista temporária
    matricula_f = open("matricula.txt","r")
    matriculas = matricula_f.read().split(",")
    matriculas = matriculas.pop(-1)

    for i in range(0, 4): #Gerando os números aleatórios da matricula
        r = random.randint(0,9)
        final_matricula.append(r) #Colocando os números dentro da lista




    matricula = str(ano[4])+ str(curso) +str(final_matricula) #Concatenando ano + curso + números da matricula
    
    for i in range(0, len(matriculas)): #Impedindo que tenha uma mátricula com o final igual a outra
        if matricula == matriculas[i]:
            check = False
    else:
        check = True

    while not check:
        for i in range(0, 4): #Gerando os números aleatórios da matricula
            r = random.randint(0,9)
            final_matricula.append(r) #Colocando os números dentro da lista

        for i in range(0, len(matriculas)):
            if matricula == matriculas[i]:
                check = False
        else:
            check = True
        final_matricula = str(final_matricula[0])  + str(final_matricula[1]) + str(final_matricula[2]) + str(final_matricula[3]) #Concatenando os números gerados
        if int(mes) > 6:
            matricula = str(ano[4])+ "2" + str(curso) +str(final_matricula) #Concatenando ano + curso + números da matricula
        else:
            matricula = str(ano[4])+ "1" + str(curso) +str(final_matricula) #Concatenando ano + curso + números da matricula
        
    final_matricula = str(final_matricula[0])  + str(final_matricula[1]) + str(final_matricula[2]) + str(final_matricula[3]) #Concatenando os números gerados
    if int(mes) > 6:
        matricula = str(ano[4])+ "2" + str(curso) +str(final_matricula) #Concatenando ano + curso + números da matricula
    else:
        matricula = str(ano[4])+ "1" + str(curso) +str(final_matricula) #Concatenando ano + curso + números da matricula
        
    return matricula



def validar_senha():
    if carac_espc_str in senha: #Verificando se não foi passado caracteres especiais indesejados, exceto o "\"
        return False
    elif len(senha) < 4: #Verificando o tamanho da senha
        return False
    else:
        return True



def finalizar_matricula(nome, cpf, nascimento, email, curso):
    
    #Abrindo os arquivos de texto
    cpf_f = open("cpf.txt","a")
    email_f = open("email.txt","a")
    matricula_f = open("matricula.txt","a")
    nascimento_f = open("nascimento.txt","a")
    nome_f = open("nome.txt","a")
    senha_f = open("senha.txt","a")

    #Gravando os dados nos arquivos
    cpf_f.write("{},".format(str(cpf)))
    nome_f.write("{},".format(nome))
    nascimento_f.write("{},".format(nascimento))
    email_f.write("{},".format(email))
    matricula_f.write("{},".format(matricula_final))
    senha_f.write("{},".format(senha))
    #Fechando os arquivos
    cpf_f.close()
    email_f.close()
    matricula_f.close()
    nascimento_f.close()
    nome_f.close()
    senha_f.close()

    #Copiando/criando os arquivos necessários para o funcionamento do sistema.


    curso_materia = curso.lower()

    os.makedirs('./Users/{}'.format(matricula_final))
    os.system("copy pastas.py Users\{}".format(matricula_final))
    os.system("copy materia_{}.py Users\{}".format(curso_materia, matricula_final))

    user_f = open("user.txt","w")
    user_f.write("{}\n{}\n{}\n{}\n{}\n{}".format(nome, cpf, nascimento, email, matricula_final, curso))
    user_f.close()
    os.system("copy user.txt Users\{}".format(matricula_final))
    os.system("del user.txt")

    print("\n","-"*20, "\nUsuário cadastrado!\nNome:{}\nCPF:{}\nData de Nascimento:{}\nEmail:{}\nMatrícula:{}\n".format(nome, cpf, validar_nascimento(), email, matricula_final) ,"-"*20,"\n")


def login_matricula():
    global index_matricula, session_matricula
    
    matriculalogar = matricula_login.strip().upper()

    matricula_f = open("matricula.txt","r") #Abrindo o arquivo no formato read
    matriculas_cadastradas = matricula_f.read().split(",") #lendo o arquivo e o transformando em lista
    if matriculalogar in matriculas_cadastradas: #Caso a matricula informada esteja na lista de matriculas cadastradas
        index_matricula = matriculas_cadastradas.index(matriculalogar) #Captura o index da matricula na lista de matriculas cadastradas
        session_matricula = matriculalogar
        return True
    else:
        return False



def login_senha():
    senhas_f = open("senha.txt","r") #Abrindo o arquivo de senhas no formato read
    senhas_cadastradas = senhas_f.read().split(",") #Lendo o arquivo e o transformando em lista
    matricula_f = open("matricula.txt","r") #Abrindo o arquivo no formato read
    matriculas_cadastradas = matricula_f.read().split(",") #lendo o arquivo e o transformando em lista

    matriculalogar = matricula_login.strip().upper()
    senhalogar = senha_login.strip().upper()

    index_matricula = matriculas_cadastradas.index(matriculalogar)
    if str(senhas_cadastradas[index_matricula]) == str(senhalogar): #Se a senha digitada for igual a senha do index da matricula passada permite o login(cada matricula e senha detém o mesmo index, ou seja, a senha e a matricula do mesmo index devem combinar com a senha e o login digitado para que a entrada seja permitida)
        return True
    elif str(senha_login).strip() == str("0"):
        return False
    else:
        return False

def cadastrar_materia_tipi(materia):
    materia_split = materia.split(" ")
    materia_f = open("materia_tipi.txt","a")
    for i in range(0, len(materia)): #Percorrendo a varíavel nome e checando se os seus dígitos são algarismos númericos, caso sejam, apresenta erro
        if materia[i] in acentos:
            return False
    if len(materia) < 3:
        return False
    if len(materia_split) >1:
        return False
    else:
        materia_f.write("{}\n".format(materia)) #Escrevendo a matéria no arquivo de matérias respectivo do curso
        return True

def cadastrar_materia_ma(materia):
    materia_split = materia.split(" ")
    materia_f = open("materia_ma.txt","a")
    for i in range(0, len(materia)): #Percorrendo a varíavel nome e checando se os seus dígitos são algarismos númericos, caso sejam, apresenta erro
        if materia[i] in acentos:
            return False
    if len(materia) < 3:
        return False
    if len(materia_split) >1:
        return False
    else:
        materia_f.write("{}\n".format(materia)) #Escrevendo a matéria no arquivo de matérias respectivo do curso
        return True

def cadastrar_materia_edf(materia):
    materia_split = materia.split(" ")
    materia_f = open("materia_edf.txt","a")
    for i in range(0, len(materia)): #Percorrendo a varíavel nome e checando se os seus dígitos são algarismos númericos, caso sejam, apresenta erro
        if materia[i] in acentos:
            return False
    if len(materia) < 3:
        return False
    if len(materia_split) >1:
        return False
    else:
        materia_f.write("{}\n".format(materia)) #Escrevendo a matéria no arquivo de matérias respectivo do curso
        return True

def cadastrar_materia_adm(materia):
    materia_split = materia.split(" ")
    materia_f = open("materia_adm.txt","a")
    for i in range(0, len(materia)): #Percorrendo a varíavel nome e checando se os seus dígitos são algarismos númericos, caso sejam, apresenta erro
        if materia[i] in acentos:
            return False
    if len(materia) < 3:
        return False
    if len(materia_split) >1:
        return False
    else:
        materia_f.write("{}\n".format(materia)) #Escrevendo a matéria no arquivo de matérias respectivo do curso
        return True

def realocarmaterias():
    dir = os.listdir("Users") #Lendo todos os diretórios de usuários
    
    for i in range(0, len(dir)): #Copiando o arquivo de materias para o diretório de cada usuário
        if "TIPI" in dir[i]:
            os.system("copy materia_tipi.txt Users\\{}".format(dir[i]))
        elif "MA" in dir[i]:
            os.system("copy materia_ma.txt Users\\{}".format(dir[i]))
        if "EDF" in dir[i]:
            os.system("copy materia_edf.txt Users\\{}".format(dir[i]))
        if "ADM" in dir[i]:
            os.system("copy materia_adm.txt Users\\{}".format(dir[i]))

def criar_arquivos_notas(): #Criando os arquivos, executando o pastas.py, não tem como entrar na pasta e executar, então tenho que trazer o arquivo user.txt executar o pastas.py de dentro da pasta raiz copiar os arquivos gerados para dentro da pasta e deletar eles da pasta raiz
    dir = os.listdir("Users") 

    for i in range(0, len(dir)):
        os.system("copyuser.bat {}".format(dir[i]))
    


def trazer_arquivos():

    #Conforme a matricula digitada ele sabe o curso, assim sabe qual o nome do arquivo de matérias e copia da pasta do usuário para o diretório atual.

    global materias_user
    if "TIPI" in session_matricula:
        materia_f = open("materia_tipi.txt","r")
        materias_user = materia_f.read().split("\n")

        if materias_user[0] == '':
            return False

        for i in range(0, len(materias_user)-1):
            os.system("copy Users\{}\{}.txt".format(session_matricula, materias_user[i]))
    elif "ADM" in session_matricula:
        materia_f = open("materia_adm.txt","r")
        materias_user = materia_f.read().split("\n")

        if materias_user[0] == '':
            return False

        for i in range(0, len(materias_user)-1):
            os.system("copy Users\{}\{}.txt".format(session_matricula, materias_user[i]))
    elif "EDF" in session_matricula:
        materia_f = open("materia_edf.txt","r")
        materias_user = materia_f.read().split("\n")

        if materias_user[0] == '':
            return False

        for i in range(0, len(materias_user)-1):
            os.system("copy Users\{}\{}.txt".format(session_matricula, materias_user[i]))
    elif "MA" in session_matricula:
        materia_f = open("materia_ma.txt","r")
        materias_user = materia_f.read().split("\n")

        if materias_user[0] == '':
            return False

        for i in range(0, len(materias_user)-1):
            os.system("copy Users\{}\{}.txt".format(session_matricula, materias_user[i]))

def materias():
    for i in range(0, len(materias_user)-1):
        nota = float(input("Digite a nota equivalente à {}\n>> ".format(materias_user[i])))

        materia_atual_f = open("{}.txt".format(materias_user[i]),"w") #O usuário entra com a nota respectiva da matéria e o sistema escreve essa nota no arquivo.
        materia_atual_f.write(str(nota))
        materia_atual_f.close()

def escolhermateria():

    #Percorre toda a lista de matérias do usuário logado
    #Mostra todos com seu respectivo indice
    #Trata o erro de entrada de dados
    #Altera o valor conforme o indice que o usuário escolheu

    print("-"*50)
    for i in range(0, len(materias_user)-1):
        print("Digite {} para editar {}".format(i, materias_user[i]))
    escolha = int(input(">> "))
    while escolha > len(materias_user) or escolha < 0:
        print("Matéria Inválida! Escolha novamente")
        escolha = int(input(">> "))
    nota = float(input("Digite sua nova nota equivalente à {}\n>> ".format(materias_user[escolha])))

    material_atual_f = open("{}.txt".format(materias_user[escolha]),"w")
    material_atual_f.write(str(nota))
    material_atual_f.close

def boletim():
    
    #Le todas as notas do usuario, abrindo cada arquivo
    #Salva as notas em uma lista
    #Incrimenta as dps
    #Mostra se foi aprovado com dependencia ou não
    
    notas = []
    dps = 0

    for i in range(0, len(materias_user)-1):
        nota_materia = open("{}.txt".format(materias_user[i]),"r")
        nota_atual = nota_materia.read()
        nota_materia.close()
        notas.append(nota_atual)
        
    print("-"*50)
    for i in range(0, len(materias_user)-1):
        if float(notas[i])== 100:
            print("{} ----- {} Aprovado com Distinção".format(materias_user[i], notas[i]))
        elif float(notas[i]) >= 60 and float(notas[i])< 100:
            print("{} ----- {} Aprovado".format(materias_user[i], notas[i]))
        else:
            print("{} ----- {} Reprovado".format(materias_user[i], notas[i]))
            dps += 1
    print("\n")
    if dps == 0:
        print("Aprovado sem dependência")
    elif dps > 0 and dps <= 2:
        print("Aprovado com {} dependência(s)".format(dps))
    else:
        print("Reprovado")
    print("-"*50)

def finalizar_aluno():

    #Copia os arquivos de volta para a pasta do usuario logado
    #Delta os arquivos da pasta atual

    for i in range(0, len(materias_user)-1):
        os.system("copy {}.txt .\\Users\\{}\\{}.txt".format(materias_user[i], session_matricula, materias_user[i]))
        os.system("del {}.txt".format(materias_user[i]))

criar_arquivos()
os.system("cls")
os.system("cls")
realocarmaterias()
criar_arquivos_notas()
os.system("cls")
while True:
    print("-"*50)
    escolha = int(input("Digite 1 para cadastrar um usuário\nDigite 2 para logar\nDigite 3 para sair\n>> "))

    while escolha != 1 and escolha !=2 and escolha !=3 and escolha != 123:
        escolha = int(input("Entrada inválida\nDigite 1 para cadastrar um usuário\nDigite 2 para logar\nDigite 3 para sair\n>> "))

    if escolha == 1:
        cadastro()
        criar_arquivos_notas()
        os.system("cls")
        finalizar_matricula(nome, cpf, nascimento, email, curso)
        
    
    
    if escolha == 2:
        realocarmaterias()
        criar_arquivos_notas()
        os.system("cls")
        matricula_login = str(input("Digite sua matrícula para logar(Ou 0 para sair do programa): "))
        if matricula_login == "0":
            break
        while login_matricula() == False:
            matricula_login = str(input("Matrícula digitada inexistente. Digite sua matrícula para logar(Ou 0 para sair do programa): "))

        
        senha_login = str(input("Digite a senha referente a sua matrícula(Ou 0 para sair do programa): "))
        if senha_login == "0":
            break
        while login_senha() == False:
            senha_login = str(input("Senha inválida! Digite a senha referente a sua matrícula(Ou 0 para sair do programa): "))
        
        if trazer_arquivos() == False:
            print("Não há materias cadastradas para seu curso. Converse com o administrador do sistema.")
            break

        while True:
            escolha_login = int(input("\nDigite 1 para cadastrar nota(sequencialmente)\nDigite 2 para ver suas notas(Somente Uma)\nDigite 3 para ver o boletim.\nDigite 4 para voltar ao hub\n>> "))
            if escolha_login == 1:
                materias()

            if escolha_login == 2:
                escolhermateria()

            if escolha_login == 3:
                boletim()

            if escolha_login == 4:
                finalizar_aluno()
                print("\n")
                break
    
    
    if escolha == 123:
        print("-"*50)
        print("Bem vindo, Administrador!")
        
        while True:
            
            escolha_adm = int(input("\nDigite 1 para cadastrar uma matéria.\nDigite 2 para sair.\n>> "))
            if escolha_adm == 1:
                curso = str(input("Escolha o curso em que deseja alterar a matéria(TIPI, ADM, EDF ou MA): "))
                curso = curso.strip().upper()
                while curso not in cursos:
                    curso = str(input("Entrada Inválida!\nEscolha o curso em que deseja alterar a matéria(TIPI, ADM, EDF ou MA): "))
                    curso = curso.strip().upper()
                quantidade = int(input("Digite a quantidade de matéria a serem cadastradas: "))
                
                
                for i in range(1, quantidade+1):
                    print("Digite sem acentos!!!")
                    nome_materia = str(input("Digite o nome da {}ª matéria a ser cadastrada: ".format(i)))
                    if curso == "MA":
                        while cadastrar_materia_ma(nome_materia) == False:
                            nome_materia = str(input("Entrada inválida! Digite o nome da {}ª matéria a ser cadastrada: ".format(i)))
                    elif curso == "EDF":
                        while cadastrar_materia_edf(nome_materia) == False:
                            nome_materia = str(input("Entrada inválida! Digite o nome da {}ª matéria a ser cadastrada: ".format(i)))
                    elif curso == "TIPI":
                        while cadastrar_materia_tipi(nome_materia) == False:
                            nome_materia = str(input("Entrada inválida! Digite o nome da {}ª matéria a ser cadastrada: ".format(i)))
                    elif curso == "ADM":
                        while cadastrar_materia_adm(nome_materia) == False:
                            nome_materia = str(input("Entrada inválida! Digite o nome da {}ª matéria a ser cadastrada: ".format(i)))
                    
                realocarmaterias()
            if escolha_adm == 2:
                print("\n")
                break
    
    if escolha == 3:
        break