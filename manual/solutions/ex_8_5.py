# Rewrite grep and grepinto functions to use context managers.

def grep(file, text):
    lines_matching = []
    with open(file, "r") as f:
        for line in f:
            if text in line:
                lines_matching.append(line)
    return lines_matching


def grepinto(file_in, file_out, text):
    with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
        for line in f_in:
            if text in line:
                f_out.write(line)


if __name__ == "__main__":
    filename = input("Enter file name:")
    print_lines = grep("ex_6_2.py", "filter")
    print(print_lines)

    grepinto("ex_6_2.py", "filter_lines.txt", "filter")
