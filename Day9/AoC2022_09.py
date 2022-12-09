"Day 9 of AOC2022"
with open("AoC2022_09_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

n=10
visited=[{(0,0)}for i in range(n)]
l=[[0,0] for i in range(n)]
DIR = {'R':(0,1),'L':(0,-1),'U':(1,0),'D':(-1,0)}

def is_touching(t,h):
    dr=abs(t[0]-h[0])
    dc=abs(t[1]-h[1])
    if dr<=1 and dc<=1:
        return True
    return False

def move_head(h,DIR):
    h[0]+=DIR[0]
    h[1]+=DIR[1]
    return h

def move_tail(t,h):
    dr,dc = t[0]-h[0],t[1]-h[1]
    t[1],t[0]=int(h[1]+dc/2),int(h[0]+dr/2)
    if abs(dr)>1 and abs(dc)!=2:
        t[1]=h[1]
    elif abs(dc)>1 and abs(dr)!=2:
        t[0]=h[0]
    return t

for line in data:
    d,n=line.split()
    for i in range(int(n)):
        for k in range(len(l)-1):
            h,t = l[k],l[k+1]
            if k==0:
                h = move_head(h,DIR[d])
                visited[k].add((h[0],h[1]))
            if not is_touching(t,h):
                t = move_tail(t,h)
                visited[k+1].add((t[0],t[1]))

for i in range(len(visited)):
    print(i,l[i], len(visited[i]))
