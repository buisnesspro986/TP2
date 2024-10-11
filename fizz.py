class FizzBuzz:
    def affiche(self, n1, n2):
        result = []
        for i in range(n1, n2 + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FrisBee")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return "".join(result)


fizzbuzz = FizzBuzz()
print(fizzbuzz.affiche(5, 10))  
print(fizzbuzz.affiche(10, 16)) 




