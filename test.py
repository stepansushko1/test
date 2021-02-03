# """ LESSON 1 """

# class Point:        # класс
#     x = 1
#     y = 2


# point_1 = Point()   # екземпляр

# point_1.x = 10

# getattr(point_1, "x", False)     # повертає значення атрибута
# hasattr(point_1, "x")            # повертає булеве, якщо є або немає атрибуту
# setattr(point_1, "x", 7)         # додає атрибут або змінює існуючий
# delattr(point_1, "y")            # видаляє атрибут

# point_1.__dict__                 # показує, які локальні об'єкти має екземпляр

""" LESSON 2 """

class Point4D:
    x = 1
    y = 5

    def addDots(self,x,y):
        self.a = x
        self.b = y

pt = Point4D()

pt.addDots(5,7)

print(pt.__dict__)


