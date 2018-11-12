import yaml
from Encrypt import DES
from  Encrypt import Hash
from Encrypt import RSA


def register(login,password):
    '''

    :param login:
    :param password:
    :return: nothing
    '''
    archive = open('register.yaml')
    usr = Hash.generate_hash_md5(login)
    psw = Hash.generate_hash_md5(password)
    archive = yaml.load(archive)
    data = {'login':usr,'password':psw}
    archive['users'].append(data)
    with open('register.yaml','w') as f:
        yaml.dump(archive, f)


def login(login,password):
    '''

    :param login:
    :param password:
    :return: bool if user is autorized to see the messages
    '''
    archive = open('register.yaml')
    usr = Hash.generate_hash_md5(login)
    psw = Hash.generate_hash_md5(password)
    archives = yaml.load(archive)['users']

    for archive in archives:
        if(archive['login'] == usr) and (archive['password'] == psw):
            return True

    return False


def send_mesage(message):

    '''
    Todo: encrypt mesage in DES and encrypt the DES mesage with RSA
    :param message:
    :return: mesage encrypted
    '''

    keys = open('keys.yaml')
    keys = yaml.load(keys)
    chat =  open('chat.yaml')
    chat = yaml.load(chat)
    key_RSA = keys['rsa_public']
    encrypt_msg = RSA.rsa_encrypt(key_RSA,message)
    chat['mesages'].append(encrypt_msg)
    with open('chat.yaml','w') as f:
        yaml.dump(chat, f)


def get_mesages():
    '''
    Todo: decrypt with RSA key and Decrypt with DES key
    :return: mesage decrypted
    '''
    chat = open('chat.yaml')
    chat = yaml.load(chat)
    mesages = chat['mesages']
    keys = open('keys.yaml')
    keys = yaml.load(keys)
    rsa_key = keys['rsa_private']
    mesages_decrypted = []
    for mesage  in mesages:
        mesages_decrypted.append(RSA.rsa_decrypt(mesage,rsa_key))
    return mesages_decrypted

def backlog():
    pass

