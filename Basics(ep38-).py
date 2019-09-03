#Unpacking the list or Tuples
date,item,price=['Dec 23,2018','Bread gloves',8.51]
print(date)
def drop_first_last(grades):
    first,*middle,last=grades
    avg=sum(middle)/len(middle)
    print(avg)

drop_first_last([65,75,79,49,56,80,90])

# ZIP

first=['bucky','b','bbsf']
last=['x','y','z']
names=zip(first,last)
for a,b in names:
    print(a, b)

# Lamda
ans = lambda x:x*x*x
print(ans(9))
#Min_Max of the dictionary

stocks={
    'GOOG':145.26,
    'FB':74.23,
    'AMAZON':123.21,
    'YAHOO':56.15,
    'AAPL':253.21
}
print(sorted(zip(stocks.values(),stocks.keys())))
