class Starter():
    def __init__(self):
        self.cnt = 3
    
    def count_raiser(self):
        for i in range(self.cnt, 0, -1):
            print(f'До старта {i} секунд(ы)')
        self.cnt += 1
        

n = int(input())
starter = Starter()
for i in range(1, n + 1):
    starter.count_raiser()
    print(f'Старт {i}!!!')