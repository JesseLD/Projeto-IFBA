from modules import database,showUsers,menu,utils,session,logs,registerUser,appError,search

modifyQueryConfirm = 'N'
modifyConfirm = False

tempUsers = []

newUsername = ''
newPassword = ''


def getRole():
    appError.showLastError()
    newTempRole = int(input('Escolha o cargo do usuário\n[1] Admin\n[0] Visitante\n>> '))
    
    if(newTempRole == ''):
        appError.add('Dado inválido')
        return getRole()
    
    elif((newTempRole > 1) or (newTempRole < 0)):
        appError.add('Dado inválido')
        return getRole()
    
    else:
        appError.clear()
        return newTempRole



def modifyOptions(searchIndex):
    session.update()
    print('O que deseja modificar?')
    appError.showLastError()
    option = input('[1] Nome\n[2] Senha\n[3] Cargo\n[4] TokenID\n[5] Tudo\n[0] Sair\n>> ')


    if(option == '1'):
        utils.clear()
        print('Modificar nome')
        database.users[searchIndex] = registerUser.getUser()
        session.update()
        logs.add(f'{session.sessionUsername} Modificou o usuário {database.users[searchIndex]}')



    elif(option == '2'):
        utils.clear()
        print('Modificar senha')
        database.password[searchIndex] = registerUser.getPass()
        session.update()
        logs.add(f'{session.sessionUsername} Modificou o usuário {database.users[searchIndex]}')


    elif(option == '3'):
        utils.clear()
        print('Modificar cargo')
        database.roles[searchIndex] = getRole()
        session.update()
        logs.add(f'{session.sessionUsername} Modificou o usuário {database.users[searchIndex]}')


    elif(option == '4'):
        utils.clear()
        print('Modificar Token')

        database.tokenID[searchIndex] = registerUser.getToken()   
        session.update()  
        logs.add(f'{session.sessionUsername} Modificou o usuário {database.users[searchIndex]}')   

    elif(option == '5'):
        utils.clear()
        print('Modificar tudo')
        modifyAll(searchIndex) 
        session.update()
        logs.add(f'{session.sessionUsername} Modificou o usuário {database.users[searchIndex]}')

    elif(option == '0'):
        utils.clear()
        menu.drawMenu()
        menu.handleUserInput()

    else:
        appError.add('Opção inválida')  
        modifyOptions(searchIndex)



def modifyAll(searchIndex):

    queryIndex = searchIndex

    print('Insira os novos dados!')

    newUsername = registerUser.getUser()
    newPassword = registerUser.getPass()
    newRole  = getRole()
    newTokenID = registerUser.getToken()

    modifyQueryConfirm = input('Confirma modificar esse registro? [Y/N]\n>> ')
    if((modifyQueryConfirm == 'y') or (modifyQueryConfirm == 'Y')):

        logs.add(f'{session.sessionUsername} Modificou o usuário {database.users[queryIndex]}')

        database.users[queryIndex] = newUsername
        database.password[queryIndex] = newPassword
        database.roles[queryIndex] = newRole
        database.tokenID[queryIndex] = newTokenID

        session.forceCreateSession(queryIndex)

        appError.clear()
        showUsers.showAllUsers()
    else:
        print('Retornando ao menu principal')
        menu.drawMenu()
        menu.handleUserInput()    


def modifyUser():

    appError.showLastError()
    showUsers.printUsers()

    searchValue = input('Digite o *NOME* do usuário que deseja modificar\n>> ')
    appError.clear()

    utils.clear()
 
    if(searchValue.lower() in database.users):
        print('Usuários encontrados')
        print('--------------------\n')

        for i in range(0,len(database.users)):
            if(searchValue.lower() == database.users[i]):
                tempUsers.append( database.id[i])
                print(f'ID: {database.id[i]} | Nome: {database.users[i].capitalize()} | TokenID: {database.tokenID[i]}')


        print('\n')
        modifyQuery = input('digite o *ID* Deseja modificar\n>> ')

        utils.clear()
        
        if(modifyQuery not in tempUsers):
            appError.add('*ID* inválido!') 
            return modifyUser()

        for i in range(0,len(database.id)):
            if(modifyQuery == database.id[i]):
                print('Usuários encontrados')
                print('--------------------\n')

                print(f'ID: {database.id[i]} Nome: {database.users[i]} TokenID: {database.tokenID[i]}')
                print('\n')
                appError.clear()
                modifyOptions(i) 
                return showUsers.showAllUsers()
                 
        appError.add('*ID* inválido!') 
        return modifyUser()

    else:
        appError.add('Não encontrado!')
        return modifyUser()
  