from modules import arrDB

isLogged = False


def menu():
    userInput =  input('>[menu] [0] logout\n[menu]>> ')
    if(userInput == '0'):
      print('>[menu] Exiting..')
      global isLogged
      isLogged = False
      startSession()
    (menu())

def trySession():
    global isLogged
    print('>[TS] Iniciar Sessão')
    userLogin = input('>[TS] Digite o nome do usuário\n>> ')
    userPassword = input('>[TS] Digite a senha\n>> ')
    if(userLogin in arrDB.users and userPassword in arrDB.password):
        isLogged = True
        print('>[TS] Logged')
        menu()


def tryLogin():
    while (not isLogged):
      trySession()


def startSession():
    
  while True:
    sessionInput = input('>[SS] [1] Login\n>[SS] [0] Sair\n>[SS]>> ')

    if(sessionInput ==  '1'):
      tryLogin()
    elif(sessionInput == '0'):
      print('>[SS] Exiting..')
      break
    else:
      print('>[SS] Invalid input')
      (startSession())


    

startSession()

