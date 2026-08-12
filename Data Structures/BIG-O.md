
-----------
# **BIG - O**
-----------

2 IMPORTANT QUESTIONS 

## 1. How much **TIME** does the algorithm need to finish?

## 2. How much **SPACE** does this algorithm need for its computation?

> **BIG-O**
1. ***Only cares about the worst case***
2. ***Only cares when input becomes large*** {second}
>

# WE USE A NOTATION FOR THIS
 
![Complexity-Time](./images/Complexity-Time.png)
**We can visualize it as:**

![Graphic](https://imgs.search.brave.com/k45umg6rIRkt659BY7GnxsFEvw8qHQ2dTKSK3QKAuH8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdWJz/dGFja2Nkbi5jb20v/aW1hZ2UvZmV0Y2gv/JHNfIVZydm0hLHdf/MTQ1NixjX2xpbWl0/LGZfYXV0byxxX2F1/dG86Z29vZCxmbF9w/cm9ncmVzc2l2ZTpz/dGVlcC9odHRwczov/L3N1YnN0YWNrLXBv/c3QtbWVkaWEuczMu/YW1hem9uYXdzLmNv/bS9wdWJsaWMvaW1h/Z2VzL2M5ODU1YmNm/LTk5NGQtNDNiNi05/ZmM0LWY4MDU3NGMx/NzgyZV8xMTk0eDgx/MC5wbmc)

# Properties

So as we said before **BIG O** only cares if input is too large
EXAMPLES:
> **O (N + C) = O(N)**
> **O (CN) = O(N), C>0**
> 
##### C is constant so we can ignore it 

But lets see how this works with a function
![Function](./images/function-BigO.png)
**The highest exponential here is 3 so we can ignore the rest and keep the highest exponential as our BIG O**