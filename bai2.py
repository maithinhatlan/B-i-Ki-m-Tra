A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 88]
B = [1, 3, 5, 4, 7, 88, 66, 59, 40, 54]
print("A: ", A)
print("B: ", B)

C = set(A) & set(B)
print("Danh sách các phần tử giống nhau trong A và B là: ")
for i in C:
    print(i, end="  ")

D = set(A) - set(B)
print("")
print("Danh sách các phần tử còn lại trong A là: ")
for i in D:
    print(i, end="  ")

E = set(A) - set(C)
print("")
print("Danh sách các phần tử còn lại trong B là: ")
for i in E:
    print(i, end="  ")