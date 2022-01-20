my_list = []

with open('maze.txt', 'r') as f:
    for element in f:
        element = element.strip("\n")
        line = list(element)
        my_list.append(line)
    
    for element in my_list:
        count = len(element)
        print(count)
