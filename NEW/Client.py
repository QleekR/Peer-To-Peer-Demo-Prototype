# A P2P Client Architecture which supports Encrypted Data transmission

import socket
import rsa
import sys
Current_BTC_Rate = "100" #Hypothetical 1BTC = $100

#Dont ask me how and why this method/function works, took me an entire day to come up with this arrangement
def process_public_key(data):
    public_key2 = rsa.PublicKey.load_pkcs1(data)
    
    with open('keys/pubkey.pem', 'wb') as fileW:
        fileW.write(public_key2.save_pkcs1('PEM'))
    

    with open('keys/pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())
        # print(type(pubKey))
        return pubKey




    
def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False


def crypto_to_fiat(): #Get BTC , Pay Fiat
    print("Welcome to Crypto=>Fiat")
    #Have a method which provides with Verifying stuff to LP to verify and carry out further process,otherwise terminate!
    inpp_sell = input("Please input how much BTC you want to sell?: ")
    continue_yes_or_no = input("1BTC = $100, Would you like to continue?[Y/N]: ")
    if "N" in continue_yes_or_no:
        print("Ending transaction")
        exit()
    try:
        data = s.recv(1024)

    except:
        print("No Public Key Received Yet!")
    
    # print('Received PUBKEY', data.decode())


    pubKey = process_public_key(data.decode()) #Process Pubkey back to RSA Pub Key class since we received it as string which is not accepted for encryption
   
    # print(pubKey)
    info = {"BTCREC":int(inpp_sell)}
    encinfo = rsa.encrypt(str(info).encode('ascii'),pubKey)
    
    #debugging, since the encinfo is empty on LP side
    with open("encryption.txt","wb") as filenc:
        filenc.write(encinfo)

    # print(sys.getsizeof(encinfo)) #debugging

    #sending encinfo to LP
    s.sendall(str(encinfo).encode())
    s.close()
    exit()
    

   
#Exchange Logic
def fiat_to_crypto(): #To be written
    print("Fiat=>Crypto")



    

#program starts here
if __name__ == "__main__":

    while 1:
        #Keep trying untill a LP provider is available to connect to
        try:
            #TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('localhost', 50002))

            inpp = input("[1]Crypto-To-Fiat\n""[2]Fiat-To-Crypto\nEnter: \n""[3]Exit: ")
        
            if "1" in inpp:
                crypto_to_fiat()

            elif "2" in inpp:
                fiat_to_crypto()

            elif "3" in inpp:
                exit()

            else:
                print("something went wrong!")

        except:
             LP_exists = False
             print(LP_exists)



    
'''Bugs:

- Encrypted message is in some 'Scooby-Doo' Language which is non readable/non sendable over socket, since the data decoded on LP code is empty(I basically fucked up encryption)
- I might have fucked up with the type conversions
- I hate RSA Encryption, thanks

'''
