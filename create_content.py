import csv
import re


sourcefile = './result.csv'

content = open('content.csv', 'w')

with open(sourcefile,'r',encoding='utf-8') as f:
    text = f.readline()
    print(text)
    text = text.split(',')
    print(text[9])
    text = f.readline()
    print(text)


if __name__ == '__main__':

    pass

