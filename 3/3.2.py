def write_array(array, file_name):
    """���������� ������ �� array � ���� file_name ��� ������"""
    with open(file_name, 'w') as f: 
        f.write('\n'.join(array))
    


#��� ��� �������� ������� (�� ������ � �������)        
file_name='p.txt'
array=['adg','djjjjj','csssssssssss','sjjjjjjddd']
write_array(array,file_name)


