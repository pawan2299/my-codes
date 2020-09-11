''' how to print 5x4 table with 5to1 numbers  
like this   
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''


for i in range(5,1,-1):
    for j in range (5,0,-1):
        print(j,end="\t")
    print()