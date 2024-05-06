import random as r
i=1
while True:
    with open('troll{}.txt'.format(i),'w')as f:
        n=r.randint(0,1000)
        f.write('{}'.format(n))
    i+=1