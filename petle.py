#razy = input("Ile razy chcesz wypisać swoje zdanie ?")
#zdanie = input()
#print((zdanie + "\n") * int(razy))

for num in range(1,21):
    #print(num)
        if (num%2) == 0 and num != 4:
            print(f" {num} parzysta")
        elif (num == 4 or num == 13):
            print(f" {num} nieszcześliwe")
        else:
            print(f" {num} nieparzysta")

