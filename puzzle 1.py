v = [199, 200, 208, 210, 200, 207, 240, 269, 260,263]

increase =0
decrease =0

length = len(v)

for i in range(0, length-1):
    if v[i+1] > v[i]:
        increase= increase +1
    else:
        decrease= decrease +1

print ("increased elemenets:", increase)
print (" decreased elements:", decrease)

# Correct answers: increased elemenets: 1184
