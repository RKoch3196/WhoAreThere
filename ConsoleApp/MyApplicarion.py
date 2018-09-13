from uuid import getnode as get_mac

class MyApplication:


    def TEST ():
        print("Hellow Word")

    def __init__(self):
        pass

    def GetMacAdresses():
        mac = get_mac()
        print(mac)

    GetMacAdresses()
