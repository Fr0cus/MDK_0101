Capitals = dict()

#Capitals["Архангельск", "Новодвинск", "Северодвинск", "Шенкурск", "Котласс"] = 'Архангельская область'
#Capitals["Санкт-Петербург", "Пушкин", "Павловск"] = 'Ленинградская область'
Capitals['Архангельск'] = 'Архангельская область'
Capitals['Новодвинск'] = 'Архангельская область'
Capitals['Северодвинск'] = 'Архангельская область'
Capitals['Шенкурск'] = 'Архангельская область'
Capitals['Котлас'] = 'Архангельская область'
Capitals['Санкт-Петербург'] = 'Ленинградская область'
Capitals['Павловск'] = 'Ленинградская область'
Capitals['Пушкин'] = 'Ленинградская область'
#Capitals['USA'] = 'Washington'

Countries = ['Архангельск', 'Пушкин', 'Котлас']
for sity in Countries:
 # Для каждой страны из списка проверим, есть ли она в словаре Capitals
    if sity in Capitals:
        print(Capitals[sity])
    else:
        print("В базе нет такого населённого пункта")
