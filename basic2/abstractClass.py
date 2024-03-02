from abc import abstractmethod

class MyInterface:
    @abstractmethod
    def method1(self):
        pass   

    @abstractmethod
    def method2(self):
        pass



class MyClass(MyInterface):
    def method1(self):
        print("method1")

    def method2(self):  
        print('Method 2')



myObj = MyClass()

myObj.method1()
myObj.method2()
