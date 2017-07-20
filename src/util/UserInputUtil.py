#Function to validate integer input type from user
'''
INPUT

message=message to be shown when to ask for the input

'''
def intergerValidationOnInput(message):
    while True:
        try:
            return int(input(message))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


#Function to validate input type from user with only valid values
'''
INPUT

message=message to be shown when to ask for the input
valid_values=List of valid values which is acceptable or are valid inputs

'''
def textValidationOnInput(message,valid_values=[]):
    while True:
        try:
            input_value=input(message);
            input_value_valid="false";
            for x in valid_values:
                if input_value==x:
                    input_value_valid="true";
            if input_value_valid=="false":
                raise Exception('invalidValue', 'Please enter only valid values')
            else:
                return input_value
        except Exception as inst:
            x,y=inst.args
            print(y)





