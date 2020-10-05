# problem: does a string have all unique characters
# input: input_string
# output: True: if string is unique, else False

# test cases

def slow_unique(input_string):
    # sort the string
    sorted_input = sorted(input_string)
    # for each character in the string
    for i in range(len(sorted_input)):
        if i < len(sorted_input)-1:
            # check next character, are they the same?
            if sorted_input[i] == sorted_input[i+1]:
                # if yes, return False
                return False
            # else return True
    return True

if __name__ == "__main__":
    print(unique('helo'))
    print(unique('hello'))