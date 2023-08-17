def create_an_empty_list():
    return []

def create_a_list():
    return [1, 2, 3, 4]

def add_element_to_end_of_list(lst, element):
    lst.append(element)
    return lst

def add_element_to_start_of_list(lst, element):
    lst.insert(0, element)
    return lst

def remove_element_from_end_of_list(lst):
    lst.pop()
    return lst

def remove_element_from_start_of_list(lst):
    del lst[0]
    return lst

def retrieve_first_element_from_list(lst):
    return lst[0]

def retrieve_element_from_index(lst, index):
    return lst[index]

def retrieve_last_element_from_list(lst):
    return lst[-1]

# Test the functions
empty_list = create_an_empty_list()
print(empty_list)

list_with_elements = create_a_list()
print(list_with_elements)

list_with_elements = add_element_to_end_of_list(list_with_elements, 5)
print(list_with_elements)

list_with_elements = add_element_to_start_of_list(list_with_elements, 0)
print(list_with_elements)

list_with_elements = remove_element_from_end_of_list(list_with_elements)
print(list_with_elements)

list_with_elements = remove_element_from_start_of_list(list_with_elements)
print(list_with_elements)

first_element = retrieve_first_element_from_list(list_with_elements)
print(first_element)

element_at_index = retrieve_element_from_index(list_with_elements, 2)
print(element_at_index)

last_element = retrieve_last_element_from_list(list_with_elements)
print(last_element)
