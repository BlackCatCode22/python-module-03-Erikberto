#Module 3
#list_of_numbers
#eS 3/22/25
#CIT-95 spring25

numbers = []
while True:
    user_input =input(f"Enter numbers, then enter 'done' when finished.")
    if user_input=='done':
        break
    try:
        number=float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input.")
        #continue
    if numbers:
        print("Max:",max(numbers))
        print("Min:",min(numbers))
