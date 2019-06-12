class Student():
    def test(self,sname,sage):

        if sage >= 18:
                print(sname+" is major")
        else:
                print(sname+" is minor")

s1 = Student()
sname = input('Enter the name: ')
sage = int(input('Enter the age: '))
s1.test(sname, sage)
