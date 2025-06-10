# ✅ Python Variables Cheatsheet for Interview Coding Questions

# 📌 1. Declaring Variables
x = 10              # Integer
name = "Alice"       # String
is_valid = True      # Boolean
pi = 3.14            # Float

# 📌 2. Multiple Assignment
a, b, c = 1, 2, 3    # Multiple values at once
x = y = z = 0        # Same value to multiple variables

# 📌 3. Swapping Variables Without Temp Variable
a, b = b, a

# 📌 4. Constants (By Convention Only)
PI = 3.14159         # Constants are uppercase (not enforced)

# 📌 5. Type Conversion / Casting
x = int("5")          # String to int
s = str(123)          # Int to string
f = float("2.5")      # String to float
b = bool(1)           # Int to bool (0 = False, else True)

# 📌 6. Variable Scope
global_var = "I am global"

def some_func():
    local_var = "I am local"
    global global_var
    global_var = "Modified globally"

# 📌 7. Dynamic Typing
value = 5             # int
value = "Now a string" # Python allows reassigning different types

# 📌 8. Unpacking Collections
lst = [1, 2, 3]
a, b, c = lst

# 📌 9. Using Underscores
_ = "ignore value"
first_name, _, last_name = ("John", "Middle", "Doe")

# 📌 10. Variable Naming Rules
# - Must start with a letter or underscore (_)
# - Can contain letters, digits, and underscores
# - Case-sensitive: myVar != myvar

# 📌 11. Temporary Variables for Looping
for i in range(5):
    temp_result = i * 2
    print(temp_result)

# 📌 12. Using `globals()` and `locals()`
# Dynamically access variables (not common in interviews)
my_var = 100
print(globals()['my_var'])

# 📌 13. Deleting Variables
del x  # Deletes x

# 📌 14. Checking if Variable Exists
try:
    x
except NameError:
    x = 0  # Default value if not exists

# 📌 15. Python is Pass-by-Object-Reference
# Mutable objects can be modified inside functions

def append_item(lst):
    lst.append(99)

my_list = [1, 2, 3]
append_item(my_list)  # my_list is now [1, 2, 3, 99]

# 📌 16. Mutability of Data Types
# Immutable: int, float, bool, str, tuple
# Mutable: list, dict, set

x = 5
print(id(x))
x += 1
print(id(x))  # New object created

l = [1, 2, 3]
print(id(l))
l.append(4)
print(id(l))  # Same object modified

# 📌 17. In-Depth Interview Examples

# Example 1: Function side-effect with mutable argument
def modify_list(lst):
    lst.append("new")

data = ["original"]
modify_list(data)
print(data)  # ['original', 'new'] - shows mutability

# Example 2: Function with immutable argument
def modify_string(s):
    s += " changed"
    return s

text = "hello"
result = modify_string(text)
print(text)   # 'hello' - original unchanged
print(result) # 'hello changed'

# Example 3: Variable scope trap
def outer():
    count = 0
    def inner():
        # Uncommenting below will cause UnboundLocalError without 'nonlocal'
        # count += 1
        pass
    inner()
    return count

print(outer())

# Example 4: Global variable trap
def use_global():
    global x
    x = 42
use_global()
print(x)  # 42
