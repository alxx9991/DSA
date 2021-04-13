sensors = [2, 5, 6, 9, 11, 13]
distances = []

i = 0
while i < len(sensors) - 1:
    distances.append(sensors[i+1] - sensors[i])
    i += 1

pairs = []

i = 0
while(i<len(distances)):
    if distances[i] > 2:
        i += 1
        continue
    chain = 0
    while distances[i] <= 2:
        i += 1
        chain += 1
        for j in range(0, chain):
            pairs.append((i - chain + j,i))
        if i == len(distances):
            break


print(pairs)

        
