CheckEven = lambda No : No%2 == 0

Increase = lambda No : No + 1

Add = lambda A,B: A + B


def filterX(Task, Elements):
    Result = [] 

    for no in Elements:
        if(Task(no) == True):
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = []

    for no in Elements:

        Result.append(Task(no))

    return Result

def reduceX(Task, Elements):
    Sum = 0

    for no in Elements:
        Sum = Task(sum, no)
        
    return Sum