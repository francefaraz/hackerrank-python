l=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name,score]);
lowest=sorted(list(set([scores for name,scores in l])))[1]
print(lowest)
for a,b in sorted(l) :
    if(b==lowest):
        print(a)