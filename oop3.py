def greeting(name):
    name=name
    print(f'hello {name}')
greeting('samwel')

class Patient:
    def __init__(self,name,age,phone_number):
        self.name=name
        self.age=age
        self.phone_number=phone_number
        print(self.name,self.age,self.phone_number)
sam=Patient(name="sam",age=23,phone_number="0715733966")