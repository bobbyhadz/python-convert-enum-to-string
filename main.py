# Convert an Enum to a String in Python

from enum import Enum


class Color(Enum):
    RED = 'stop'
    GREEN = 'go'
    YELLOW = 'get ready'


# 👇️ Human-readable string representation
print(Color.RED)  # 👉️ Color.RED

# 👇️ repr() shows the value as well
print(repr(Color.RED))  # 👉️ <Color.RED: 'stop'>

# 👇️ Get the name of enum
print(Color.RED.name)  # 👉️ RED

# 👇️ Get the value of enum
print(Color.RED.value)  # 👉️ stop

# 👇️ If the enum value is int, you can convert it to str
print(str(Color.RED.value))  # 👉️ stop