from calculate_fns import calculate_basic_operations
from calculate_fns import obtine_values

result = None

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
    
        #Getting the data    
    
        try:
        
            print("Enter the numbers and the symbol of the operation that you want to execute separated by espaces. As follows: 5 + 7")
        
            data_enter = input()
        
            data = data_enter.split(" ")
    
            #Checking data
    
            if len(data) > 3:
            
                print("You entered an unnecessary value")
            
                print("Enter the numbers and the symbol of the operation that you want to execute separated by espaces. As follows: 5 + 7")
            
                data_enter = input()
            
                data = data_enter.split(" ")
            
        except Exception:
        
            print("You have entered an incorrect value")
    

        # Value recollection
        
        try:
        
            obtine_values(data) 
        
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

    #Checking for a result
    
    elif option == 2 and result == None:
    
        print("There is not a result to work")

    elif option == 2 and result != None:
        
        #Getting data    
        
        try:
    
            print("Enter the symbol and the number separated by spaces to perform the operation with the result.")
            
            result_list = []
            
            result_list.append(result)
        
            data_enter = input()
        
            data = data_enter.split(" ")
        
            result_list.append(data[0])
            
            result_list.append(data[1])
            
            #Checking data
            
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
            #Obtine values
            
            obtine_values(result_list)
    
        except Exception:
    
            print("You have entered an incorrect value") 

        try:
            
            #Make operations with the result
            
            result = calculate_basic_operations(result_list)
            
            print(calculate_basic_operations(result_list))
        
        except ZeroDivisionError:
            
            print("Cannot be divided by zero")
    
    #Break the cycle
    elif option == 3:
        
        break

    
    