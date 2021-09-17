def product_of_items(lst):
    """Return a new list such that
     each element at index i of the new list is the product
      of all the numbers in the original array except the one at i"""
    result = []

    def product_list(my_list):
        product = 1
        for x in my_list:
            product *= x
        return product
    for i in lst:
        index = lst.index(i)
        other_numbers = lst[:index]+lst[index+1:]
        result.append(product_list(other_numbers))
    return result
