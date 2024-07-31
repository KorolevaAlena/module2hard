box = ""
namber = int(input("Введите число от 3 до 20: "))

if namber < 3 or namber > 20:
    print("Число введено некорректно")

for i in range(1, 21):
    for j in range(i+1, 21):
        if namber % (i+j) == 0:
            box += f"{i}{j}"
print(box)