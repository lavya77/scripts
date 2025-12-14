import os

path = input("Enter directory path: ")
size_limit = 100 * 1024 * 1024 

for root, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        try:
            if os.path.getsize(full_path) > size_limit:
                print("Large file:", full_path)
        expect:
                pass
