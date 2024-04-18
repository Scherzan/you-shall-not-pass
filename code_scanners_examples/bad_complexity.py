# example.py

class HighComplexityClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def high_complexity_method(self):
        if self.a > 10:
            for i in range(self.b):
                if i % 2 == 0:
                    print(i)
                    for j in range(i):
                        if j % 3 == 0:
                            print(j)
                            for k in range(j):
                                if k % 4 == 0:
                                    print(k)

class AnotherHighComplexityClass:
    def __init__(self, x):
        self.x = x

    def another_high_complexity_method(self):
        if self.x > 0:
            for i in range(self.x):
                if i % 2 == 0:
                    print(i)
                    for j in range(i):
                        if j % 3 == 0:
                            print(j)
                            for k in range(j):
                                if k % 4 == 0:
                                    print(k)

def moderate_complexity_function(n):
    count = 0
    for i in range(n):
        if i % 2 == 0:
            count += 1
    return count

def very_high_complexity_function(n):
    count = 0
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                if j % 3 == 0:
                    for k in range(n):
                        if k % 4 == 0:
                            count += 1
                            for l in range(n):
                                if l % 5 == 0:
                                    for m in range(n):
                                        if m % 6 == 0:
                                            count += 1
                                            for o in range(n):
                                                if o % 7 == 0:
                                                    count += 1
    return count

if __name__ == "__main__":
    obj1 = HighComplexityClass(15, 20)
    obj1.high_complexity_method()
    
    obj2 = AnotherHighComplexityClass(10)
    obj2.another_high_complexity_method()

    result1 = moderate_complexity_function(100)
    result2 = very_high_complexity_function(100)
    print("Moderate Result:", result1)
    print("Very High Result:", result2)
