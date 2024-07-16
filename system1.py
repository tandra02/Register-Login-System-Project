# Create a function named maintain_set that receives a set of integers, and an integer.
# The function will check if the integer is in the set, if it is, it will return that integer multiplied by 2. If it is not in the set, it will insert it and return the set.

def maintain_set(a_set, number):
    # Your code here
    if number in a_set:
        return number * 2
    else:
        a_set.add(number)
        return a_set
    
print(maintain_set({1, 5, 2, 4},2))   # 4
print(maintain_set({1, 2},3))         # {1,2,3}
print(maintain_set(set(),2))          # {2}