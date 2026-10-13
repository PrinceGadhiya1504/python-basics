# Topic: tell() aur seek() — file position check aur change karna.
# Static values use karna; input() nahi.
# Tumhe aisa program banana hai jo:
# 1. student.txt ko "r" mode me open kare.
# 2. file.tell() se current file position print kare.
# 3. file.read(5) se pehle 5 characters read kare aur print kare.
# 4. Dobara file.tell() se current position print kare.
# 5. file.seek(0) se file position beginning par le aaye.
# 6. file.readline() se pehli line read karke print kare.

with open("student.txt", "r") as file:
    print(file.tell())
    print(file.read(5))
    print(file.tell())
    file.seek(0)
    print(file.readline())
    print(file.tell())
