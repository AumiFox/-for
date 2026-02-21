multipl = 1
i = 0
for i in range(1, 11):
    if i % 2 == 0:
        continue
    multipl *= i
    print(multipl)