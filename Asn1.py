n=int(input( ))
d={ }
for i in range(n):
    k=int(input( ))
    v=int(input( ))
    d[k]=v
for k in d:
    if k%2==0:
        print('yes',end=' ')
    else:
        print('no',end=' ')
        
