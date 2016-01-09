#fileName:testReference.py
print 'simple assignment'
shopList = ['apple','peach','mango','carrot','onion']
myList = shopList
del shopList[0]
print(shopList)
print 'myList is',myList
