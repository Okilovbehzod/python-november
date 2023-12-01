def categorize_numbers(number_list):
    for number in number_list:
        if number > 10:
            print("High Number")
        elif 5<= number <=10:
            print ("Medium Number")
        else:
            print("Low Number")
            print("Low Number")


    number_list = [3, 7, 12, 5, 9]
    categorize_numbers(number_list)


#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC


    def conditional_multiply(number_list, multiply_factor):
        for number in number_list:
            if number > 5:
             print(number * multiply_factor)
        else:
            print(f"Number is not multiplied.")

number_list = [3, 7, 12, 5, 9]
multiply_factor = 2
conditional_multiply(number_list, multiply_factor)

