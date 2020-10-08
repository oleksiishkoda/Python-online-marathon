import json
import logging
def walk(lst, path = ()):
    for dicti in lst:
        path = path + dicti['name']
        yield path
        for child in dicti:
            yield from walk(child, path)

def parse_user(output_file, *input_files):
    lst = []
    for item in input_files:
        with open(f'sprint 6/2 task/{item}','r') as f:
            f_read = f.read()
            data = json.loads(f_read)
            lst.append(data)
    new_lst = walk(lst)
    # with open(f'sprint 6/2 task/{output_file}', 'w') as f:
    #     json.dump(lst, f, indent = 2)

    return new_lst
a = parse_user('2020_3.json', '2020-01.json','2020_2.json')
print(a)