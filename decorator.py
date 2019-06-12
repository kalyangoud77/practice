def dec(func):
    def wrap():
        print("$$$$$$$$")
        func()
        print("$$$$$$$$")
    def sayhi():
        print("Hi")
        print (sayhi())