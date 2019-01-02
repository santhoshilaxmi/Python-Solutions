'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
#gb = []

#for i in range(5):
#    gb.append(list(map(int, input().rstrip().split())))
    
#print(gb)

gb = [[1, 6], [2, 6], [2, 7], [3, 8], [4, 9]]
gb2=[]

for i in gb:
    elem = i[0]
    for j in gb:
        if(i!=j):
            if(elem == j[0]):
                i.append(j[1])
    i.sort()
    if i not in gb2:
        gb2.append(i)
    
print(gb2) 
gb3=[]

for i in range(0,len(gb2)):
    counter = 0;
    list1 = gb2[i]
    for j in range(0,len(gb2)):
        list2 = gb2[j]
        if(i!=j):
            if(len(set(list1[1:])&set(list2[1:]))!=0):
                list3 = list(set(list1)|set(list2))
                if list3 not in gb3:
                    gb3.append(list3)
                counter = counter+1
    if(counter ==0):
        if list1 not in gb3:
            gb3.append(list1)
                
print(gb3)

            
            
    
    