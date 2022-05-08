import socket
import json
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 50000))

Current_BTC_Rate = "100" #Hypothetical

s.listen(1)
conn, addr = s.accept()



def crypto_to_fiat_C(crypto_data):
    f = open('LP.json')
    data = json.load(f)
    update_Data = data
    #adding btc and deducting USD
    prev_btc = update_Data["BTC"]
    prev_usd = update_Data["USD"]

    update_Data["BTC"] = int(crypto_data) + int(prev_btc)

    usd_to_be_sent = int(crypto_data) * int(Current_BTC_Rate)


    update_Data["USD"] = int(prev_usd) - int(usd_to_be_sent)
    # print(update_Data)
    with open("LP.json", "w") as outfile:
        json.dump(update_Data, outfile)
    
    data = {"USDREC":int(usd_to_be_sent)}
    send_data = json.dumps(data)
    conn.sendall(send_data.encode())
    print("Transaction done")
    conn.close()
    

    # if os.path.exists("temp.json"):
    #     os.remove("temp.json")

while 1:
    data = conn.recv(1024)
    # print(type(data))
    datastr = data.decode()
    # print(type(datastr))

    #writing it to temp json file so i can read it back as dictionary/json format, since direct conv not working
    with open("temp.json","w") as tempfile:
        tempfile.write(datastr)


    jsonobj = open('temp.json')
    dataa = json.load(jsonobj)
        

    # print(dataa)
    # print(type(dataa))
    BTC_VAL = dataa["BTCREC"]
    crypto_to_fiat_C(BTC_VAL)
    
