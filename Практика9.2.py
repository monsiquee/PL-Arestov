print("Практика 9, задание 3")
def F():
    count = 1

    def G():
        nonlocal count
        n = int(input())
        if n == 0:
            return
        if count % 2 == 1:
            print(n)
        count += 1
        G()

    G()

F()