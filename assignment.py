'''PROVIDED INFORMATION
I am a human
I am good
Good graders study well
Humans love graders
Every human does not study well
Query:Is every human a good garder?'''
#Code
print("Is every human a good grader")
lst1=[1,1,0,0]    #truth values for proposition Every human does not study well
lst2=[0,1,0,1]    #truth values for proposition Good graders study well
lst3=[]           #to store truth values for propsition Is every human good grader
j=0               #indexing variable
for i in lst1:
    lst3.append(not(i) and lst2[j])
    j+=1
if lst3.count(1)==4:
    print("Yes")
else:
    print("No")
