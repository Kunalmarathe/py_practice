# def Addition(No1, No2, No3, No4):
#     Ans = No1 + No2 + No3 + No4
#     return Ans

# Result = Addition(10, 20, 30)
# print(Result)

# New variation

def Addition(*No):
    print(type(No)) # type is tuple. It is sequence data type
    print(len(No))
    Ans = 0

    for i in No:
        Ans = Ans + i

    return Ans

Result = Addition(10, 20, 30)
print(Result)

Result = Addition(10, 20, 30, 40)
print(Result)

Result = Addition(10, 20, 30, 40, 50)
print(Result)