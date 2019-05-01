#!/usr/bin/env python
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


#miscelaneas
def list_clients():
    global clients

    print(clients)


def _add_semicolon():
    global clients

    clients += ','


def _print_welcome():
    print('WELCOME TO PLATZIVENTAS')
    print('*'*50)
    print('what would you like to do today?')
    print('[C] create client')
    print('[U] Update client')
    print('[D] delete client')


def _get_client_name():
    return input('what is the client name? ')


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

    #else
    else:
        print('Invalid comand')
