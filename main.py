import json
import csv


file = '/media/xianwei/E8E6-15AB/组会/zhong.json'


'''创建csv文件并生成head'''
def create_csv(filename, file):
    resultfile = open(filename, 'w')
    head = generate_title(file)
    writer = csv.writer(resultfile)
    writer.writerow(head)

    return resultfile

'''在这里读取一次文件，从而生成表头信息'''
def generate_title(file):
    head = []
    with open(file, 'r', encoding='utf-8') as f:
        try:
            line_data = f.readline()
            if line_data:
                data = json.loads(line_data)
                head = data.keys()
        except Exception as e:
            print(e)
    return head

'''读取文件'''
def read_file(file):
    pass

'''一次读取一行信息'''
def read_line(file):
    pass

'''在这里开始处理数据'''
def write_flie(file):
    try:
        while True:
            row = {}
            line_data = file.readline()
            if line_data:
                data = json.loads(line_data)
                row = data.valus()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    create_csv('result.csv',file)


# with open(filename, 'r', encoding='utf-8') as f:
#     keys = []
#     print(type(keys))
#     try:
#         while True:
#             line_data = f.readline()#every time just load one line to save the memorary
#             if line_data:
#                 data = json.loads(line_data)
#                 keys = data.keys()
#                 print(keys)#将key作为表头name
#                 #print(data)
#                 input("等待")
#     except Exception as e:
#         print(e)
#         f.close()
