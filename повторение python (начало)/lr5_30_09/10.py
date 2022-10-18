from functools import reduce
 
s = ['научиться плести рыболовные сети', 'обучать нейронные сети', 'паук ловит в сети мух']
 
print(reduce(lambda x, y: x + y, map(lambda x: 'сети' in x.lower(), s), 0))
