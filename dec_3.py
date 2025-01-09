

# ———————————————— Part 1 ————————————————
# Extracting mul operations and suming the result

# mul(X,Y), where X and Y are each 1-3 digit
# many invalid characters that should be ignored
# Adding up the result of each valid mul instruction

# Smallest number has length 8
# Biggest number has length 12

# Loading the corrupted memory
#lines = open('resources/corrupted_memory.txt').read().splitlines()
f = open('resources/corrupted_memory.txt')  # Read the contents of the file into a variable
line_list = f.readlines()
f.close()
# sjekk ut mulighet med "with open('filnavn') as f:"


# Overview data 
#print(line_list)
#print(len(line_list))


# One reason to avoid .strip is that it would could cause what is an inreadable message to become an readable message
# i.e: mul(123,$%56) becomes mul(123,56) which acording to the problem description, in this case, is not a valid mul message in the memory


def first_number_test(line, n):  # n is position of each character in the line
    # note, we already know that the first character is an integer
    # test cases
    a = line[n+5]==','  # one digit number
    b = line[n+5] in '0123456789' and line[n+6] ==','  # two digit number
    c = line[n+5] in '0123456789' and line[n+6] in '0123456789' and line[n+7]==','  # three digit number

    if a:
        number = int(line[n+4])
        return True, number, 1
    elif b:
        number = int(line[n+4] + line[n+5])
        return True, number, 2
    elif c:
        number = int(line[n+4] + line[n+5] + line[n+6])
        return True, number, 3
    else:
        return False, None, None


def last_number_test(line, n, prev_length):  # n is position of each character in the line
    # test cases
    a = line[n+prev_length+2]==')'  # one digit number
    b =  line[n+prev_length+2] in '0123456789' and line[n+prev_length+3] ==')'  # two digit number
    c =  line[n+prev_length+2] in '0123456789' and line[n+prev_length+3] in '0123456789' and line[n+prev_length+4] ==')'  # three digit number

    if line[n+prev_length+1] in '0123456789':
        if a:
            number = int(line[n+prev_length+1])
            return True, number, 1
        elif b:
            number = int(line[n+prev_length+1] + line[n+prev_length+2])
            return True, number, 2
        elif c:
            number = int(line[n+prev_length+1] + line[n+prev_length+2] + line[n+prev_length+3])
            return True, number, 3
        else:
            return False, None, None  # This returns false if none of the test cases match at all, meaning we have an incomplete mul statement
    else:
        return False, None, None  # This returns false if we do not have an integer following the comma that seperates the two numbers
    

def check_text(a_list):
    list_of_sums = []
    for a_line in a_list:
        valid_mul_results = []  # reset this after each new line is completed
        #// We extract the last 12 characters in the line to test them again later, o.w the for n in range would run out of spaces to test 
        # Nono, in this case, the better solutiton is to just add 12 characters at once so that we can if-test the complete line in one go
        #a_line = a_line + '-'*5  # I think this is the minimum
        a_line = a_line + '-'*13  # but to be extra shure i just add 12+1
        
        for n in range(0,len(a_line)-12):  # n is the position of each character in the line.
            # Subtract 12 as to not index out of the list for the largest possible number
            if a_line[n]=='m' and a_line[n+1]=='u' and a_line[n+2]=='l' and a_line[n+3]=='(' and a_line[n+4] in '0123456789':  # Oh lord, forgot a 7 in the number list
                # test first number
                
                first_number_bool, first_number, first_number_length = first_number_test(a_line, n)
                
                if first_number_bool:
                    prev_length = 3+first_number_length+1  # calculate the distance of the last characters from "start", i.e  n
                    
                    # test last number
                    last_number_bool, last_number, last_number_length = last_number_test(a_line, n, prev_length)
                    
                    if last_number_bool:
                        #Multiplication 
                        mul_value = first_number*last_number
                        valid_mul_results.append(mul_value)
        
        # When all valid mul operations has been calculated we sum the result of the current line
        summed_mul_for_line = sum(valid_mul_results)  # Sum all numbers in the list
        list_of_sums.append(summed_mul_for_line)
    
    #print(list_of_sums)
    total_sum = sum(list_of_sums)
    print(f"The total sum is {total_sum}")
    return None


test = ['}?~who()select()-mul(316,505)', 'mul(31x,505)-', 'mul(3,5)-','mul(2,30)-', 'mul(40,50)-', 'mul(100,100-', 'mul(100100-']
# total sum of test is 316*505+3*5+2*30+40*50 = 161655
# NEXT TIME, create a test function with all numbers

# ———— Small test enviroment ————
"""
test_3 = ['mul(316,505)-', 'mul(3,5)-----']  # first is 12 long +1 - to make 13, last one is 8 long +5 - to make 13, now it can be compleatly read

print(len(test[0]), len(test[0])-12, )
test_3 = test[0][:-12]
test_4 = test[0][-12:]
print(test_3)
print(test_4)
"""
# ————

check_text(line_list)
    


# ———————————————— Part 2 ————————————————
# New instructions
# - The do() instruction enables future mul instructions.
# - The don't() instruction disables future mul instructions.
# Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled


# Plan rewrite the function check_text

def check_text_part_2(a_list):
    list_of_sums = []
    mul_operation_bool = True
    for a_line in a_list:
        valid_mul_results = []  # reset this after each new line is completed
        #// We extract the last 12 characters in the line to test them again later, o.w the for n in range would run out of spaces to test 
        # Nono, in this case, the better solutiton is to just add 12 characters at once so that we can if-test the complete line in one go
        #a_line = a_line + '-'*5  # I think this is the minimum
        a_line = a_line + '-'*13  # but to be extra shure i just add 12+1
        
        for n in range(0,len(a_line)-12):  # n is the position of each character in the line.
            # Subtract 12 as to not index out of the list for the largest possible number
            if a_line[n]=='d' and a_line[n+1]=='o' and a_line[n+2]=='(' and a_line[n+3]==')':
                mul_operation_bool = True
            if a_line[n]=='d' and a_line[n+1]=='o' and a_line[n+2]=='n' and a_line[n+3]=="'" and a_line[n+4]=="t" and a_line[n+5]=="(" and a_line[n+6]==")":
                mul_operation_bool = False
            if a_line[n]=='m' and a_line[n+1]=='u' and a_line[n+2]=='l' and a_line[n+3]=='(' and a_line[n+4] in '0123456789' and mul_operation_bool==True:  # Oh lord, forgot a 7 in the number list
                # test first number
                
                first_number_bool, first_number, first_number_length = first_number_test(a_line, n)
                
                if first_number_bool:
                    prev_length = 3+first_number_length+1  # calculate the distance of the last characters from "start", i.e  n
                    
                    # test last number
                    last_number_bool, last_number, last_number_length = last_number_test(a_line, n, prev_length)
                    
                    if last_number_bool:
                        #Multiplication 
                        mul_value = first_number*last_number
                        valid_mul_results.append(mul_value)
        
        # When all valid mul operations has been calculated we sum the result of the current line
        summed_mul_for_line = sum(valid_mul_results)  # Sum all numbers in the list
        list_of_sums.append(summed_mul_for_line)
    
    #print(list_of_sums)
    total_sum = sum(list_of_sums)
    print(f"The total sum is with new conditions {total_sum}")
    return None


check_text_part_2(line_list)




# Solution from REddit
import re
import numpy as np
from pathlib import Path

# import utils # this was creators own python file with utilities
# https://github.com/cutonbuminband/AOC/blob/main/utils.py

datadir = Path(__file__).parent / "data"

def year_load(year):
    def load(day, output="lines", header=0, footer=None, **kwargs):
        filename = datadir / str(year) / f"{day}.txt"
        if output == "raw":
            s = open(filename).read()
            return s if s[-1] != "\n" else s[:-1]
        lines = open(filename).readlines()[header:footer]
        if output == "lines":
            return [x.strip() for x in lines]
        if output == "int":
            regex = re.compile(r"-?\d+")
            integers = [[int(x) for x in re.findall(regex, line)] for line in lines]
            return [integer for integer in integers if integer]
        if output == "np":
            if "delimiter" not in kwargs:
                kwargs["delimiter"] = ","
            return np.loadtxt(filename, dtype=int, **kwargs)
        if output == "chararray":
            return np.array([[char for char in line.strip()] for line in lines])

    return load

load = year_load(2024)

#data = load(3, "raw")
data = open('resources/corrupted_memory.txt').read()
#print(type(data), len(data))

mul = r"mul\((\d{1,3}),(\d{1,3})\)"

sum(int(pair[0]) * int(pair[1]) for pair in re.findall(mul, data))
#print(sum(int(pair[0]) * int(pair[1]) for pair in re.findall(mul, data)))

