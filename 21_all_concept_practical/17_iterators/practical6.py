# Ek generator function running_total() banao jo:
# 1. Starting total 0 rakhe.
# 2. yield se current total return kare.
# 3. send(value) se nayi value receive kare.
# 4. Received value ko total mein add kare.
# 5. Updated total ko agle yield par return kare.

# Expected output
# 0
# 10
# 30
# 35

def running_total():
    total = 0
    while True:
        value = yield total
        total += value

runner = running_total()
print(next(runner))
print(runner.send(10))
print(runner.send(20))
print(runner.send(5))