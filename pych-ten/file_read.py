def read_file(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("File "+filename+" does not found.")
    else:
        print(contents.rstrip().title())