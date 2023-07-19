from modules import database


tempUsers = []

def searchByName():
    global tempUsers
    searchQuery = input('Digite o nome do usuário\n>> ')

    foundUsers = [user for user in database.users if searchQuery.lower() in user.lower()]
    tempUsers = foundUsers

    print(foundUsers)

    if foundUsers:
        print('Usuários encontrados')
        print('--------------------\n')
        for user in foundUsers:
            index = database.users.index(user)
            print(f'ID: {database.id[index]} | Nome: {database.users[index]} | TokenID: {database.tokenID[index]} | Cargo: {database.roles[index]}')
        print('\n')
        return True
    else:
        print('Não encontrado')
        return False
    


    
def searchByID():
    global tempUsers
    searchQuery = input('Digite o *ID* do usuário\n>> ')

    foundUsers = [id for id in database.id if searchQuery.lower() in id.lower()]
    tempUsers = foundUsers

    if foundUsers:
        print('Usuários encontrados')
        print('--------------------\n')
        for id in foundUsers:
            index = database.users.index(id)
            print(f'ID: {database.id[index]} | Nome: {database.users[index]} | TokenID: {database.tokenID[index]} | Cargo: {database.tokenID[index]}')
        print('\n')
    else:
        print('Não encontrado')
        return False