
scores = [68, 87, 99, 25, 34, 22, 12, 44]
total = 0
count = 0

for score in scores:
    if score < 50:
        continue

    total +=score
    count +=1

print("The total is ", total)
print("The amount of scores counted is", count)