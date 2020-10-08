import json
def find_all(data, key):
    result = []
    def find_in_dict(data, key):
        for k, value in data.items():
            if k == key:
                if isinstance(value, list): result.extend(value)
                else: result.append(value)
            else:
                find_in_data(value, key)

    def find_in_data(data, key):
        if isinstance(data, list):
            for elem in data:
                find_in_data(elem, key)
        if isinstance(data, dict):
            find_in_dict(data, key)
    find_in_data(data, key)
    return set(result)
def find(file, key):
    with open(file, 'r') as f:
        data = json.load(f)
    return list(find_all(data, "password"))


print(find("sprint 6/1 task/3.json", "password"))
print(find("sprint 6/1 task/2.json", "password"))
print(find("sprint 6/1 task/1.json", "password"))