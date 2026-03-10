#func untuk mengembalikan fibonacci ke-n
def fibonacci(n):
    if n <= 0:
        return "Input harus lebih dari 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b


#prosedur untuk mencetak deret fibonacci sampai suku ke-n
def cetakFibonacci(n):
    if n <= 0: 
        print("Input harus lebih dari 0")
        return
    
    a, b = 0, 1
    print("Deret Fibonacci sampai suku ke-", n, ":")
    
    for i in range(1, n + 1):
        if i == 1:
            print(a, end=" ")
        elif i == 2:
            print(b, end=" ")
        else:
            a, b = b, a + b
            print(b, end=" ")
    print()


#memanggil fungsi dan prosedur
n = int(input("Masukkan nilai n: "))

#memanggil fungsi
hasil = fibonacci(n)
print("Fibonacci ke-", n, "adalah:", hasil)

#memanggil prosedur
cetakFibonacci(n)