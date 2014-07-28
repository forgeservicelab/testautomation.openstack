def size(arr):
        return len(arr)

def Compare_Ignore_Case(s1, s2):
    if s1.lower() != s2.lower():
        return True
    else:
        return False
    
def To_First_Upper(s1):
    return s1[:1].upper() + s1[1:].lower()