# https://stepik.org/lesson/24469/step/6?unit=6775
s, a, b = input(), input(), input()


counter = 0
while True:
    if (a in s and a == b) or (counter > 999):
        counter = "Impossible"
        break

    if a not in s and a == b:
        counter = 0
        break

    elif a not in s:
        break

    s = s.replace(a, b)
    counter += 1

print(counter)




