v = "&&&**$gnirtS PLIO!!@1234"

print(v[6:-7])

x = v[6:12]
rvs = x[::-1]
print(rvs)

y = v[13:17]
z = y.replace("I","E").replace("O","U")
print(z)

print(rvs,z)