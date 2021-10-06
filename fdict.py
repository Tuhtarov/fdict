from fcore.controller import Controller

delimiter = '==================================='
print('')
print(delimiter)
print("+=============RUNNING=============+")
print(delimiter)


def get_file_path():
    return str(input("\nType full path of file => "))


controller = Controller()
controller.set_file_path(get_file_path())

while not controller.file_is_available():
    print("please, type the correct path")
    controller.set_file_path(get_file_path())

controller.run()

print(delimiter)
print('---> The end. Bye :)\n')
print("---> developer: 'Tukhtarov Dynamic'")
print(delimiter)
