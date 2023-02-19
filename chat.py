# 讀取檔案
def readfile(rfilename):
    chat = []
    with open(rfilename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
        print(chat)
        return chat

# 內容格式轉換
def convert(chat):
    new = []
    person = None # 先不給值(但還是要先宣告這個變數，以免出錯)
    for line in chat:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: # 如果person有值
            new.append([person, line])
    return new

# 寫入檔案
def write_file(wfilename, chat):
    with open(wfilename, 'w', encoding = 'utf-8') as f:
        for person, line in chat:
            f.write(f'{person}: {line}\n')

def main():
    rfilename = 'input.txt'
    wfilename = 'output.txt'
    chat = readfile(rfilename)
    chat = convert(chat)
    write_file(wfilename, chat)

if __name__ == '__main__':
    main()