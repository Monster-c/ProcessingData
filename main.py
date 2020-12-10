import json
import csv


sourcefile = '/media/xianwei/E8E6-15AB/组会/zhong.json'

resultfile = open('result.csv', 'w')


headdict = {'id':'编号',
            'title':'标题',
            'classify':'种类',
            'infoType':'信息类型',
            'province':'省份',
            'city':'城市',
            'content':'内容'}


'''生成head'''
def create_csv(sourcefile):

    head = generate_title(sourcefile)
    writer = csv.writer(resultfile)
    writer.writerow(head)



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


'''在这里开始处理数据'''
def write_flie(file):
    with open(file, 'r', encoding='utf-8') as f:
        writer = csv.writer(resultfile)
        try:
            while True:
                line_data = f.readline()
                if line_data:
                    data = json.loads(line_data)
                    row = data.values()
                    writer.writerow(row)
                else:
                    break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    create_csv(sourcefile)
    write_flie(sourcefile)


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
