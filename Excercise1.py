#write a function  to get list of even numbers from the given list.
inputList = [1,3,4,5,6,8,10,12,13,12]

def get_even_numbers(lst: list): 
    output = []
    for x in lst:
        if x%2==0:
            output.append(x)
    return output

print(get_even_numbers(inputList))