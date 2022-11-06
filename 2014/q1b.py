lucky_numbers = [i for i in range(1,11000) if i % 2 != 0]
# Replaced with 11000

def remove_numbers(lucky_number,numbers):
    return [numbers[i] for i in range(len(numbers)) if not((i+1) % lucky_number) == 0]

counter = 1
while counter < len(lucky_numbers):
    next_number = lucky_numbers[counter]
    lucky_numbers = remove_numbers(next_number,lucky_numbers)
    counter += 1
    
def find_numbers(number):
    for i in range(len(lucky_numbers)):
        if lucky_numbers[i] > number:
            if number in lucky_numbers:
                #print(lucky_numbers[i-2],lucky_numbers[i])
                return lucky_numbers[i]-lucky_numbers[i-2]
            else:
                #print(lucky_numbers[i-1],lucky_numbers[i])
                return lucky_numbers[i]-lucky_numbers[i-1]

for i in range(2,100):
    if not(i in lucky_numbers):
        print(find_numbers(i))
