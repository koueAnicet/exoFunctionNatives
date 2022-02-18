def getRange():
    i =int(input('nombre1 min:\t'))
    j=int(input('nombre2 max:\t'))
    c=[]
    while i < j:
        c.append(i)
        i+=1
    print(c)
getRange()
#---------------  
# def autre(n,m):
#     n=n-1
#     m=m-1
#     boite=[]
#     while n< m:
#         n+=1
#         boite.append(n)
#     print(boite)

# autre(3,10)

"""def autreFor(n,m):
    n-=1
    m-=1
    boite=[]
    for i in  m:
        boite.append(i)
    print(boite)

autreFor(3,10)"""