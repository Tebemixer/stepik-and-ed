class Buffer:
    def __init__(self):
        #конструктор без аргументов
        self.capacity = []
    def add(self, *a):
        #добавить следующую часть последовательности
        for i in a:
            self.capacity.append(i)
            while len(self.capacity) >= 5:
                print(sum(self.capacity[:5]))
                self.capacity = self.capacity[5:]
    def get_current_part(self):
        #вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        #добавлены
        return self.capacity