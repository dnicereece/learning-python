# Implicit type conversions

# int to float
a = 5      # int
b = 2.0    # float
result = a + b  
print(result)   

print(type(result))  # Check the type of result

# Explicit type conversions

# str to int
num_str = "42"
num_int = int(num_str)  # Converts string to integer
print(num_int)

print(type(num_int))  # Check the type after conversion

# int to float
num_int = 7
num_float = float(num_int)  # Converts integer to float
print(num_float) 

print(type(num_float))  # Check the type after conversion

# Explicit conversion to str
num = 3.14
num_str = str(num)          # Converts float to string
print(num_str)  

print(type(num_str))  # Check the type after conversion