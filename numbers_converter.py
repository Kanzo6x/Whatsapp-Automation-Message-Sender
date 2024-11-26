import unicodedata

def remove_control_characters(input_string):
    return ''.join(ch for ch in input_string if unicodedata.category(ch)[0] != "C")

file_name = 'numbers.txt'

size = int(input('total numbers that you want to store :'))

with open(file_name, 'w', encoding='utf-8') as file:
    for i in range(size):

        number = input(f"Enter number {i+1}: ").strip()
        cleaned_number = remove_control_characters(number)
        file.write(f'+2{cleaned_number}\n')

print(f"All {size} numbers have been written to {file_name} successfully!")
