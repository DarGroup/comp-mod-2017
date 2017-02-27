# ИКНиТО, 2-ой курс, ИВТ, Лазарев Игорь

x = []
y = []
n = int(input("Введите количество элементов: "))

for i in range(n):
  x.append(float(input("Введите " + str(i + 1) + " элемент Х: ")))
  y.append(float(input("Введите " + str(i + 1) + " элемент Y: ")))
  
print(x)
print(y)

x_sr = sum(x) / n
y_sr = sum(y) / n
x_kv_sr = sum(list(map(lambda p: p*p, x))) / n
x_y_sr = sum(list(map(lambda p,k: p*k, x,y))) / n

b1 = (x_y_sr - x_sr * y_sr) / (x_kv_sr - x_sr * x_sr)
b0 = y_sr - b1 *  x_sr

print("b0 = " + str(b0))
print("b1 = " + str(b1))

Xo = []
Yo = []

n = int(input("Введите количество элементов, которые вы хотите вычислить: "))

for i in range(n):
  Xo.append(float(input("Введите " + str(i + 1) + " элемент Х: ")))
  Yo.append(b0 + Xo[i] * b1)

print(Xo)
print(Yo)