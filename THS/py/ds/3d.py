a=[[[1,2,3],[0,9,2],[1,4,9]]]
b=[[[0,0,0],[0,0,0],[1,0,0]]]
d=[]
for i in range(len(a)):
 a=a[i]
 b=b[i]
 c=[]
 for i in range(3):
     newlists=[]
     for j in range(3):
         newlists.append(a[i][j]+b[i][j])
     c.append(newlists)
 d.append(c)
