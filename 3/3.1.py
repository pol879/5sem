# coding: utf-8
#насколько я поняла, в 1м задании можно создать файл произвольным образом, а сам код должен вывести содержимое этого файла без лишних пробелов
with open('file.txt', 'r',encoding="utf8") as f:
    for line in f:
        c_line=line.strip()
        if c_line: # in case I have empty lines
            print(c_line)
            