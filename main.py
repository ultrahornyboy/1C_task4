import dircmp
# для использования атрибута comapre_files
import sys
# для то что бы считывать данные с параметров


def main():
    if len(sys.argv) == 4:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
        accurancy = float(sys.argv[3])
    elif len(sys.argv) == 1:
        dir1 = input("Tony, give me name of first directory ")
        dir2 = input("Tony, give me name of second directory ")
        accurancy = float(input("Tony, give me accurancy "))
    elif len(sys.argv) == 3:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
        accurancy = 100
    else:
        print("Tony, I do not undestend what you want")
        return
    dircmp.compare_files(dir1, dir2, accurancy)


if __name__ == "__main__":
    main()
