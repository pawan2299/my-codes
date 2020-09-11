''' 4x5 column of 1to5 numbers increasing order
1	1	1	1	
2	2	2	2	
3	3	3	3	
4	4	4	4	
5	5	5	5	
'''
for i in range(1,6):
    for j in range (4):
        print(i,end="\t")
    print()

print("\n")
#  OR

for i in range(1,6):
    for j in range (1,5):
        print(i,end="\t")
    print()