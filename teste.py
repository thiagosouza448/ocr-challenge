def most_frequent(List):
    return max(set(List), key = List.count)
 
List = ["127172", "127172", "222", 2, 1, 3]
print(most_frequent(List))