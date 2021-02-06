import socket 
print('''
 ______   _______ _________ _______ 
(  __  \ (  ____ \\__   __/(  ____ )
| (  \  )| (    \/   ) (   | (    )|
| |   ) || (____     | |   | (____)|
| |   | |(_____ \    | |   |     __)
| |   ) |      ) )   | |   | (\ (   
| (__/  )/\____) )   | |   | ) \ \__
(______/ \______/    )_(   |/   \__/
       # Thanks for use my tool #

########################
#[1]port scan          #
#[2]get ip web site    #
#[3]name port          #
#[4]get your ip        #   
########################
''')
cho = int(input("enter number you went :"))
if cho == 1:
    host = input('rhost: ')
    try:
        for port in range(1,1000):
            s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((host,port))
            if result == 0: 
                def non():
                    print('------------------')
                print("port {} is open. ".format(port))
                non()
    except:
        print("erorr")

elif cho == 2 :
    ip = socket.gethostbyname(input("enter url :"))

    print ("ip adresss :" +" "+ ip)

elif cho == 3 :
    print('''
    [1] number port with name 
    [2] name port with number 
    ''')
    cho2 = int(input("enter number :"))
    if cho2 == 1:
        port = socket.getservbyname(input("enter name port :"))
        print("port number :" +" "+ port)
    elif cho2 == 2 :
        port2 = socket.getservbyport(int(input("enter number port :")))
        print("port name is :"+" "+ port2)

elif cho == 4 :
    def find_id():
        host = socket.gethostname()
        ip_add = socket.gethostbyname(host)

        print(f'host : {host}')
        print(f'IP Address : {ip_add}')

    if __name__ == '__main__':
        find_id()
elif cho == 5:
    print('''
    #################################################
    # you most install geoip and geolite2           #
    # serch in youtube how install geoip in python3 #
    #################################################
    ''')
    from geoip import geolite2
    ip = input("enter ip : ")
    local = geolite2.lookup(ip)

    if local is None :
        print("unkonwn")

    else:
        print (local)