"Day 2 of AOC2022"
with open("AoC2022_02_data.txt", "r") as file:
    data = file.read()
    
data = [x.split(' ') for x in data.split('\n')]
prova = [('A','Y'),('B','X'),('C','Z')]

score_dic = {'X':1,'A':1,'Y':2,'B':2,'Z':3,'C':3}
res = {'X':0,'Y':1,'Z':2}

score1,score2 = 0,0
for p1,p2 in data:
    score1 += score_dic[p2] + ((score_dic[p2]-score_dic[p1])%3+1)%3*3
    score2 += res[p2]*3 + ((score_dic[p1]-(res[p2]+1)%3%2*2)%(3+(res[p2])%2)+(res[p2]+1)%2)
        
print(score1,score2)
