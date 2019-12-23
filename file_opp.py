import file_operations
# from file_operations import save_to_file, read_file

file_operations.save_to_file('Rolf', 'data.txt')

name = file_operations.read_file('data.txt')
print(name)