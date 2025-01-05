from calculate_fns import calculate_basic_operations


result = int

while True is True:
    # Option selection
    print("Select an option: ")
    print("1: Make an operation")
    print("2: Continue working with the result")
    print("3: Exit")
    option = input()
    try:
        option = int(option)
    except Exception:
        print("You have entered an incorrect option")
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
    

        # Value recollection
        try:
            data[0] = int(data[0]) 

            data[2] = int(data[2]) 
        except Exception:
            print("You have entered an incorrect value") 

        try:
           # Make an operation 
            result = calculate_basic_operations(data)
            print(calculate_basic_operations(data))
        
        except ZeroDivisionError:
            print("Cannot be divided by zero")
        except Exception:
            pass

    elif option == 2:
        try:
            print("Enter the symbol and the number separated by spaces to perform the operation with the result.")
            result_list = []
            result_list.append(result)
        
            data_enter = input()
        
            data = data_enter.split(" ")
        
            result_list.append(data[0])
            result_list.append(data[1])

            if len(result_list) > 3:
            
                print("You entered an unnecessary value")
            
                print("Enter the numbers and the symbol of the operation that you want to execute separated by espaces. As follows: 5 + 7")
            
                result_list = []
                result_list.append(result)
        
                data_enter = input()
        
                data = data_enter.split(" ")

                result_list.append(data)

        except Exception:
            print("You have entered an incorrect value")

        try:
            result_list[0] = int(result_list[0]) 

            result_list[2] = int(result_list[2]) 
        except Exception:
            print("You have entered an incorrect value") 

        try:
            result = calculate_basic_operations(result_list)
            print(calculate_basic_operations(result_list))
        
        except ZeroDivisionError:
            print("Cannot be divided by zero")
    
    elif option == 3:
        break
    
    else:
        print("You have not placed a correct option")
    
    