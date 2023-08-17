""" Вкратце, цель шаблона Singleton заключаются в следующем:
• Обеспечение создания одного и только одного объекта класса
• Предоставление точки доступа для объекта, который является глобальным для программы
• Контроль одновременного доступа к ресурсам, которые являются общими"""


class Singleton:
    def __new__(cls, *args, **kwargs):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwargs)
        return it

    def init(self, *args, **kwargs):
        pass


class Singleton2:    # Эта реализация мне более понятна
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

