def calculate_structure_sum(*args):
    sum_elem = 0
    for i_elem in args:
        if isinstance(i_elem, str):
            sum_elem += len(i_elem)
        elif isinstance(i_elem, int):
            sum_elem += i_elem
        elif isinstance(i_elem, list):
            sum_elem += calculate_structure_sum(*i_elem)
        elif isinstance(i_elem, tuple):
            sum_elem += calculate_structure_sum(*i_elem)
        elif isinstance(i_elem, set):
            sum_elem += calculate_structure_sum(*i_elem)
        elif isinstance(i_elem, dict):
            sum_elem += calculate_structure_sum(*i_elem.items())

    return sum_elem


data_structure = [[1, 2, 3], {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]


result = calculate_structure_sum(data_structure)
print(result)
