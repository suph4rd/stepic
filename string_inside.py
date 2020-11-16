# https://stepik.org/lesson/24469/step/7?unit=6775
s, t = input(), input()

counter = 0
for x in range(len(s)+1-len(t)):
    if s[x:x+len(t)].count(t) > 0:
        counter += 1

print(counter)
