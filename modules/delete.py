
from modules import database,menu,showUsers,logs,session,appError,utils

queryDeleteConfirm = 'N'
deleteConfirm = False

tempUsers = []
tempID = 0


def deleteUser():
    global tempID
    appError.showLastError()
    showUsers.printUsers()

    searchValue = input('Digite o nome do usuário para deletar\n>> ')

    if(searchValue.lower() in database.users):
        print('Usuários encontrados')
        print('--------------------\n')

        for i in range(0,len(database.users)):
            if(searchValue.lower() == database.users[i]):
                tempUsers.append( database.id[i])
                print(f'ID: {database.id[i]} Nome: {database.users[i].capitalize()} TokenID: {database.tokenID[i]}')

        print('\n')
        deleteQuery = input('digite o *ID* Deseja deletar: ')

        if(deleteQuery == session.sessionID):
            utils.next()
            utils.clear()
            appError.add('Você não pode deletar você mesmo!')
            deleteUser()

        if(deleteQuery not in tempUsers):
            appError.add('*ID* inválido!') 
            deleteUser()

        if(deleteQuery in database.id):
            if(deleteQuery == database.id[i]):
                print('Usuários encontrados')
                print('--------------------\n')
                print(f'ID: {database.id[i]} Nome: {database.users[i]} TokenID: {database.tokenID[i]}')
                print('\n')

            tempID = deleteQuery
            # print(tempID)
            queryDeleteConfirm = input('Confirma deletar esse registro? [Y/N]\n>> ')
            
            if(queryDeleteConfirm == 'y' or queryDeleteConfirm == 'Y'):

                logs.add(f'{session.sessionUsername} Deletou o usuário {database.users[int(tempID)]}')

                database.id.remove(database.id[int(tempID)])
                database.users.remove(database.users[int(tempID)])
                database.tokenID.remove(database.tokenID[int(tempID)])
                database.password.remove(database.password[int(tempID)])
                database.roles.remove(database.roles[int(tempID)])  

                session.update()    
                appError.clear()
                return showUsers.showAllUsers()


            else:
                appError.clear()
                print('Retornando ao menu principal')
                menu.drawMenu()
                return menu.handleUserInput()    
        else:
          appError.add('*ID* inválido!')  
          utils.next()
          utils.clear()
          return deleteUser()
    else:

        print('Não encontrado')
        utils.next()
        utils.clear()
        menu.drawMenu()
        return menu.handleUserInput()

