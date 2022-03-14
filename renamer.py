from genericpath import isdir
import os


def main():
    print("After inputing the full path to the directory you want to rename all files in, you will have to enter a keyword that will be used as a name of every of the files in the directory. Every file will get a number as it follows.")
    print("***")
    folder = input("Write full path there to rename and add number to every file: ")
    keyword = input("What will be the name of all the files: ")
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{keyword} {str(count)}"
        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"
        os.rename(src, dst)

    print("***Done.***")


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
