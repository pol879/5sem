#��������� � ������, � 1� ������� ����� ������� ���� ������������ �������, � ��� ��� ������ ������� ���������� ����� ����� ��� ������ ��������
with open('file.txt', 'r',encoding="utf8") as f:
    for line in f:
        c_line=line.strip()
        if c_line: # in case I have empty lines
            print(c_line)
            