class MoneyBox:
    def __init__(self, capacity=0):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.capacity - v >= 0:
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        self.capacity -= v
