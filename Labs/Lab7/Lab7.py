import os
import hashlib

filedict = {}
def menu():
    while True:
        print("\n--- File Duplicate Finder ---")
        print("1. Enter directory to search")
        print("2. Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            find_duplicates(input("Enter your desired directory:"))
        if choice == 2:
            break

def find_duplicates(directory):
    # search os.walk(directory):
    # use a dictionary to store file names and paths
    # compare files with the same name
    print("Listing Python file:")
    for root,_, files in os.walk(directory):
        for file in files:
            if file in filedict:
                print(f'dupicates were found: {file}')


            file_path = os.path.join(root,file)

            filedict.update({file:get_checksum(file_path)})


    # for dirpath, dirnames, filenames in os.walk('C:/Users/valfo/Labs - ETE 4990'):
    #     for filename in filenames:
    #         if filename.endswith(".py"):
    #             print(filename)


def get_checksum(file_path):
    hash_obj = hashlib.sha256()  # Change to hashlib.sha256() if desired
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


if __name__ == "__main__":
    menu()