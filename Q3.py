# Write a sorting function without using the sort function
l = [5,4,3,22,90,50, 60, 40, 30, 20, 10, 1]
new_list=[]
while l:
    min = l[0]
    for i in l:
        if i >min:
            min=i
    new_list.append(min)
    l.remove(min)
print(new_list)
