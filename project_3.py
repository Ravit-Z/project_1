from collections import defaultdict

NAME_INDEX = 4

def file_to_dict(path: str):
    try:
        with open(path, 'r') as data_file:
            return {i: line.strip().split(',') for i, line in enumerate(data_file) if len(line) > 1}
    except FileNotFoundError:
        print(f"sorry, we didn't found {path}")

def sum_column(flowers_info: dict, index:int):
    flower_hight = defaultdict(float)
    for data in flowers_info.values():
        flower_hight[data[NAME_INDEX]] += float(data[index])
    return flower_hight

if __name__ == '__main__':
    basic_data = file_to_dict('iris.data')
    flowers_hight = sum_column(basic_data, 2)
    for name, hight in flowers_hight.items():
        print(f"{name} {round(hight, 1)}")