
mp={} # словарь 
for i in range(int(input())): # вводим строки

    for j in input().split():
        if j not in mp :
            mp[j]=1
        else :
            mp[j]+=1

ss=list(mp.items()) # преобразуем словарь в список
ss.sort(key = lambda x : x[1], reverse=True ) # сортируем список по 2 полю
for x in ss:
    print ("({0} => {1})".format (x[0], x[1]))

#Дан текст, состоящий из строк. Определить количество слов в тексте. Словом считается
#последовательность символов, слова текст разделены пробелом или символом текст конца строки.
#Используйте множества.