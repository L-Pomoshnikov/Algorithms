#ищем среди друзей инженера
class friend:
    def __init__(self, n, x, l=1):
        self.name = n
        self.profession = x
        self.level = l
        self.friends = []   

    def add_friends(self, *args): #переменное кол-во аргументов
        for a in args:
            self.friends.append(a)    
    
    def __str__(self):
        return self.name

Alex = friend('Alex','blogger')
Ivan = friend('Ivan','manager')

Sveta = friend('Sveta','sportsman')
Ira = friend('Ira','photographer')
Denis = friend('Denis','engeenier')
Nastya = friend('Nastya','marketer')

Alex.add_friends(Sveta, Ira)
Ivan.add_friends(Denis, Nastya)

deque = []
deque += [Alex, Ivan]
checked = [] #список уже проверенных, чтобы избежать повторных проверок одних и тех же людей
q = 0 #счетчик пути

while deque: #пока очередь не пуста
    f = deque[0]
    if not f in checked:
        q = f.level
        if f.profession == 'engeenier':
            print(f,'is engeenier!') #перегрузка оператора print
            break #не забываем остановить цикл while
        else: 
            checked.append(f)       #1) добавляем друга в список проверенных
            for fr in f.friends: 
                fr.level += 1       #2) друзья друзей будут иметь уровень на единицу больше, чем сам друг
            deque += f.friends      #3) добавляем в очередь проверки друзей друга
            deque.remove(f)         #4) убираем его из очереди проверки
    else:
        continue
else:
    print('engineer not founded')

print(f.profession == 'engeenier')
print('lenght of search is {} level(s)'.format(q))