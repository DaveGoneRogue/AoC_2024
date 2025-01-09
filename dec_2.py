import pandas as pd
import numpy as np

df = pd.read_csv('resources/reports.txt', header = None, engine='python')
#print(df.head)

'''
# Testing the structure of the dataframe (Long time since i worked with Pandas)
#temp = df[0]
temptemp = temp[0]
print(temp)
print(temptemp)
print(type(temptemp))
print(df.shape)
'''


def str_to_int(list_0):  # Converts ['1', '2', ...] -> [1, 2, ...]
    res = map(int, list_0)
    return list(res)


def test_increase(list_0):
    for i in range(1, len(list_0)-1):  # Recall, we have already tested first level. The last level has nothing to compare against, is exluded
        if list_0[i] > list_0[i+1]:
            return False
    return True  # If not returning false when runnning the loop, returns true


def test_decrease(list_0):
    for i in range(1, len(list_0)-1):  # Recall, we have already tested first level. The last level has nothing to compare against, is exluded
        if list_0[i] < list_0[i+1]:
            return False
    return True  # If not returning false when runnning the loop, returns true


def test_difference(list_0):
    f_difference = lambda x,y: abs(x-y)
    f_test = lambda x: True if x==1 or x==2 or x==3 else False 

    for index in range(0,len(list_0)-1):
        if f_test(f_difference(list_0[index], list_0[index+1])) == False:  # Calculates difference, then checks if the level difference is safe
            return False
    return True  # If not returning false when runnning the loop, returns true


def red_nose_nuc_plant_safety_test_1(list_0):
    # For a SAFE report, the levels must be all increasing or all decreasing, 
    # and that two adjacent levels differ by at least one and at most three
    #i.e last one is important, that means that if we have duplicate numbers the list is not safe
    
    # Thinking; by first converting to a set and comparing length, we can efficiently exclude a lot of cases to test
    if len(set(list_0)) != len(list_0):  # If the set of the list have the same length, all levels are unique 
        return False  # i.e. Contains duplicates
    
    # Test element by element if they all are all increasing or all decreasing
    # This will also work for testing duplicate numbers, but it is a element by element operation, so doing above first is prob. more efficient.
    if list_0[0]<list_0[1]:
        all_inc_or_dec = test_increase(list_0)  # test if all increasing
    else:
        all_inc_or_dec = test_decrease(list_0)  # test if all decreasing

    # Return False if the list is not: all increase or all decrease
    if all_inc_or_dec == False: 
        return False
    
    adj_val_safe = test_difference(list_0)
    if adj_val_safe == False:
        return False
    
    return True
    

def dataframe_safety_check(dataframe, safety_function):
    safe_count, nsafe_count = 0, 0
    safety_list = []
    level_list = []

    for index in range(0,len(dataframe)):
        element = dataframe[0][index]  # Each element in the column representing a report
        list_of_int = str_to_int(element.split())  # Does '1 2 ...' -> ['1','2', ...] -> [1, 2, ...]
        safety_bool = safety_function(list_of_int)  # Test if the levels in the report are safe

        # Append and Increase counters
        safety_list.append(safety_bool)
        level_list.append(list_of_int)
        if safety_bool:
            safe_count += 1
        else:
            nsafe_count += 1
    
    # Returning values
    df_new = pd.DataFrame(np.column_stack([level_list, safety_list]), columns=['reports', 'safe'])  # Create new dataframe of the two lists
    
    # Returning a tuple containing the number of safe and not safe reports, and tot. number of reports
    safety_tuple = (safe_count, nsafe_count, len(df))
    return df_new, safety_tuple


# ———————————————— Part 1 ————————————————
# Checking the safety of the reports
safe_checked_df, answer = dataframe_safety_check(df, red_nose_nuc_plant_safety_test_1)
print(f'Safety analysis complete\n #Safe: {answer[0]} \n #Not Safe: {answer[1]} \n #Total: {answer[2]}')



# ———————————————— Part 2 ————————————————
# The problem dampeneer
# The reactor can tolerate a single bad level

# Lets use the safety list from part 1 to recheck bad reports instead of rebuilding the code


def extract_unsafe(list_0):
    unsafe_reports_ls = []
    for index in range(0,len(list_0)):
        if list_0[index] == False:
            unsafe_reports_ls.append(index)
    return unsafe_reports_ls


def dampener_test(dataframe):
    unsafe_reports_ls = extract_unsafe(dataframe['safe'].tolist())

    for index in unsafe_reports_ls:
        element = dataframe['report'][index]
        # manipulte this element and run some new check


    
    return None

#dampener_test(safe_checked_df)