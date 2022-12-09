"Day 3 of AOC2022"
with open("AoC2022_03_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')

ans1=0
ans2=0

def score(x):
    if x.islower():
        return ord(x)-ord('a')+1
    else:
        return ord(x)-ord('A')+27

for line in data:
    s1 = {x for x in line[:len(line)//2]}
    s2 = {x for x in line[len(line)//2:]}
    inCommon = s1 & s2
    for x in inCommon:
        ans1 += score(x)

for i in range(0,len(data),3):
    s1={x for x in data[i]}
    s2={x for x in data[i+1]}
    s3={x for x in data[i+2]}
    inCommon = s1 & s2 & s3
    for x in inCommon:
        ans2 += score(x)

print(ans1)
print(ans2)
