#SALVA A INFORMAÇÃO DO USUÁRIO ATUAL LOGADO
from modules import database

sessionID = -1
sessionUsername = ''
sessionTokenID = ''
sessionRole = -1

tempRole = 'Visitante'

restartable = [sessionID,sessionUsername,sessionTokenID,sessionRole]

def update():

  global sessionUsername 
  global sessionTokenID 
  global sessionRole 
  global sessionID

  sessionIndex = database.users.index(sessionUsername.lower())

  sessionUsername = database.users[sessionIndex]
  sessionTokenID = database.tokenID[sessionIndex]
  sessionRole = database.roles[sessionIndex]
  sessionID = database.id[sessionIndex]



def createSession(id,name,tokenID,Role):
  global sessionID 
  global sessionUsername 
  global sessionTokenID
  global sessionRole

  sessionID = id
  sessionUsername = name
  sessionTokenID = tokenID
  sessionRole = Role


def drawNameAndRole():
  global tempRole
  if(sessionRole == 1):
    tempRole = 'Admin'
  else:
    tempRole = 'Visitante'

  print(f'=> BEM-VINDO {sessionUsername.capitalize()} | CARGO {tempRole} <=\n')  

def resetValues():
  for i in range(0,len(restartable)):
    restartable[i] = -1




    