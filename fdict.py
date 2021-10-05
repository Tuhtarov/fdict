from fcore.controller import Controller

delimiter = '==================================='
print('')
print(delimiter)
print("+=============RUNNING=============+")
print(delimiter)


def get_file_path():
    return str(input("\nType full path of file => "))


controller = Controller()

# while not controller.file_is_available():
#     print("please, type the correct path")
#     controller.set_file_path(get_file_path())
# else:
#     print('ok.. file is correct!\n')

controller.set_file_path(r'C:\Users\tukhtarov\Desktop\work\test.txt')
controller.run()

print(delimiter)
print('---> The end. Bye :)\n')
print("---> developer: 'Tukhtarov Dynamic'")
print(delimiter)
