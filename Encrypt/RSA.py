import random

def totient(p1,p2):

    '''
    totient function ofr use in RSA criptografy
    :param p1: first prime number
    :param p2: secont prime number
    :return: return the number of primes lower then p1*p2
    '''
    return (p1-1)*(p2-1)

def euclidian_mdc(divider,dividend):
    '''

    :param divider: the divider
    :param dividend: the dividend
    :return: return the mdc between numbers
    '''
    while divider != 0:
        temp = divider
        divider = dividend % divider
        dividend = temp
    return dividend

def get_public_keys(p1,p2):
    '''

    :param p1: first prime to generate public key
    :param p2: second prime to generate public key
    :return: return a list of possible public keys.
    '''
    tot = totient(p1,p2)
    keys = []
    for i in range (2,tot):
        key = euclidian_mdc(tot,i)

        if key == 1:
            key = {"k1":p1*p2,"k2":i,'k3':tot}
            keys.append(key)

    return keys

def encrypt_caracter(caracter,key,conjunt_tam):
    '''

    :param caracter: carater to encrypt
    :param key: the key for encrypt
    :param conjunt_tam: the max tam of conjunt for modular aritimetic operations
    :return: a encrypted caracter with RSA logic
    '''

    asc2_value = ord(caracter)
    return (asc2_value **key) % conjunt_tam

def decrypt_caracter(caracter,key,tot):
    '''

    :param caracter:
    :param key:
    :param tot:
    :return:
    '''
    return (caracter**key)%tot

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = int(temp_phi / e)
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:

        return d + phi
    else:
        print('error')
def rsa_encrypt (p1,p2,message):

    '''

    :param p1: first prime number to encrypt
    :param p2: second prime number to encrypt
    :param message: the mesage to encrypt in a str
    :return: the keys used to encrypt and the encrypted mesage
    '''

    conjunt_tam = p1*p2
    keys = get_public_keys(p1,p2)
    key = keys[random.randrange(len(keys))]
    encrypted_mesage = []

    for cacarter in message:
        encrypted_mesage.append(str(encrypt_caracter(cacarter,int(key['k2']),conjunt_tam)))

    return {'key':key,'mesage':encrypted_mesage}

def rsa_decrypt(mesage,key):

    private_key = multiplicative_inverse(int(key['k2']),key['k3'])
    msg = []
    decrypted_mesage = ''
    for caracter in mesage:
        msg.append(str(decrypt_caracter(int(caracter),int(private_key),int(key['k1']))))
    for mesage in msg:
        decrypted_mesage = decrypted_mesage + str(chr(int(mesage)))
    return decrypted_mesage




