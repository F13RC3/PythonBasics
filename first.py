#if statement
name= "Ashish"
if name is "K":
    print("Hey there mr.k")
elif name is "Ashish":
    print("hey there Ashish")
else:
    print("no name")
#for loop
foods =['amir','bacon','cat','dog']
for f in foods:
    print(f)
    print(len(f))
#Range function
print("\nNumbers :")
for x in range(10,50,5):
    print(x)

#while loop
print("\nWhile:")
y=8
while y<10:
    print(y)
    y+=1
print("\nWhile:")

#Comments and break & continue

magicNumber= 26
for n in range(100):
    if n is magicNumber:
        print(n," is ur Magic Number!")
        continue
        #break
    else:
        print(n)
#Functions

def bitcoin_to_usd(b):
    amount=b*11235
    print(b,"bitcoin is equal to  $",amount)
bitcoin_to_usd(3.85)

#Return values
def allowed_dating(age):
    gage=age/2+7
    return gage
print("\nYou r allowed to date girls ",allowed_dating(21),"or older\n")

#Default valued arguments
print("Defaul valued agrument")
def get_gender(sex='Unknown'):
    if(sex is 'm'):
        print("Male")
    elif(sex is 'f'):
        print("Female")
    else:
        print(sex)
get_gender('m')
get_gender()
get_gender(sex='fcuk')

#Flexible Amount of Arguments
print("Flexible agrument")
def flex(*args):
    total=0
    for x in args:
        total+=x
    print(total)
flex(3)
flex(3,4,5,6,7,8,9,122,34)

#Unpacking argument
print("\nUnpacking argument \n")
def health_calculator(age,apple_ate,cigs_smoked):
    ans=(100-age)+(apple_ate*2)-(cigs_smoked*2)
    print(ans)
my_health=[21,15,1]
health_calculator(my_health[0],my_health[1],my_health[2])
health_calculator(*my_health)

#Sets
groceries={'a','b','c','d','a'}
print(groceries,"\n")

#Dictionary
classmates = {'tony':' like coffee', 'Lucy':' talks too much'}
for k,v in classmates.items():
    print(k+v)