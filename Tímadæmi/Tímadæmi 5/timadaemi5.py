
def length_string(a_str):
    
    if a_str == '':
        return 0
    
    return 1+length_string(a_str[:-1])


print(length_string('jalo'))



def linear_search(a_list, value):
    if a_list == []:
        return False
    elif a_list[0] == value:
        return True
    
    return linear_search(a_list[1:], value)

print(linear_search([1,2,4,5],5))


def count_instances(a_list, value):

    if a_list == []:
        return 0
    elif a_list[0] == value:
        return 1 + count_instances(a_list[1:],value)
    
    return count_instances(a_list[1:],value)


print(count_instances([1,6,7,4,6],6))


def duplicates(a_list):
    # ef þetta gerist er ég kominn í endann og hef ekki 
    # enn skilað true þannig að það eru engar
    # duplicates
    if a_list == []:
        return False
    elif linear_search(a_list[1:], a_list[0]):
        return True
    
    return duplicates(a_list[1:])


print(duplicates([12,4,6,7,3,2]))


def remove_duplicates(a_list):
    
    if not duplicates(a_list):
        return a_list
    elif linear_search(a_list[1:], a_list[0]):
        return remove_duplicates(a_list[1:])

    # bæti við gildum sem 
    # eru ekki duplicates fyrir aftan 
    # og tek fremsta stakið
    a_list.append(a_list[0])
    return remove_duplicates(a_list[1:])

print(remove_duplicates([12,4,6,7,3,2,6]))



def binary_search(ord_list, value):

    if len(ord_list) == 1:
        if ord_list[0] == value:
            return True
        else:
            return False


    mid = (len(ord_list))//2

    if ord_list[mid] == value:
        return True
    elif value < ord_list[mid]:
        return binary_search(ord_list[mid:], value)
    else:
        return binary_search(ord_list[:mid], value)


print(binary_search([1,3,6,73,5], 5))

def prefix(prefix, a_str):
    '''Returns True if the first letter
     of a_str is prefix'''

    if a_str[0:len(prefix)] == prefix:
        return True

    return False


def is_substring(substring, a_str):
    
    if a_str == '':
        return False

    elif prefix(substring, a_str):
        return True
    
    return is_substring(substring, a_str[1:])

print(is_substring('ski', 'gagnaskipan'))



def x_ish(a_str, x):


    if is_substring(x, a_str):
        return True
    
    elif x == '':
        return False
    
    if check_if_in(a_str, x):
        return x_ish(a_str,x[1:])
    
    return False


# eins og að gera if x in a_str
def check_if_in(a_str, x):
    
    if a_str == '':
        return False

    if x == a_str[0]:
        return True
    else:
        return check_if_in(a_str[1:],x)



print(x_ish('gagnaskipan', 'nsk'))

def helper(a_str, b_str):

    if a_str == b_str:
        return True
    else:
        return False


def palindrome(a_str):

    if a_str == '':
        return True

    b_str = a_str[::-1]

    if helper(a_str, b_str):
        return True
    
    return False

print(palindrome('he'))