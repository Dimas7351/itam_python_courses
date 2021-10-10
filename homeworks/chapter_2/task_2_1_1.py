def greetings(s):
    s = s.split()
    return "Доброго времени суток, " + s[0] + ' "Человек" ' + s[1] +"!"
print(greetings(input()))
