
def parse_measurements(file_name):
    with open(file_name) as f:
        return [int(line.strip().replace(',','')) for line in f.readlines()]

increase =0
decrease =0

length = parse_measurements('data.txt')

for i in range(0, length-1):
    if v[i+1] > v[i]:
        increase= increase +1
    else:
        decrease= decrease +1

print ("increased elemenets:", increase)
print (" decreased elements:", decrease)

# Correct answers: increased elemenets: 1184
