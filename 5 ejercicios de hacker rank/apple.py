def applesAndOranges(apples,oranges,a,s,b,t):
    apples = 0
    oranges = 0
    for i in apples:
        if i+a>=s and i+a<=t:
            apples += 1 
    for i in oranges:
        if i+b>=s and i+b<=t:
            oranges += 1
    print(apples)
    print(oranges)
print(applesAndOranges(3,2,1,3,4,3))


