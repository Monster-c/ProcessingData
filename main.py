import json
import csv

#数据导入
sourcefile = '/media/xianwei/E8E6-15AB/组会/zhong.json'

resultfile = open('result.csv', 'w')

#contents = open('content.csv', 'w')


'''生成head'''
def create_csv(sourcefile):

    head = generate_title(sourcefile)
    print(head)

    writer = csv.writer(resultfile)
    writer.writerow(head)

    # content = list(head)
    # title = content[9].split('4')
    #print(title)
    # writer = csv.writer(contents)
    # writer.writerow(title)

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
        # writer = csv.writer(contents)
        try:
            while True:
                line_data = f.readline()
                if line_data:
                    data = json.loads(line_data)
                    data = list(data.values())
                    writer.writerow(data)
                    # row = data['content'].split('囧')#目的是将str转换为list
                    # print(row)
                    # print(type(row))
                    # writer.writerow(row)
                    # break
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
