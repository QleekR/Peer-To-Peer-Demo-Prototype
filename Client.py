import socket
import json



Current_BTC_Rate = "100" #Hypothetical 1BTC = $100

def LP_crypto_to_fiat(input_btc):
    data = {"BTCREC":int(input_btc)}
    send_data = json.dumps(data)
    s.sendall(send_data.encode())
    data = s.recv(1024)
    s.close()
    print('Received', data.decode())

    #writing it to temp json file so i can read it back as dictionary/json format, since direct conv not working
    with open("tempC.json","w") as tempfile:
        tempfile.write(data.decode())

    tf = open("tempC.json")
    Tempdata = json.load(tf)
    usdrec = Tempdata["USDREC"]

    Rf = open('Wallet.json')
    Readdata = json.load(Rf)
    update_Data = Readdata
    existing_usd = update_Data["USD"] 
    update_Data["USD"] = int(usdrec) + int(existing_usd)

    with open("Wallet.json", "w") as outfile:
        json.dump(update_Data, outfile)

    print("Updated")
    

def crypto_to_fiat_initial():
    print("Welcome to Crypto=>Fiat")
    inpp_sell = input("Please input how much BTC you want to sell?: ")
    continue_yes_or_no = input("1BTC = $100, Would you like to continue?[Y/N]: ")
    if "N" in continue_yes_or_no:
        print("Ending transaction")
        exit()

    #processing coin
    f = open('Wallet.json')
    data = json.load(f)
    oldbtc = data["BTC"]
    newbtc = int(oldbtc) - int(inpp_sell)
    newdicobj = data
    newdicobj["BTC"] = newbtc
    with open("Wallet.json", "w") as outfile:
        json.dump(newdicobj, outfile)

    LP_crypto_to_fiat(inpp_sell)

def fiat_to_crypto(): #To be written
    print("Fiat=>Crypto")
    # inpp_sell = input("How much BTC would you like to buy?: ")
    # #processing currency
    # fi = open('Wallet.json')
    # Cur_data = json.load(fi)
    # old_amt = Cur_data["USD"]
    # Coinfees = int(inpp_sell) * int(Current_BTC_Rate) 
    # new_amt = int(old_amt) - int(Coinfees)
    # updatedcurrencyobj = Cur_data
    # updatedcurrencyobj["USD"] = new_amt
    # with open("Wallet.json", "w") as outfile:
    #     json.dump(updatedcurrencyobj, outfile)


if __name__ == "__main__":

    while 1:
        #Keep trying untill a LP provider is available to connect to
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('localhost', 50000))
            inpp = input("[1]Crypto-To-Fiat\n""[2]Fiat-To-Crypto\nEnter: ")
        
            if "1" in inpp:
                crypto_to_fiat_initial()

            elif "2" in inpp:
                fiat_to_crypto()

            else:
                print("something went wrong!")

        except:
             LP_exists = False
             print(LP_exists)



    
