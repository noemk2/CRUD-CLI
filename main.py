#!/usr/bin/env python
import sys
#
##
###
#####
#######
##########
############
clients = [
    {
        'name':'pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Sofware enginner',
    },
    {
        'name':'Ricardo',
        'company': 'Facebook',
        'email': 'pablo@facebook.com',
        'position': 'Data enginner',
    },
]
############
##########
#CRUD###
######
####
###
##
#"C" (cread)
def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client alredy is in the client\'s list')
#
##
###
#####
#######
##########
#"R" (read)#
def read_clients():
    for idx, client in enumerate(clients, start=1):
        # print(f"{idx}:{client['name']}")
        uid=idx
        name= client['name']
        company=client['company']
        email=client['email']
        position=client['position']
        print(f"{uid} | {name} | {company} | {email} | {position}")
############
#########
#######
####
###
##
#"U*" (update)
def update_client(client_name, newClient):
    global clients
    indice = _get_index_client('name',client_name)
    if indice >= 0:
        clients[indice] = newClient
    else:
        _not_client_name()
#
##
###
#####
#######
##########
#"D*"(delete)
def delete_client(client_name):
    global clients
    index = _get_index_client('name',client_name)
    if index >=0:
        clients.pop(index)
    else:
        _not_client_name()
############
#########
#######
####
###
##
#---miscelaneas--
#"Search"
def search_client(client_name):
    global clients

    for client in clients:
        if client_name == client['name']:
            return True

#obtain index engine
def _get_index_client(client_name,client):
    indice = -1
    for idx, clientes in enumerate(clients):
        if client == clientes[client_name]:
            indice = idx
            break
    return indice
    
#Welcome comand's           
def _print_welcome():
    logo= '## WELCOME TO PLATZIVENTAS ##'
    sause= '# what would you like to do today?'
    for i in range(0,5):
        print("#"*i)
    print("#"*len(logo))
    print(logo)
    print("#"*len(logo))
    for i in range(4,0,-1):
        print("#"*i)
    print(sause.upper())
    for i in range(1,5):
        print("#"*i)
    print('*'*24)
    print('*  [C] Create client   *')
    print('*  [L] List client     *')
    print('*  [U] Update client   *')
    print('*  [D] Delete client   *')
    print('*  [S] Search client   *')
    print('*                      *')
    print('*'*24)

#cuestion field
def _get_client_field(field_name,client_name):
    field = None
    if client_name == '':
        while not field:
            field = input(f'What is the client {field_name} create? ')
    else:
        while not field:
            field = input(f'What is the new client {field_name}? ')    

    return field

#cuestion client name
def _get_client_name():
    client_name = None

    while not client_name:
        client_name= input('what is the client name? ')

        if client_name == 'exit':
            client_name= None
            break

    if not client_name:
        sys.exit()

    return client_name

#answer not client
def _not_client_name():
    return input('Client is not in clients list...')    
    
#object new client
def _newClient(client_name):
    return {
            'name' : _get_client_field('name',client_name),
            'company': _get_client_field('company',client_name),
            'email': _get_client_field('email',client_name),
            'position': _get_client_field('position',client_name),
        }

#start comand's
if __name__ == '__main__':
    _print_welcome()
    comand = input()
    comand = comand.upper()
    #C
    if  comand == 'C':
        client = _newClient('')
        create_client(client)
        read_clients()
    #L
    elif comand == 'L':
        read_clients()
    #D
    elif comand == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        read_clients()
    #U
    elif comand == 'U':
        client_name = _get_client_name()
        option = search_client(client_name)
        if option == True:
            newClient = _newClient(client_name)
            update_client(client_name, newClient)
            read_clients()
        else:
            _not_client_name()
    #S
    elif comand == 'S':
        client_name = _get_client_name()
        #found puede ser true o false
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
                print(f'The client {client_name} is not in our client\'s list')
    #else
    else:
        print('Invalid comand')
