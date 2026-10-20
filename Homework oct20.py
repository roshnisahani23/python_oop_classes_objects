class Bangles:
    material = "Glass"

    def __init__(self, s, c, p):
        self.size = s
        self.color = c
        self.price = p


b1 = Bangles("Medium", "Red", "100rs")
b2 = Bangles("Small", "Green", "150rs")
b3 = Bangles("Large", "Blue", "200rs")
b4 = Bangles("Medium", "Pink", "120rs")
b5 = Bangles("Small", "Yellow", "180rs")

bangles_list = []
bangles_list.append(b1)
bangles_list.append(b2)
bangles_list.append(b3)
bangles_list.append(b4)
bangles_list.append(b5)

for obj in bangles_list:
    print(obj.material)
    print(obj.size)
    print(obj.color)
    print(obj.price)



class Lipstick:
    Brand = "Swiss Beauty"

    def __init__(self, c, p, q):
        self.color = c
        self.price = p
        self.quality = q


lip1 = Lipstick("Wine", "500rs", "Good")
lip2 = Lipstick("Pink", "300rs", "Good")
lip3 = Lipstick("Red", "250rs", "Excellent")
lip4 = Lipstick("Brown", "400rs", "Good")
lip5 = Lipstick("Nude", "350rs", "Excellent")

lipstick_list = []
lipstick_list.append(lip1)
lipstick_list.append(lip2)
lipstick_list.append(lip3)
lipstick_list.append(lip4)
lipstick_list.append(lip5)

for obj in lipstick_list:
    print(obj.Brand)
    print(obj.color)
    print(obj.price)
    print(obj.quality)

class WaterBottle:
    brand = "Milton"

    def __init__(self, c, cap, m, p, w, s):
        self.color = c
        self.capacity = cap
        self.material = m
        self.price = p
        self.weight = w
        self.shape = s


w1 = WaterBottle("Blue", "2L", "Plastic", "250rs", "200g", "Cylindrical")
w2 = WaterBottle("Red", "1L", "Steel", "300rs", "250g", "Round")
w3 = WaterBottle("Green", "750ml", "Plastic", "150rs", "150g", "Round")
w4 = WaterBottle("Black", "1.5L", "Steel", "400rs", "300g", "Cylindrical")
w5 = WaterBottle("Pink", "500ml", "Plastic", "100rs", "100g", "Round")

bottle_list = []
bottle_list.append(w1)
bottle_list.append(w2)
bottle_list.append(w3)
bottle_list.append(w4)
bottle_list.append(w5)

for obj in bottle_list:
    print(obj.brand)
    print(obj.color)
    print(obj.capacity)
    print(obj.material)
    print(obj.price)
    print(obj.weight)
    print(obj.shape)


class StudyTable:
    brand = "Godrej"

    def __init__(self, c, m, l, w, h, p, d):
        self.color = c
        self.material = m
        self.length = l
        self.width = w
        self.height = h
        self.price = p
        self.drawers = d


t1 = StudyTable("Brown", "Wood", "120cm", "60cm", "75cm", "2000rs", 2)
t2 = StudyTable("White", "Wood", "100cm", "50cm", "70cm", "2500rs", 3)
t3 = StudyTable("Black", "Metal", "110cm", "55cm", "72cm", "3000rs", 2)
t4 = StudyTable("Grey", "Wood", "130cm", "65cm", "75cm", "3500rs", 4)
t5 = StudyTable("Blue", "Plastic", "90cm", "45cm", "68cm", "1500rs", 1)

table_list = []
table_list.append(t1)
table_list.append(t2)
table_list.append(t3)
table_list.append(t4)
table_list.append(t5)

for obj in table_list:
    print(obj.brand)
    print(obj.color)
    print(obj.material)
    print(obj.length)
    print(obj.width)
    print(obj.height)
    print(obj.price)
    print(obj.drawers)

class Laptop:
    company = "Lenovo"

    def __init__(self, c, r):
        self.color = c
        self.RAM = r


laptop1 = Laptop("Black", "8GB")
laptop2 = Laptop("Silver", "16GB")
laptop3 = Laptop("White", "8GB")
laptop4 = Laptop("Grey", "16GB")
laptop5 = Laptop("Blue", "32GB")

laptop_list = []
laptop_list.append(laptop1)
laptop_list.append(laptop2)
laptop_list.append(laptop3)
laptop_list.append(laptop4)
laptop_list.append(laptop5)

for obj in laptop_list:
    print(obj.company)
    print(obj.color)
    print(obj.RAM)

