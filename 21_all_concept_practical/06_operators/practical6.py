# Identity Operators (is aur is not)
# Task
#     1. a = [1, 2, 3] banao.
#     2. b = a banao.
#     3. c = [1, 2, 3] banao.
#     4. Check karo a is b.
#     5. Check karo a is c.
#     6. Check karo a == c.
#     7. Check karo a is not c.

# Expected output
#     a is b: True
#     a is c: False
#     a == c: True
#     a is not c: True

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"a is b: {a is b}")
print(f"a is c: {a is c}")
print(f"a == c: {a == c}")
print(f"a is not c: {a is not c}")