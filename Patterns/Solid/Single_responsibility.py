# Anti pattern


class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Invoice(Book):

    def __init__(self, quantity: int, discount_rate: float, tax_rate: float, name, price):
        super().__init__(name, price)
        self.quantity = quantity
        self.discount_rate = discount_rate
        self.tax_rate = tax_rate
        self.total_price = None

    def calculate_total(self):
        self.total_price = (self.price - self.price * self.discount_rate) * self.quantity
        return self.total_price

    def print_price(self):
        print(f"{self.quantity} x  {self.name}    {self.price}  $")
        print(f"Discount Rate: {self.discount_rate}")
        print(f"Tax Rate: {self.tax_rate}")
        print(f"Total: {self.total_price}")

    def save_to_file(self, text: str, filename: str):
        """ func, saving results in file """
        pass


"""
‼️Антипаттерн, т.к. причиной изменения класса должно служить только изменение системы подсчета полной стоимости 
При изменении формата вывода, пострадает этот же класс! 

В нашем классе есть еще один метод, нарушающий SRP, — метод save_to_file. 
Смешивание долгоживущей логики с бизнес-логикой это еще одна распространенная ошибка.
Думайте об этом не только как о записи в файл: это могло бы быть сохранение в базу данных, создание вызова API и т.д

✅Для следования принципу, следует создать 2 отдельных класса для вывода тестра и для сохранения данных в файлы или БД
"""

class InvoicePrint(Invoice):
    # В этот класс выделяем логику выводов
    pass

class InvoiceSave(Invoice):
    # Здесь прописываем сохранение данных
    pass




