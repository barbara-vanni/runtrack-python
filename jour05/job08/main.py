List = [78,45,92,32,67,89,14,53,76,41,60,85,23,94,50]

def bubble_sort(List):
    n = len(List)
    for i in range(n):
        sort = True
        for j in range(0, n - i - 1):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]
                sort = False
        if sort:
            break
    return (List)

list_sort = bubble_sort(List)

print("Liste triée:", list_sort)