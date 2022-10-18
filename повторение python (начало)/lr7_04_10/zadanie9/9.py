l = [] # Создается список

with open('D:\\Code_all\\MDK_0101\\повторение python (начало)\\lr7_04_10\\zadanie9\\zadanie9.txt', 'r', encoding='utf8') as file:
    line = file.readlines() # Считываем строки
    
    station_count = int(line[0]) # Кол-во станций
    passengers = line[1:] #Считывание со второй строки
    for i in passengers: 
        l.append(i.split()) # Добавляем в список пассажиров и разделяем их элементы
    print(l)
    print(len(l))
    for i in range(len(l)): #Выборка пассажиров
        for j in range(1,3): # Выписка цифр
            l[i][j] = int(l[i][j])# вывод стартовой станции и конечной
            print(l[i][j])
            
at_every_station = [0 for _ in range(station_count)]
for name, start_station, end_station in l:
    for station in range(start_station - 1, end_station - 1):
        at_every_station[station] += 1
 
max_passengers = max(at_every_station)
 
for station, count in enumerate(at_every_station, start=1):
    if count == max_passengers:
        print(f'{station} - {station + 1}')

file.close()