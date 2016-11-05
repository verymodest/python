#!/user/bin/python
def foo():
    print 'foo'    

def log():
    print 'logger.debug'

def logFunc(func):
    log()
    func()
#pre foo print log
#step1
print 'step1......'
foo()
log()
logFunc(foo)

#step2
print 'step2......'
def logFuncWrapper(func):
    def wrapper():
        log()
        return func()
    return wrapper

foo = logFuncWrapper(foo)
foo()

#step3
print 'step3......'
@logFuncWrapper
def foo2():
    print 'foo'    
foo2()

#step4
print 'step4......'
def logFuncWrapper2(param):
    def decorator(func):
        def wrapper():
            print param
            log()
            return func()
        return wrapper
    return decorator
@logFuncWrapper2('warning')
def foo3():
    print 'foo'

foo3()
print foo3.__name__

#step5
print 'step5......'
from functools import wraps
def logFuncWrapper3(param):
    def decorator(func):
        @wraps(func) 
        def wrapper():
            print param
            log()
            return func()
        return wrapper
    return decorator

@logFuncWrapper3('warning')
def foo4():
    print 'foo'
print foo4.__name__
