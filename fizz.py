def affiche(n1, n2):
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
    print("".join(result))
affiche(5, 10)
affiche(10, 16)



