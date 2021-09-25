A = [1, 1, 2, 6, 8, 9, 4, 5, 6, 45, 34, 66, 44, 37, 78]
print("A: ", A)
print("B: ")
for i in range(0, 15):
    if(A[i] < 30):
        B = A[i]
        print(B, end=", ")
print("")
print("Nhập vào số a: ")
a = input("")
print("Những số nhỏ hơn số a là: ")
for i in range(0, 15):
    if(A[i] < int(a)):
        C = A[i]
        print(C, end=", ")