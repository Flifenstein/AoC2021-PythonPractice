v = [199, 200, 208, 210, 200, 207, 240, 269, 260,263]

increase =0
decrease =0
sum1 =0
sum2 =0
length = len(v)

for i in range(0, length-3):
    sum1 = v[i] + v[i+1] + v[i+2] 
    sum2 = v[i+1] +v[i+2] +v[i+3]
    if sum1 < sum2 :
        increase = increase +1
    else:
        decrease = decrease +1

print ("increased elemenets:", increase)
print (" decreased elements:", decrease)

#correct answer: 1158 increased; 839 decreased
