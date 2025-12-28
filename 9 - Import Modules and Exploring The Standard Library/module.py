print("Module Imported")
def find_index(string,index):
    for i,value in enumerate(string):
        if value == index:
            return i
    return False 