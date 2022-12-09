"Day 8 of AOC2022"
with open("AoC2022_08_data.txt", "r") as file:
    data = file.read()

data=data.split('\n')
R,C = len(data),len(data[0])
d = [(1,0),(-1,0),(0,1),(0,-1)]
ans1,ans2=0,0
            
def check_view(r,c,d,m):
    if 0<=r<R and 0<=c<C and int(data[r][c])<m:
        n,visible=check_view(r+d[0],c+d[1],d,m)
        return 1 + n,visible
    elif 0<=r<R and 0<=c<C and int(data[r][c])>=m:
        return 1,False
    else:
        return 0,True
            
def scenic_score(r,c):
    score = 1
    visible = False
    for dr,dc in d:
        n,v = check_view(r+dr,c+dc,(dr,dc),int(data[r][c]))
        visible = max(visible,v)
        score *= n
    return score,visible
               
for r in range(R):
    for c in range(C):
            score,visible = scenic_score(r,c)
            if visible:
                ans1+=1
            ans2 = max(ans2,score)
print(ans1)
print(ans2)
