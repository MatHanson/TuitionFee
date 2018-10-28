'''
This program is designed to prompt the user to choose a language between Python, Java and
C++. It will then prompt the user to input number of lessons, additional hours and number
of tests taken. The program will then compute the fees for each of these as well as the
overall tuition fee and then display these fees to the user.
'''

# Create a variable to control the loop and assign 'y' so that the program runs at least once
again = 'y'

# Main function
def main():
    # Call get_language function
    language = get_language()

    # Input validation loop for language choice. If either of the three choices are not
    # entered, a loop occurs.
    while language not in ['Python', 'Java', 'C++']:
        print('Invalid input')
        language = get_language()

    # If Python is entered, the following code is run.
    if language == 'Python':
        # Call set_fee_constants function passing the fees as arguments
        set_fee_constants(300, 200, 250)

        # Call get_number_of_lessons function
        get_number_of_lessons()
        # Input validation loop, number_of_lessons must be >= 5
        while number_of_lessons < 5:
            get_number_of_lessons()
            
        # Call get_number_of_additional_hours function
        get_number_of_additional_hours()
        # Input validation loop, number_of_additional_hours must be >= 5
        while number_of_additional_hours < 5:
            get_number_of_additional_hours()

        # Call get_number_of_tests function
        get_number_of_tests()
        # Input validation loop, number_of_tests must be >= 5
        while number_of_tests < 5:
            get_number_of_tests()
        
        print('')

        # Call calculate_fees function
        calculate_fees()

        # Call display_fees function
        display_fees()

    # If Java is entered, the following code is run.    
    elif language == 'Java':
        # Call set_fee_constants function passing the fees as arguments
        set_fee_constants(200, 150, 150)

        # Call get_number_of_lessons function
        get_number_of_lessons()
        # Input validation loop, number_of_lessons must be >= 4
        while number_of_lessons < 4:
            get_number_of_lessons()
            
        # Call get_number_of_additional_hours function
        get_number_of_additional_hours()
        # Input validation loop, number_of_additional_hours must be >= 10
        while number_of_additional_hours < 10:
            get_number_of_additional_hours()

        # Call get_number_of_tests function
        get_number_of_tests()
        # Input validation loop, number_of_tests must be >= 2
        while number_of_tests < 2:
            get_number_of_tests()
        
        print('')

        # Call calculate_fees function
        calculate_fees()

        # Call display_fees function
        display_fees()

    # If C++ is entered, the following code is run.    
    elif language == 'C++':
        # Call set_fee_constants function passing the fees as arguments
        set_fee_constants(175, 175, 170)

        # Call get_number_of_lessons function
        get_number_of_lessons()
        # Input validation loop, number_of_lessons must be >= 6
        while number_of_lessons < 6:
            get_number_of_lessons()
            
        # Call get_number_of_additional_hours function
        get_number_of_additional_hours()
        # Input validation loop, number_of_additional_hours must be >= 7
        while number_of_additional_hours < 7:
            get_number_of_additional_hours()

        # Call get_number_of_tests function
        get_number_of_tests()
        # Input validation loop, number_of_tests must be >= 2
        while number_of_tests < 2:
            get_number_of_tests()
        
        print('')

        # Call calculate_fees function
        calculate_fees()

        # Call display_fees function
        display_fees()

    # Call loop_again function
    again = loop_again()

# Function for defining the fee constants
def set_fee_constants(fee1, fee2, fee3):
    # Setting global constants for use outside of function
    global LESSON_FEE
    global ADDITIONAL_HOUR_FEE
    global TEST_FEE

    # Constants assigned by function arguments
    LESSON_FEE = fee1
    ADDITIONAL_HOUR_FEE = fee2
    TEST_FEE = fee3

# This function will request the user to input a language choice
def get_language():
    # Input a language choice
    language = str(input('Enter the name of the programming language (Python, Java, or C++): '))
    
    # Return the chosen language
    return language

# This function will request the user to input number of lessons
def get_number_of_lessons():
    # Setting global variable for use outside of function
    global number_of_lessons
    
    # Input number of lessons, using an exception for int data type
    while True:
        try:
            number_of_lessons = int(input('Enter the number of lessons: '))
        except ValueError:
            continue
        else:
            break
        
#This function will request the user to input additional hours of study
def get_number_of_additional_hours():
    # Setting global variable for use outside of function
    global number_of_additional_hours

    # Input number of additional hours, using an exception for int data type
    while True:
        try:
            number_of_additional_hours = int(input('Enter the additional hours: '))       
        except ValueError:
            continue
        else:
            break

# This function will requestthe user to input number of tests
def get_number_of_tests():
    # Setting global variable for use outside of function
    global number_of_tests
    
    # Input number of tests, using an exception for int data type
    while True:
        try:
            number_of_tests = int(input('Enter the number of tests: '))
        except ValueError:
            continue
        else:
            break
        
#This function will calculate fee totals
def calculate_fees():
    # Setting global variable for use outside of function
    global lesson_fee_total
    global additional_hour_fee_total
    global test_fee_total
    global tuition_total
    
    # Calculate the fee totals
    lesson_fee_total = LESSON_FEE * number_of_lessons
    additional_hour_fee_total = ADDITIONAL_HOUR_FEE * number_of_additional_hours
    test_fee_total = TEST_FEE * number_of_tests
    tuition_total = lesson_fee_total + additional_hour_fee_total + test_fee_total

# This function will display the calculated totals
def display_fees():
    print('Tuition fee for the lessons (in dollars):', lesson_fee_total)
    print('Tuition fee for additional hours (in dollars):', additional_hour_fee_total)
    print('Tuition fee for the tests (in dollars):', test_fee_total)
    print('')
    print('Total tuition fee (in dollars):', tuition_total)
    print('')

# This function will prompt the user if they want to run the program again
def loop_again():
    # Setting global variable for use outside of function
    global again
    # Prompt user if another computation is required
    again = str(input('Do you want to compute the tuition fee for another student? '))
    # Return the input
    return again

# Display header
print("""----------------------------------------------------------------------------------------------
Welcome to Dr Ho Coaching Centre
-----------------------------------------------------------------------------------------------""")

# Call main function if loop variable "again" = y
while again in ['y', 'Y']:
    print('')
    main()

print('')    
print('Good Bye.')
