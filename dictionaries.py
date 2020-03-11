ja = {
    "name": "Czarek",
    "surname": "Bohdanowicz",
    "age": 22,
    "height": 186,
    "owns_dog": False
}
karolina = dict(name = "Karolina", surname = "Jadwiżyc", age = 22, height = 150, owns_dog = True)

# print(ja,karolina)
for key, value in karolina.items():
    print(key+ ":", value)
print(" ")
for key, value in ja.items():
    print(key+ ":", value)

if ja["height"] > karolina['height']:
    print("Czarek jest wyższy")
else:
    print("Karolina jest wyższa")

