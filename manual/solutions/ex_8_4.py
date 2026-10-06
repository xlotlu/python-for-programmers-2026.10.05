# Write a program that reads the content of a text file and counts the number of
# words in it. Print the word count.
def ex1():
    filename = "ex_7_2.py"
    f = open(filename, "r")
    words_count = 0
    for line in f:
        words_count += len(line.split())
    f.close()
    print(f"File {filename} contains {words_count} words.")
    print(f"File {filename} is closed: {f.closed}.")


def ex1_with():
    filename = "ex_7_2.py"
    with open(filename, "r") as f:
        words_count = 0
        for line in f:
            words_count += len(line.split())
    print(f"File {filename} contains {words_count} words.")
    print(f"File {filename} is closed: {f.closed}.")


# Write a function grep that receives text and file as parameters and returns a
# list with all the lines in the file containing text.
def grep(file, text):
    f = open(file, "r")
    lines_matching = []
    for line in f:
        if text in line:
            lines_matching.append(line)
    f.close()
    return lines_matching


# Write another function grepinto that receives text, infile and outfile as
# parameters and writes to outfile the lines in infile that contain text.
def grepinto(file_in, file_out, text):
    f_in = open(file_in, "r")
    f_out = open(file_out, "w")

    for line in f_in:
        if text in line:
            f_out.write(line)

    f_in.close()
    f_out.close()


if __name__ == "__main__":
    ex1()
    ex1_with()

    print_lines = grep("ex_6_2.py", "print")
    print(print_lines)

    grepinto("ex_6_2.py", "print_lines.txt", "print")
