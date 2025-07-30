import math as m
# taking input as degree
safe_functions = {
    'sin': lambda x: m.sin(m.radians(x)),
    'cos': lambda x: m.cos(m.radians(x)),
    'tan': lambda x: m.tan(m.radians(x)),
    'cot': lambda x: 1 / m.tan(m.radians(x)),
    'sec': lambda x: 1 / m.cos(m.radians(x)),
    'cosec': lambda x: 1 / m.sin(m.radians(x)),
    'sqrt': m.sqrt,
    'log': m.log10,
    'pi': m.pi,
    'e': m.e
}



# taking input
while True:
    expr=input("ENTER THE TRIGONOMETRIC EXPRESSION (or done to finish):")
    if expr.lower()=="done":
        print("-"*30)
        print("YOU CHOOSE TO EXIT")
        print("-"*30)
        break
    try:
            result = eval(expr, {"__builtins__": None}, safe_functions)
            print("Result:", round(result, 4))  
    except Exception as e:
            print("Invalid input or error:", e)