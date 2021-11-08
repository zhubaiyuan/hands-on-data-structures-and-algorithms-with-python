# create an empty tuple
t = tuple()
print("Type of tuple t is ", type(t))


# create a tuple with 1 element
t = ('a',)
print("print tuple t is", t)
print('type of t is ', type(t))


tpl = ('a', 'b', 'c')
print("print another tuple", tpl)
print("another way to create a tuple", tuple('sequence'))


# multiple assignment
x, y, z = tpl
print("value of element x in tuple is", x)
print("value of element x in tuple is", y)
print("value of element x in tuple is", z)
print('a' in tpl)  # Membership can be tested
print('z' in tpl)


# braces are optional
tupl = 1, 2, 3, 4, 5
print("tuple value at index 1 is", tupl[1])
print("tuple[1:3] is ", tupl[1:3])


# tuple concatenation
tupl2 = (11, 12, 13)
tupl3 = tupl + tupl2
print("Tuple concatenation", tupl3)
print("Tuple repetition is", tupl*2)      # repetition for tuples
print("membership test", 5 in tupl)    # membership test
print("Tuple negative indexing", tupl[-1])     # negative indexing
print("Length of tuple is ", len(tupl))   # length function for tuple
print("Maximum value in tuple is", max(tupl))
print("Minimum value in tuple is", min(tupl))
print(tupl == tupl2)
print(tupl > tupl2)
