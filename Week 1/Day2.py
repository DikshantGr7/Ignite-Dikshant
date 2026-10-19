#Python control structures
#Conditionals

age = int(input("Enter your age:"))
citizen_of_india = True
if age >=18 and citizen_of_india:
    print("You are eligible to vote")
elif age<18 or citizen_of_india == False :
    print("You are not eligible to vote")
else :
    print("You are not eligible to vote as you are either a minor or not a citizen of india")

#Loops
#For Loops

for i in range(1,11):
    print(i,sep =",")

for item in ["apple","banana","cherry"]:
    print(item)

#while loop
count = 0
while count<5:
    count += 1
    if count == 2:
        continue
    if count == 4:
        break
    print(count)

#Lists
a = []                    
b = [1, 2, 3]            
c = list()               
d = list("abc")          
e = list((1, 2, 3))    
print(a,b,c,d,e)

lst = [10, 20, 30]
print(lst)
lst.append(40)    
print(lst)      
lst.extend([50, 60])    
print(lst) 
lst.insert(1, 15)      
print(lst) 
lst.remove(20)   
print(lst)        
val = lst.pop()  
print(lst)        
lst.sort(reverse=True)  
print(lst) 

#Tuples
a = ()                  
b = (1,)                
c = (1, 2, 3)        
d = tuple()             
e = tuple([1, 2, 3])    
f = tuple("py")         
tup = (10, 20, 30, 20)

cnt = tup.count(20)     
print(cnt)
idx = tup.index(30)    
print(idx) 
length = len(tup)   
print(length)    
s_list = sorted(tup)   
print(s_list) 

#Sets
a = set()               
b = {1, 2, 3}         
c = set([1, 2, 2, 3])   
s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1.add(10)
print(s1)
s1.discard(3)   
print(s1)           
u = s1.union(s2)    
print(u)      
i = s1.intersection(s2)    
print(i)
d = s1.difference(s2)       
print(d)
e = s1.symmetric_difference(s2)
print(e)

#Dictionaries
a = {}                            
b = {"a": 1, "b": 2}            
c = dict()                       
d = dict(a=1, b=2)               
e = dict([("a", 1), ("b", 2)])   
d = {"name": "Alice", "age": 25}

d.update({"city": "New York", "age": 26})
print(d)
age = d.get("age", 0)    
print(age)                
role = d.get("role", "N/A") 
print(role)             
val = d.pop("city")     
print(val)                 

for k, v in d.items():
    print(f"{k} -> {v}")

#String Manipulation
s = "  Python Developer  "

# Methods
print(s.strip())           
print(s.lower(),s.upper())
print(s.replace("P", "J"))   
print(s.split(" "))           
print("-".join(["a", "b"]))  
print(s.startswith(" P "))    
s.find("Dev")          


text = "Programming"
print(text[0:4])       
print(text[4:])        
print(text[::-1])      


#Functions

def calculate_total(price: float, tax: float = 0.05, discount: float = 0.0) -> float:
    final_price = price * (1 + tax) - discount
    return round(final_price, 2)

total1 = calculate_total(100.0)                         
total2 = calculate_total(100.0, discount=10.0)          

def master_function(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

master_function(10, 20, name="Alice", role="Admin")