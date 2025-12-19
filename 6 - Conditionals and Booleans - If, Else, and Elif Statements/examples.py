# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

value = "water"
if value == 'water' and value != "fire":
    print("Value is water")
elif value != "water":
    print("Value is not water")
else:
    print("Error")

value = "" # A false value
if value:
    print("True")
else:
    print("False")