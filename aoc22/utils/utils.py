def read_input(filepath, part_2 = False):
    filepath = filepath + '\\input.txt'
    if part_2:
        filepath = filepath.replace('.txt', '2.txt')
    with open(filepath, 'r') as file:
        full_text = file.read()
    
    if full_text[-1] == '\n':
        return full_text[:-1]
    else:
        return full_text