v = "Amit_ml@gmail.edu"

print(v.count("@"))
print(v[8:].count("."))

y = (v[8:].count("."))

if y > 1:
    print("invaild email")
          
print(v[0:7])
print(v[8:-4])

if v.endswith(".com"):
    print("Commercial Domain")
    
elif v.endswith(".edu"):
    print("Educational Domain")
    
else:
    print("Other Domain")
    
