# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
        return lines


def convert(lines):
    new = []
    for line in lines:
        s = line.split(' ')
        time = s[0][:5]
        name = s[0][5:]
        print(time, '講話的人', name)


def main():
    filename = '3.txt'
    lines = read_file(filename)
    convert(lines)

if __name__ == '__main__':
    main() 