y = input("Texto: ")
count = {}

for l in y.lower():
  if l.isalpha():
    if l in count:
      count[l] += 1
    else:
      count[l] = 1
    
print(count)
