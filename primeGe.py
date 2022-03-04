#Python 3.8
from math import sqrt
import time

i = j = 3
primes = [3]
class printColor:
    RED = '\033[91m'
    END = '\033[0m'

print("The following numers are prime:\nNO: #1st - Val: 2\nNO: #2nd - Val: 3\nNO: #3rd - Val: 5")

start_time = time.time()
while j<100000:
    if str(i)[(len(str(i))-1)] != "5":
        for x in primes:
            if i % x == 0:
                break
            else:
                if x >= sqrt(i):
                    primes.append(i)
                    j += 1
                    print("NO: #{:0,}th - Val: {:1,}".format(j,i))
                    break
    i += 2
end_time = time.time()

result = "Time Lapsed = {:.6f}".format(end_time-start_time) + " seconds"
print(f"{printColor.RED}{result}{printColor.END}")