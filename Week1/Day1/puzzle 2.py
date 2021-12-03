
def parse_measurements(file_name):
    with open(file_name) as f:
        return [int(line.strip().replace(',','')) for line in f.readlines()]

measurements = parse_measurements('data.txt')
increase =0
decrease =0
sum1 =0
sum2 =0

for i in range(len(measurements)-3):
    sum1 = sum(measurements[i:i+3])
    sum2 = sum(measurements[i+1:i+4])
    if sum1 < sum2 :
        increase = increase +1
    else:
        decrease = decrease +1

print ("increased elemenets:", increase)
print (" decreased elements:", decrease)

#correct answer: 1158 increased; 839 decreased
