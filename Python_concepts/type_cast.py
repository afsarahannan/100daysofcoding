# age : int
# name : str
# height: float
# is_human : bool

def police_check(age:int)->bool:
    if age >= 18:
        statement = True
        print("You are good to go")
    else:
        statement = False
        print("Show me some ID")
    return statement

police_check(22)


