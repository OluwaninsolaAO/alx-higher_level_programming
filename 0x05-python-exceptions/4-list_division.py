#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides one list by another using their corresponding
    indexed elements of range llist_lenght"""

    new_list = []
    for num in range(list_length):
        try:
            tmp = my_list_1[num] / my_list_2[num]
        except TypeError:
            tmp = 0
            print("wrong type")
        except ZeroDivisionError:
            tmp = 0
            print("division by 0")
        except IndexError:
            tmp = 0
            print("out of range")
        finally:
            new_list.append(tmp)

    return new_list
