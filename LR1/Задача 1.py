vse = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
a = {"а", "о", "э", "е", "и", "ы", "у", "ё", "ю", "я"}
u1 = vse - a
c = input()
b = set(c)
u = b - u1
print(len(u))