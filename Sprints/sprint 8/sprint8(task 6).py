import unittest
def file_parser(file, *strings):
    count = 0
    data = open(file, 'r')
    if len(strings) == 1:
        for line in data:
            if strings[0] in line:
                count += 1
        data.close()
    if len(strings) == 2:
        lines = data.readlines()
        write_data = open(file, 'w')    
        for line in lines:
            if strings[0] in line:
                write_data.write(line.replace(strings[0], strings[1]))
                count += 1
            else:
                write_data.write(line)
        write_data.close
        data.close()
        return f"Replace {count} strings"
    data.close()
    return f"Found {count} strings"
class ParserTest(unittest.TestCase):
    pass

print(file_parser('d', 2, 3))