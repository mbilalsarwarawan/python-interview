# 🎯 In-Depth Python Variable & int Type Interview Questions

# ✅ Q1. How does variable assignment work in Python?
x = 5
print(id(x))  # Memory address (object id)

x = x + 1
print(id(x))  # Different id - integers are immutable, so new object is created

# ✅ Q2. What happens when two variables reference the same int object?
a = 10
b = 10
print(a is b)  # True - small integers are cached by Python (-5 to 256)

# ✅ Q3. Demonstrate the difference between `is` and `==` with integers
a = 257
b = 257
print(a == b)  # True (value equality)
print(a is b)  # False (different objects outside caching range)

# ✅ Q4. Are integers mutable in Python?
def try_modifying(n):
    print("Inside before:", id(n))
    n += 1
    print("Inside after:", id(n))

x = 100
print("Outside before:", id(x))
try_modifying(x)
print("Outside after:", id(x))

# Output: New object created inside the function

# ✅ Q5. What is integer interning and how does it affect performance?
a = 100
b = 100
c = 1000
d = 1000
print(a is b)  # True (cached)
print(c is d)  # False (not cached)

# ✅ Q6. Variable Rebinding with integers
x = 10
y = x
x = 20
print(y)  # 10 - integers are immutable, rebinding doesn’t affect y

# ✅ Q7. How do `globals()` and `locals()` affect variable access?
a = 99
print("globals: ", globals()['a'])

# Inside function:
def test_scope():
    a = 42
    print("locals: ", locals())

test_scope()

# ✅ Q8. Using int with `isinstance` and `type`
x = 7
print(isinstance(x, int))  # True
print(type(x) == int)      # True

# ✅ Q9. Can we override the int type or shadow it?
int = 5
print(int)  # 5 - don't shadow built-ins in real code!
del int  # Always clean up if you do

# ✅ Q10. What happens with arithmetic on int?
a = 2**63
print(a)  # Python handles arbitrary precision
print(type(a))  # Still <class 'int'>

# ✅ Q11. Can an int be used as a key in a dictionary?
d = {}
d[10] = 'value'
print(d[10])  # 'value' — int is hashable and immutable, so valid key

# ✅ Q12. How does int behave in a function call?
def square(n):
    n *= n
    return n

x = 6
print(square(x))  # 36
print(x)          # 6 - original unchanged due to immutability

# ✅ Q13. How to force an integer type from input or float
x = int("42")
y = int(3.99)   # Truncated to 3
z = int(True)   # 1

# ✅ Q14. What are edge-case behaviors of int division?
print(5 / 2)    # 2.5 - true division (float)
print(5 // 2)   # 2   - floor division (int)

# ✅ Q15. Can we extend int with subclassing?
class MyInt(int):
    def is_even(self):
        return self % 2 == 0

x = MyInt(4)
print(x.is_even())  # True
