#!/usr/bin/env python
import sys
clients = 'pablo,ricardo,'

#"C"
def create_client(client_name):
    global clients

    if client_name not in clients:
            clients += client_name
            _add_semicolon()
    else:
        print('Client alredy is in the client\'s list')

 
#"U"
def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
            clients = clients.replace(client_name + ',', update_client_name+',')
    else:
            _not_client_name()


#"D"
def delete_client(client_name):
    global clients

    if client_name in clients:
            clients = clients.replace(client_name+ ',','')
    else:
            _not_client_name()

#"L"
def list_clients():
    global clients

    print(clients)

#"S"
def search_client(client_name):
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True

#miscelaneas
def _add_semicolon():
    global clients

    clients += ','


def _print_welcome():
    print('WELCOME TO PLATZIVENTAS')
    print('*'*50)
    print('what would you like to do today?')
    print('[C] Create client')
    print('[L] List client')
    print('[U] Update client')
    print('[D] Delete client')
    print('[S] Search client')


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


def _not_client_name():
    return input('Client is not in clients list...')    
#END miscelaneas

#star comand
if __name__ == '__main__':
    _print_welcome()

    comand = input()
    comand = comand.upper()

    #C
    if  comand == 'C':
        client_name =_get_client_name()
        create_client(client_name)
        list_clients()

    #L
    elif comand == 'L':
        list_clients()

    #D
    elif comand == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    #U
    elif comand == 'U':
        client_name = _get_client_name()
        update_client_name = input("What is the update client name: ")
        update_client(client_name, update_client_name)
        list_clients()

    #S
    elif comand == 'S':
        client_name = _get_client_name()
        #found puede ser true o false
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
                #  print(f'The client {client_name} is not in our client\'s list')

    #else
    else:
        print('Invalid comand')
