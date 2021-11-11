import moduleVar
number=200   #第一个number作用域类型是什么？
print(number)
print(number)
print(number)
print(number)
print(moduleVar.number) #第二个number作用域类型是什么？
print(moduleVar.number) #第二个number作用域类型是什么？
print(moduleVar.number) #第二个number作用域类型是什么？
print(moduleVar.number) #第二个number作用域类型是什么？
def function1():
    global number
    print(number)
    numA=500          #numA作用域类型是什么？
    def innerFunc():
        number=400
        print(number) #第三个number作用域类型是什么？
function1()


        
