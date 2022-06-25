
import enchant
d = enchant.Dict("en_US")
word = list(input("Enter the 5 letters here:"))
words = []
count = 0

def swap(sIndex, nIndex):
    temp = word[sIndex]
    word[sIndex] = word[nIndex]
    word[nIndex] = temp

for i in range(5):
    if(i!=0):
        swap(0,1)
    for j in range(4):
        if(j!=0):
            if(j==1 or j==2):
                swap(1,2)
            else:
                swap(1,4)
        for k in range(3):
            if(k!=0):
                swap(2,3)
            for l in range(2):
                if(l!=0):
                    swap(3,4)
                if(l>0):
                    if(d.check("".join(word[0:3]))):
                        words.append("".join(word[0:3]))
                if(d.check("".join(word[0:4]))):
                    words.append("".join(word[0:4]))
                if(d.check("".join(word))):
                    words.append("".join(word))
                    
words.sort(key=len)
words.reverse() 
for x in words:
    print(x)
    count+=1
print(count)