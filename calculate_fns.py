def calculate_basic_operations(array):
    try:  
        if array [1] == "+":
            result = array[0] + array[2]
            return(result)

        if array [1] == "-":
            result = array[0] - array[2]
            return(result)

        if array [1] == "*":
            result = array[0] * array[2]
            return(result)

        if array [1] == "/":
            result = array[0] / array[2]
            return(result)
    except ZeroDivisionError:
        print("Cannot be divided by zero")

    except Exception:
        pass
    
def obtine_values(array):
    array[0] = int(array[0]) 

    array[2] = int(array[2]) 