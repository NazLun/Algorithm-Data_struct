"""
Как должен вести себя Singleton при создании повторного экземпляра?
- ругаться исключением
- отдать единтсвенный экземпляр без запуска нового констркутора
- отдать единтсвенный экземпляр с запуском нового констркутора
  (! тогда нужно учесть как это отразится на уже созданных связанных объектах внутри, в общем нужно быть аккуратным !)
"""
# https://webdevblog.ru/realizaciya-shablona-singleton-v-python/
# https://pastebin.com/qnjkQht4
# https://proglib.io/p/3-luchshih-patterna-proektirovaniya-v-python-singlton-dekorator-i-iterator-2022-02-03


# подход к созданию одиночки с вызовом конструктора этого же экземпляра при создании нового объекта-ссылки на одиночку
class Singleton1(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        # запуск нового конструктора этого же экземпляра
        # при повторной попытке создать экземпляр одиночки
        # (фактически при получении нового объекта-ссылки на одиночку в нужном месте программы)
        print('! Singleton1.__init__ !')
        self.x = args[0]
        self.y = kwargs['y']


s = Singleton1(1, y=2)
print("Object created", s, s.__dict__)
ss = Singleton1(10, y=20)
print("Object created", ss, ss.__dict__)

# out:
'''
! Singleton1.__init__ !
Object created <__main__.Singleton1 object at 0x00C11FD0> {'x': 1, 'y': 2}
! Singleton1.__init__ !
Object created <__main__.Singleton1 object at 0x00C11FD0> {'x': 10, 'y': 20}
'''


# подход к созданию одиночки без вызова конструктора этого же экземпляра каждый раз при создании нового объекта-ссылки на одиночку
class MetaSingleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = type.__call__(cls, *args, **kwargs)
        return cls._instance


class Singleton2(metaclass=MetaSingleton):
    def __init__(self, *args, **kwargs):
        # полное игнорирование новых аргументов конструктора
        # т.к. сюда даже не попадаем при повторном создании экземпляра одиночки
        print('! Singleton2.__init__ !')
        self.x = args[0]
        self.y = kwargs['y']


s = Singleton2(1, y=2)
print("Object created", s, s.__dict__)
ss = Singleton2(10, y=20)
print("Object created", ss, ss.__dict__)

# out:
'''
! Singleton2.__init__ !
Object created <__main__.Singleton2 object at 0x00C3EAF0> {'x': 1, 'y': 2}
Object created <__main__.Singleton2 object at 0x00C3EAF0> {'x': 1, 'y': 2}
'''

