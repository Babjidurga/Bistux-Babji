# First question answer



a = input().split(" ")
for i in range(len(a)):
    if a[i][0] == "a":
        a[i] = "****"
print(" ".join(a))

# Second qusetion answer
def group_by_first_letter(string):
    dic = {}
    for wor in string:
        first = wor[0]
        if first not in dic:
            dic[first] = []
        dic[first].append(wor)
    order = sorted(dic.items())
    return order

b = input().split(" ")
get = group_by_first_letter(b)
print([(words) for letter,words in get])
        