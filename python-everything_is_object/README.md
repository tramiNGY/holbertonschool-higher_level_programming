
# Python3: Mutable, Immutable... everything is object!

## 1) Introduction
In Python, everything is an object. To write clean and efficient code, it's really important to understand how these objects work, how they're stored in memory, and how variables point to them.

This project mentions the fundamental concepts of object identity, mutability, and how Python handles assignment and function arguments, with examples and explanations.
## 2) Id and type
Every object in Python has:
- A **type**, which defines what kind of object it is. It identifies the type of data that a variable can store.

![python types](https://miro.medium.com/v2/resize:fit:1400/1*QfI8H_8HplGa1v9IrrWjBA.png)
- An **identity**, which is an object's unique memory address
The id() function returns a unique id for the specified object. All objects in Python has its own unique id. The id is assigned to the object when it is created.
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? No. (by adding + [5], python creates a new list so a points to a new object (new id))
```
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Yes. (Here, += modifies the object in place (same id))
```
To compare objects:

- **==**: to check if two objects's values are indentical (content of the object)
```
>>> a = 89
>>> b = a
In the following code, do a and b point to the same object? Yes (when assigning a variable to another (b = a), the two variables point to the same object and if the object is mutable, if it is modified via one variable, the other variable will also see the modification)
```
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2) # True (same value)
```
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2) # True (same value)
```
- **is**: to check if two variables point to the same object in memory (entity of the object, memory reference)
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2) # False (str with a space no interning, two distinc str objects created)
```
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2) # False (same value but when assigning a list, creates new object)
```
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2) # True (Asigning l2 to same object than l1)
```
![mutable immutable](https://storage.googleapis.com/algodailyrandomassets/curriculum/blogs/mutablevsimm.png)
## 3) Mutable objects
Mutable objects can be modified in place (after their creation), their contents can be changed without changing their identity (no new object created).
**In-place operations** (like +=, .append(), .update()) will change the object without changing its id().

Common mutable types:
- list
- dict
- set
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2) # [1, 2, 3, 4]
print(l1 == l2) # True (same value)
print(l1 is l2)  # True - l1 and l2 have the same memory addess

# A List is a mutable object so the object's value can be changed in place.
```
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2) # [1, 2, 3]

# step 1 -l1 points to list object [1, 2, 3]
# step 2 - l1 is assigned to l2 so l2 now points to the same object as l1 [1, 2, 3]
# step 3 - + [4] creates a new list, l1 references this new object and points to new list [1, 2, 3, 4]
# step 4 - l1 still references the same list object [1, 2, 3]
```
## 4) Immutable objects
Immutable objects cannot be modified once they are created. Any operation that changes an immutable value creates a new object in memory (new instance).

Common immutable types:
- int
- float
- str
- tuple
- bool
```
a = 89
b = a + 1

print(a)  # 89
print(b)  # 90

# step 1 - read a's value (89)
# step 2 - Calculate a + 1 (90 which is a new int since int are immutable (89 cannot be changed))
# step 3 - Assign this new value (90) to b so b points to this new object in memory
```
Even though a += 1 looks like an in-place modification, for immutable types, it always creates a new object.
## 5) Why does it matter and how differently does Python treat mutable and immutable objects
Knowing whether an object is mutable or not helps you:
- Avoid unintended side effects
- Predict the outcome of assignments and function calls
- Debug issues where multiple variables seem to “change together”
### In-Place vs Out-of-Place Modifications
| Operation | Behavior | Affects Object Identity ?
| :----------: |:---------------:|:---------------:|
| a += [4] (list) | In-place modification| No new object
| a = a + [4] | Out-of-place (new object)| New object created
| a += 1 (int) | New object created| New object |

## 6) How arguments are passed to functions and what does that imply for mutable and immutable objects
![pass by reference](https://miro.medium.com/v2/resize:fit:572/1*0Z1bXtvFVj5RIhn0EfFNAQ.png)


Python uses **pass-by-object-reference**, also called pass-by-assignment.
- The object itself is passed to the function, not a copy.
- If the object is mutable, modifications inside the function affect the original.
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l) # [1, 2, 3, 4]

# step 1 - l = [1, 2, 3] is a list (mutable)
# step 2 - incremet(l) calls the function and passes the reference to the same list object
# step 3 - inside the function, N.append(4) adds 4 to the original list (in-place modification)
(l gets modified directly)
```
- If the object is immutable, changes won't reflect outside the function.
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a) # 1

# step 1 - a = 1 is an int (immutable)
# step 2 - increment(a) sends the value of a (1) into the function
# step 3 - inside the function, n +=1 creates a new int (2) but only inside the function scope (it does'nt affect a outside the function)
```
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1) # [1, 2, 3]

# step 1 - l1 and l2 are mutable list objects
# step 2 - assign_value(l1, l2) - n receives the reference to l1 and v to l2
# step 3 - inside function n = v - n now points to l2 (same reference as v)
# l1 outside the function still points to same object [1, 2, 3]

```
## 7) Interning and Singleton
![interning](https://towardsdatascience.com/wp-content/uploads/2020/08/12bCl5cSdmLdcdcu4SJ7yZA.png)
A singleton in Python refers to a value for which only one instance exists in memory. So any time you create that value, Python gives you a reference to the same object. Python only creates one shared instance of () in memory to save space and improve performance.

Example of singletons:
- None
- True and False
- Empty typle ()
- Small integers (<-5 < < 256)
- Some short string (sometimes interned)
Interning means that Python reuses identical objects by creating only one instance in memory for objects with the same value.
```
>>> a = 89
>>> b = 89
In the following code, do a and b point to the same object? Yes (int: -5 < 89 < 256)

```
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2) # True (str: simple short string withoutspace)
```
```
a = ()
b = ()
a is b # True (a and b are both empty tuple which is a singleton so same reference)
```
## 8) Garbage Collector
![garbage collector](https://miro.medium.com/v2/resize:fit:1400/0*7H9I427eldrykVMn.png)
The garbage collector (GC) in Python is an automated process that frees memory of objects that are unused (not referenced by any variable). It acts in the background and maintains memory's management efficiently without the need to handle it (unlike C/C++).
```
l1 = [1, 2, 3, 4] # l1 points to the list object [1, 2, 3, 4]
l1 = l1 + [5] # new list object is created and the reference of l1 is updated to point to [1, 2, 3, 4, 5].
# The old list [1, 2, 3, 4] is no longer referenced and becomes admissible to be fetched by the garbage collector unless it was also assigned to it by another variable.

# Remark case
l2 = [1, 2, 3, 4] # A new list object is created which l2 points to (l2 doesn't point to the former list [1, 2, 3, 4] that l1 was pointed to before, this list stays unreferenced)
```
