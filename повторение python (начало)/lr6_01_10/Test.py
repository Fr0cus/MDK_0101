def find_longest_word(word_list):  
    longest_word = ''  
    longest_size = 0   
    for word in word_list:    
        if len(word) > longest_size:
            longest_word = word
            longest_size = len(word)      
    return longest_word


words = input('Please enter a few words')  
word_list = words.split()  
find_longest_word(word_list) 
