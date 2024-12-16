import pandas as pd

#df = pd.read_csv('resources/two_list.txt', header = None,sep='\t', lineterminator='\r')
df = pd.read_csv('resources/two_list.txt', header = None, sep='\s+')
# print(df.head)


# Testing the structure of the dataframe (Long time since i worked with Pandas)
#temp= df[1]
#print(temp.head)  # Prints the 1st (remember 0 index) column
#temptemp = temp[0]
#print(temptemp)  # Printes the 0th element


def sort_ascending(one_col_dataframe):
    return one_col_dataframe.sort_values(ascending=True)


def elementwise_function(f, list_0, list_1):
    returned_elementwise_function = map(f, list_0, list_1)
    return list(returned_elementwise_function)


f_subtract = lambda x,y : x-y
f_difference = lambda x,y: abs(x-y)
f_add = lambda x,y : x+y
f_multiply = lambda x,y : x*y


# ———————————————— Part 1 ————————————————
# Total difference score
sorted_0, sorted_1 = sort_ascending(df[0]), sort_ascending(df[1])  # Extract the columns and sort them
sorted_0_ls, sorted_1_ls = sorted_0.tolist(), sorted_1.tolist()  # Convert to Python lists
difference_ls = elementwise_function(f_difference, sorted_0_ls, sorted_1_ls)  # Perform an elementwise computation
total_difference = sum(difference_ls)  # Sum all numbers in the list
print(f"The total difference is {total_difference}")


# ———————————————— Part 2 ————————————————
# Similarity score

def get_duplicates(list_0, list_1):
    duplicates_dic = {}
    for element in list_1:  # We want to check if elements in list 0 appear in list 1. 
        if element in list_0:  # Therefore we itierate over list 1 and check if this element is in list 0
            if element not in duplicates_dic.keys():  # If it is not already in the dictionary we add it
                duplicates_dic[element] = 1  # the key is the element/number itself
            else:
                duplicates_dic[element] += 1  # and the value will be the number of times the element/value will appear in list 1
    return duplicates_dic  


def duplicate_scaling(list_0, duplicates_dic):
    list_0_copy = list_0.copy()
    for position in range(0, len(list_0)):  # Iterate over the list we want to scale values of
        element = list_0_copy[position]  # This is the original value
        if element in duplicates_dic.keys():  # Check if the value is in duplicates
            scaling = duplicates_dic[element]  # Recall that the key for dictionary is the element itself
            list_0_copy[position] = element*scaling  # Update values
        else:
            scaling = 0
            list_0_copy[position] = element*scaling
    return list_0_copy


# ttt2 = sorted_1_ls[:70]  # TESTING
#duplicates = get_duplicates(sorted_0_ls, ttt2)  # TESTING
duplicates = get_duplicates(sorted_0_ls, sorted_1_ls)


#testliste = [0,1,2,3,17008,19198]  # TESTING
#scaled = duplicate_scaling(testliste, duplicates)  # TESTING
scaled = duplicate_scaling(sorted_0_ls, duplicates)

closing = sum(scaled)
print(f"The simelarity score is {closing}") # IT is 23177084 !!



# Alternative solution idea
# Do a simpler loop that fills a list with 0 on the non-duplicates, and the number of duplicates for duplicate numbers.
# Then use the previous elementwise function to pass with multiplication and then sum the list in the end