
import random

#value = random.random()
value = 0.6

x = int(input("uma moeda eh x veses mais provavel de ser cara doque coroa: x = :"))


prob = (1 / (x + 1))

print(prob)
print(value)

if value < prob:
    print("coroa")
else:
    print("cara")



#////////////////////////////////////////////////////////