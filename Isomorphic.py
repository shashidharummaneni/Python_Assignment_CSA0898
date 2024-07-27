def compare_indexes(ch1,ch2,s1,s2):
    ind1 = []
    ind2 = []
    for i in range(len(s1)):
        if ch1 == s1[i]: ind1.append(i)
        if ch2 == s2[i]: ind2.append(i)
    if ind1==ind2:
        return True
s1 = str(input())
s2 = str(input())
if len(s1)==len(s2):
    lst1 = list(s1.split())
    lst2 = list(s2.split())
    count =0
    for i in range(len(s1)):
        ch1 = s1[i]
        ch2 = s2[i]
        if compare_indexes(ch1,ch2,s1,s2):
            count+=1
    if count==len(s1): print("They are isomorphic")
    else : print("They are not isomorphic")
else:
    print("They are not isomorphic")
        
