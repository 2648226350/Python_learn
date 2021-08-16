def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file "+filename+" does not found."
        print(msg)
    else:
        num_words = len(contents.split())
        print("The file "+filename+" has "+str(num_words)+" words.")
count_words('file\\hello.txt')