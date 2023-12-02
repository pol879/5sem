def write_array(array, file_name):
    """записывает строки из array в файл file_name без циклов"""
    with open(file_name, 'w') as f: 
        f.write('\n'.join(array))
    


#код для проверки функции (не входит в задание)        
file_name='p.txt'
array=['adg','djjjjj','csssssssssss','sjjjjjjddd']
write_array(array,file_name)


