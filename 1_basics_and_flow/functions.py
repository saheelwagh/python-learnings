def sayHello(name):
    print(name)

#error handling with try and catch

def divideBy(num):
    try:
        return (42/num)
    except ZeroDivisionError:
        print('cant divide by 0')