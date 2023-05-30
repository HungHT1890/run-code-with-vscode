from os import system
system('cls')
system('title Open Code Quickly - Python - t.me/hunght1890')
def open_folder_code():
    path = input("Path folder: ")
    if path != '':
        system(f'cd /d {path} & code . & exit')
    else:
        system('cls')
        return open_folder_code()


if __name__ == '__main__':
    open_folder_code()
    