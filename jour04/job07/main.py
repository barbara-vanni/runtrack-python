L = [8, 24, 48, 2, 16]
print(L)

def filter_multiples_of_three(lst):
    new_list = [num for num in lst if num % 3 == 0]
    return new_list

L = filter_multiples_of_three(L)
print("Multiples de 3:", L)