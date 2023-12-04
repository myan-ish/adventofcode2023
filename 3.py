test_text=\
"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def get_diagonal_adj_pos(lines):
    number_pos_dict = {}
    special_pos_dict = {}
    for line_id, line in enumerate(lines):
        temp_number = ""
        length = 0
        pos = None
        for index, char in enumerate(line):
            # print(index,char, char.isdigit())
            if char.isdigit():
                temp_number += char
                length += 1
                if pos == None:
                    pos = index
            
            if not char.isdigit() and not char.isalpha() and char != ".":
                special_pos_dict[f'{char} {line_id}'] = {
                    "pos": f'{index-1}-{index+1}',
                    }

            if (char == "." or index == len(line)-1) and pos != None:
                number_pos_dict[temp_number] = {
                    "pos" : f"{pos}-{pos+length-1}",
                    "line": f"{line_id}"}
                temp_number = ""
                length = 0
                pos = None
    print(number_pos_dict, special_pos_dict)
    return number_pos_dict, special_pos_dict

def get_sum(lines):
    number_pos_dict, special_pos_dict = get_diagonal_adj_pos(lines)

    number_of_lines = len(lines)

    for index in range(number_of_lines):
        get_special_objs = special_pos_dict.keys().strip()

        for key, value in special_pos_dict
    
    

get_sum(test_text.strip().split("\n"))

print()