# 6: Conditions - If elif and else statements  

### Overview
How to use if elif and else statements , also some false values to look out for , also , and or and not
### Key Concepts
## Comparisons:
- Equal:            ==
- Not Equal:        !=
- Greater Than:     >
- Less Than:        <
- Greater or Equal: >=
- Less or Equal:    <=
- Object Identity:  is


## False Values:
- False
- None
- Zero of any numeric type
- Any empty sequence. For example, '', (), [].
- Any empty mapping. For example, {}.

### Important Details
> Look out for 0s because you might not want it to return false when value is 0 sometimes
### Examples
- If , elif and else with != , and in one code:
  ```python
    value = "water"
    if value == 'water' and value != "fire":
        print("Value is water")
    elif value != "water":
        print("Value is not water")
    else:
        print("Error")