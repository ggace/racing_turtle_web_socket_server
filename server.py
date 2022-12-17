import socket

import time

def reverse(text):
    return text[::-1]

def encoding(text):
    charList =[]

    for t in text:
        charList.append(ord(t))

    rsText = ""

    for c in charList:
        temp = chr(int(reverse(str(c))))
        
        rsText += temp + str(len(str(c)))
        
    return rsText

conn, addr = None, None

def input_controller(number, percentage, forward_from, forward_to):
    result_percentage   = input(f"BOOST{number} percentage  (default:{percentage}) : ")
    result_forward_from = input(f"BOOST{number} forward_from(default:{forward_from}) : ")
    result_forward_to   = input(f"BOOST{number} forward_to  (default:{forward_to}) : ")

    result_percentage   = result_percentage   if result_percentage   != "" else percentage
    result_forward_from = result_forward_from if result_forward_from != "" else forward_from
    result_forward_to   = result_forward_to   if result_forward_to   != "" else forward_to

    return f"{result_percentage} {result_forward_from} {result_forward_to}/"


def run_server(host='127.0.0.1', port=7788):

    global conn, addr


    BUF_SIZE = 1024
    with socket.socket() as sock:
        print("SYSTEM> waiting for connection....")
        sock.bind((host, port))
        sock.listen()
        conn, addr = sock.accept()
        print("SYSTEM> connected to client.\n")
        while True:

            is_start = input(">> ")
            
            if(is_start == "finish"):
                conn.sendall('finish'.encode("utf-8"))
                break
            elif(is_start== "change"):
                data = "change/"
                data += input_controller("1", "12",  "30",  "49")
                data += input_controller("2", "10",  "40",  "57")
                data += input_controller("3", "7",   "50",  "72")
                data += input_controller("4", "5",   "60",  "90")
                data += input_controller("5", "0.4", "400", "600")
                conn.sendall(f'{data}'.encode("utf-8"))

                data = conn.recv(BUF_SIZE)
                msg = data.decode()
                print(f"CLIENT> {data.decode()}\n")
                if msg == 'finish':
                    
                    break
            
            elif(is_start == "go"):
                conn.sendall("go/".encode("utf-8"))

                data = conn.recv(BUF_SIZE)
                msg = data.decode()
                print(f"CLIENT> {data.decode()}\n")
                if msg == 'finish':
                    
                    break
            
if __name__ == '__main__':
    is_run_server = False
    for i in range(3):
        input_id = input("id : ")
        input_pw = input("pw : ")
        print(encoding(input_id), encoding(input_pw))
        if(encoding(input_id) == encoding("id") and encoding(input_pw) == encoding("pw")):
            is_run_server = True
            break
        else:
            print("wrong")
    if(is_run_server):
        run_server()
        print("SYSTEM> wating for closing connection")
        print("SYSTEM> please wait for 3 seconds\n")
        time.sleep(3)
        conn.close()
    else:
        print("login denied")