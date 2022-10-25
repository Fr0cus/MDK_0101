import pickle
import time
     


class Otdelbl(): #Класс - отдел с переменными, Класс "Отделы" с переменными: название отдела, этаж, телефон, начальник отдела.
    def __init__(self, nazv_otd, floor, phone, nath_otd):
        self.nazv_otd = nazv_otd
        self.__floor = floor
        self.phone = phone
        

        if  isinstance(nath_otd, str):
            self.nath_otd = nath_otd
        else:                                   
            raise InvalidNameError(nath_otd)
            

        #Свойство
    @property
    def Floor(self): 
        return self.__floor
    
        #Частный метод
    def Nachalinik(self):
        print(f"Начальник данного отдела - {self.nath_otd}")



    #def __del__(self): # Уничтожение экземпляра
        #print(f"На этаж с названием отделом {self.nazv_otd} влетела ракета Калибр")

#Сериализация
    def serialize(self): # Сериализация модели телефона
        with open('D:\Code_all\MDK_0101\лабораторные нормальные\lr4_12_10\cock.pkl', 'wb') as f:
            pickle.dump(self.phone, f)
        f.closed

#Десериализация
    def deserialize(self): #Десериализация модели телефона
        with open('D:\Code_all\MDK_0101\лабораторные нормальные\lr4_12_10\cock.pkl', 'rb') as f:
            cock = pickle.load(f)
        f.closed
        print (cock)


class Human():
    def __init__(self,age):
        self.age = age

    def Prorok(self):
        return (f'Ваш возраст через 5 лет:{self.age+5}')


class Sotrydniki(): #Класс "Сотрудники" с переменными: название отдела, этаж, телефон, начальник отдела.
    def __init__(self, FIO, doljnost, nomer_otdela, pol_M_or_J, adress, date_birth, five_year, age):
        self.FIO = FIO
        self.doljnost = doljnost #Допустимые должности: (конструкторы,инженеры, техники, лаборанты, 
                                 #прочий обслуживающий персонал)
        self.nomer_otdela = nomer_otdela
        self.pol_M_or_J = pol_M_or_J
        self.adress = adress
        self.date_birth = date_birth
        self.sotrydnik = Human(age)#Ассоциация
        self.a = five_year #Агрегация
    
    def __str__(self):
        return f'ФИО:{self.FIO},Возраст:{self.sotrydnik.age}'

    def Future(self):
        return self.a.Prorok()
    
    def Nama(self):
        return self.FIO
    
    def Execution_time(func):

        def wrapper(self, *args, **kwargs):
            result = func(self,*args, **kwargs)
            start = time.perf_counter()
            runtime = time.perf_counter() - start
            print(f"Выполнение метода заняло {runtime:.10f} секунд")
            return result
        return wrapper
    @Execution_time
    def ff(self):
        print(self.FIO)


 

class Organizatsia(): #Класс "Организация" с переменными: название организации, тип деятельности, страна, город, адрес, ФИО директора.
    def __init__(self, nazvanie_org, type_deyatelnosti, country, city, adres, FIO_directora):
        self.nazvanie_org = nazvanie_org
        self.type_deyatelnosti = type_deyatelnosti
        self.country = country
        self.city = city
        self.adres = adres
        self.FIO_directora = FIO_directora
    def Name(self):
        print(f'Тип деятельности:{self.type_deyatelnosti}')

class Dogovor(): #Класс "Договор" с переменными: номер договора, дата заключения договора, организация, стоимость договора.
    def __init__(self, nomer_dogovora, data_zakl, organizatsia, stoimost_dogovora):
        self.nomer_dogovora = nomer_dogovora
        self.data_zakl = data_zakl
        self.organizatsia = organizatsia
        self.stoimost_dogovora = stoimost_dogovora

class Proekt_rab(): #Класс "Проектная работа" с переменными: дата начала проектной работы, дата завершения проектной работы, номер договора, отдел, осуществляющий разработку.
    def __init__(self, data_nachala_rabot, data_zaversheniya_rabot, nomer_dogovor, otdel_razrabotki):
        self.data_nachala_rabot = data_nachala_rabot
        self.data_zaversheniya_rabot = data_zaversheniya_rabot
        self.nomer_dogovor = nomer_dogovor
        self.otdel_razrabotki = otdel_razrabotki

#Наследование
 
class Budget(Organizatsia):
    def __init__(self,nazvanie_org,type_deyatelnosti,country,city,adres,FIO_directora,size): 
        super().__init__(nazvanie_org,type_deyatelnosti,country,city,adres,FIO_directora)
        self.size = size
    def Name(self):  
        print(f'Название организации:{self.nazvanie_org}')

#Перегрузка операций
    def __add__(self, money):
        self.size += money

    def __call__(self, money):
        self.size = money

    def Show_BD(self):
        print(f"Утверждённый бюджет:{self.size}")

class InvalidNameError(Exception):
    def __init__(self, nath_otd):
        self.nath_otd = nath_otd
    
    def __str__(self):
        return f"Неправильное название - {self.nath_otd}! Название состоит из цифр, а должно из букв!"



#Экземпляры
try: 
    o1 = Otdelbl("Calibr",4,"Redmi","Зимин Виктор Анатольевич")
    o2 = Otdelbl("Bread", 1, "Xiaomi", "Лесовой Василий Батькович")
    o3 = Otdelbl("Bread", 1, "Xiaomi", "2004")
    r1 = Organizatsia("Хлебопекарня","Повар","Россия","Новодвинск","Мира 13","Шарипов Никита Олегович")
    r1.Name()
    r1 = Budget(r1.nazvanie_org,r1.type_deyatelnosti,r1.country,r1.city,r1.adres,r1.FIO_directora,5)
    h1 = Human(18)
    h2 = Human(18)
    h3 = Human(19)
    h4 = Human(17)
    s1 = Sotrydniki("Зимин Данила Викторович","Лаборант", 2 ,"М","Пушкина 25", "08.08.2004",h1, h1.age)
    s2 = Sotrydniki("Мальцев Филипп Дмитриевич","Техник", 3 ,"М","Нагорная 47", "15.03.2004",h2, h2.age)
    s3 = Sotrydniki("Зимин Виктор Викторович","Инженер", 42 ,"М","Центральная 13", "11.11.2002",h3, h3.age)
    s4 = Sotrydniki("Четырин Антон Петрович","Конструктор", 10 ,"М","Привокзальная 8", "16.08.2005",h4, h4.age)
#Использование Агрегации и Ассоциации
    print(s1,s2,s3,s4)
    print(s2.Future())

#Перегрузка операций
    r1 + 10
    r1.Show_BD()
    r1(1076)
    r1.Show_BD()
    # print(s1.Nama())
    # o1.Nachalinik()
    # o2.Nachalinik()
#Использование декоратора 
    # s1.ff()
    # s2.ff()
    # s3.ff()
    # s4.ff()
#del o1

    # o2.serialize()
    # o2.deserialize()

#Полиморфизм
    r1.Name()

except InvalidNameError as e:
    print(e)