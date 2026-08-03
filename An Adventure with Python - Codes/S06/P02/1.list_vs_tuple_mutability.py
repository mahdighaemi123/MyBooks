# A list is mutable (can change)
mutable_list = [10, 20]
mutable_list.append(30)  # This works!
print("Mutable list:")
print(mutable_list)

# A tuple is immutable (cannot change)
# Tuples are defined using parentheses ()
immutable_tuple = (10, 20)
print("Immutable tuple:")
print(immutable_tuple)

# If you try to change a tuple, you get an ERROR!
# immutable_tuple.append(30) # This will crash the code! (AttributeError)
