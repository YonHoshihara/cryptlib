import yaml
from Encrypt import DES
from  Encrypt import Hash
from Encrypt import RSA
from Encrypt import DES

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
    print(keys)
    chat = open('chat.yaml')
    chat = yaml.load(chat)
    key_RSA = keys['rsa_public']
    key_DES = keys['DES']
    print(key_DES)
    des = DES.des()
    encrypt_msg = des.encrypt(key_DES,message)
    key_DES_encrypted = RSA.rsa_encrypt(key_RSA, key_DES)
    hash_mesage = Hash.generate_hash_md5(message)
    result = {'DES_key': key_DES_encrypted,'hash_mesage':hash_mesage,'encrypt_mesage':encrypt_msg}
    chat['mesages'].append(result)
    with open('chat.yaml','w') as f:
        yaml.dump(chat, f)


def get_mesages():
    '''
    Todo: decrypt with RSA key and Decrypt with DES key
    :return: mesage decrypted
    '''
    chat = open('chat.yaml')
    chat = yaml.load(chat)
    des = DES.des()

    mesages = chat['mesages']
    keys = open('keys.yaml')
    keys = yaml.load(keys)
    rsa_key_private = keys['rsa_private']
    mesages_decrypted = []

    for mesage  in mesages:
        des_key = RSA.rsa_decrypt(mesage['DES_key'],rsa_key_private)
        print(des_key)
        msg= des.decrypt(des_key,mesage['encrypt_mesage'],)
        hash_msg = Hash.generate_hash_md5(msg)
        #print(hash_msg)
        #print(msg)
        if hash_msg == mesage['hash_mesage']:
            mesages_decrypted.append(msg)

    return mesages_decrypted

def backlog():
    pass

