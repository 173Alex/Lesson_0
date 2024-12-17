# First programm: "Arithmetic"
print("First programm:", 9 ** 0.5 * 5)

# Second programm: "Logics"
print("Second programm:", 9.99 > 9.98 and 1000 != 1000.1)

# Third programm: "School assignment"
priority = 2 * 2 + 2
print("Third programm:")
print("1:", priority)
no_priority = 2 * (2 + 2)
print("2:", no_priority)
print("3:", priority == no_priority)

# Fourth programm: "The first after the dot"
data_str = "123.456"
data_float = float(data_str)
data_int = int(data_float * 10)
first_after_dot = data_int % 10
print("Fourth programm:", first_after_dot)