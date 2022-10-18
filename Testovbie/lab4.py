import pickle
class Biblioteka(): # Сщздание библиотеки с переменными: отдел, кол-во книг
    def __init__(self,chapter, book_in):
        self.chapter = chapter
        self.book_in = book_in

# Конструктор
    def books(self): # Вывод информации о количестве всех книг в отделах библиотеки
        b = b1.book_in + b2.book_in + b3.book_in + b4.book_in
        print("Вы находитесь в отделе " + self.chapter + '.' + 'Сумарное количество книг во всех отделах библиотеки равно ' + str(b))

    def test(self): # unittest
        b = b1.book_in + b2.book_in + b3.book_in + b4.book_in
        return b


# Сериализация
    
    def serialize(self):
        with open('C:\\Programming\\MDK\\MDK_01_01\\Testovbie\\proba.pkl', 'wb') as f:
            pickle.dump(self.book_in, f)
        f.closed

# Десериализация
    
    def deserialize(self):
        with open('C:\\Programming\\MDK\\MDK_01_01\\Testovbie\\proba.pkl', 'rb') as f:
            book_in = pickle.load(f, encoding="UTF-8")
        f.closed
        print(book_in)




#Деструктор
#   def __del__(self): # Уничтожение экземпляра
#       print("Стелаж" + self.chapter + "не находиться в нашей библиотеке")

#Наследование
class Aftor(Biblioteka): #Дочериний класс авторы
    def __init__(self,chapter, book_in, name_aftor):
        super().__init__(chapter, book_in)
        self.name_aftor = name_aftor

    def aftor_chapter(self): #На каком слаже данный автор
        print("Автор " + str(self.name_aftor) + " находится на стелаже " + str(self.chapter) + '.')

#Полиморфизм
    def books(self):
        print("Количество книг на этом стелаже: " + str(self.book_in))

b1 = Biblioteka("Психология", 115)
b2 = Biblioteka("Наука", 33)
b3 = Biblioteka("История", 54)
b4 = Biblioteka("Художественная литература", 211)


b1 = Aftor(b1.chapter, b1.book_in, "Иванов")
b1.aftor_chapter()
b1.books()

b1.serialize()
b1.deserialize()
b4.serialize()
b4.deserialize