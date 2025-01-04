result = int
try:
    print("Enter the numbers and the symbol of the operation that you want to execute separated by espaces. As follows: 5 + 7")
    data_enter = input()
    data = data_enter.split(" ")
    print(data)

    if len(data) > 3:
        print("You entered an unnecessary value")
        print("Enter the numbers and the symbol of the operation that you want to execute separated by espaces. As follows: 5 + 7")
        data_enter = input()
        data = data_enter.split(" ")
        print(data)
        
except Exception:
    print("You have entered an incorrect value")
    

try:
    data[0] = int(data[0]) 

    data[2] = int(data[2]) 
except ValueError:
    print("You have entered an incorrect value") 

try:
    if data [1] == "+":
        result = data[0] + data[2]
        print(result)

    if data [1] == "-":
        result = data[0] - data[2]
        print(result)

    if data [1] == "*":
        result = data[0] * data[2]
        print(result)

    if data [1] == "/":
        result = data[0] / data[2]
        print(result)
except ZeroDivisionError:
    print("Cannot be divided by zero")

except Exception:
    pass

while True is True:
    print("Select a option: ")
    print("1: Another operation")
    print("2: Continue working with the result")
    print("3: Exit")
    option = input()
    option = int(option)
    
    if option == 1:
        try:
            print("Enter the numbers and the symbol of the operation that you want to execute separated by espaces. As follows: 5 + 7")
        
            data_enter = input()
        
            data = data_enter.split(" ")

            if len(data) > 3:
            
                print("You entered an unnecessary value")
            
                print("Enter the numbers and the symbol of the operation that you want to execute separated by espaces. As follows: 5 + 7")
            
                data_enter = input()
            
                data = data_enter.split(" ")
            
        except Exception:
            print("You have entered an incorrect value")
    

        try:
            data[0] = int(data[0]) 

            data[2] = int(data[2]) 
        except ValueError:
            print("You have entered an incorrect value") 

        try:
            if data [1] == "+":
                result = data[0] + data[2]
                print(result)

            if data [1] == "-":
                result = data[0] - data[2]
                print(result)

            if data [1] == "*":
                result = data[0] * data[2]
                print(result)

            if data [1] == "/":
                result = data[0] / data[2]
                print(result)
        
        except ZeroDivisionError:
            print("Cannot be divided by zero")

    if option == 2:
        try:
            print("Enter the symbol and the number separated by spaces to perform the operation with the result.")
            result_list = []
            result_list.append(result)
        
            data_enter = input()
        
            data = data_enter.split(" ")
        
            result_list.append(data[0])
            result_list.append(data[1])
            print(result_list)
            if len(result_list) > 3:
            
                print("You entered an unnecessary value")
            
                print("Enter the numbers and the symbol of the operation that you want to execute separated by espaces. As follows: 5 + 7")
            
                result_list = []
                result_list.append(result)
        
                data_enter = input()
        
                data = data_enter.split(" ")

                result_list.append(data)
                print(result_list)
        except Exception:
            print("You have entered an incorrect value")

        try:
            result_list[0] = int(result_list[0]) 

            result_list[2] = int(result_list[2]) 
        except ValueError:
            print("You have entered an incorrect value") 

        try:
            if result_list [1] == "+":
                result = result_list[0] + result_list[2]
                print(result)

            if result_list [1] == "-":
                result = result_list[0] - result_list[2]
                print(result)

            if result_list [1] == "*":
                result = result_list[0] * result_list[2]
                print(result)

            if result_list [1] == "/":
                result = result_list[0] / result_list[2]
                print(result)
        
        except ZeroDivisionError:
            print("Cannot be divided by zero")
    
    if option == 3:
        break
    
    