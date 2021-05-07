print('Hello world!')
sum = 0
x = 1000
y = list(range(1, x))
for i in range(x - 1):
  if (y[i] % 3 == 0) or (y[i] % 5 == 0):
    sum += y[i]
    print(sum)