# 讀取檔案
def readfile(rfilename):
    chat = []
    with open(rfilename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
        # print(chat)
        return chat


# 聊天內容計算
def convert(chat):
    Allen_ct = 0
    Allen_cs = 0
    Allen_cp = 0
    Viki_ct = 0
    Viki_cs = 0
    Viki_cp = 0
    for line in chat:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_cs += 1
            elif s[2] == '圖片':
                Allen_cp += 1
            else:
                for m in s[2:]:
                    Allen_ct += len(m)
        if name == 'Viki':
            if s[2] == '貼圖':
                Viki_cs += 1
            elif s[2] == '圖片':
                Viki_cp += 1
            else:
                for m in s[2:]:
                    Viki_ct += len(m)
    print(f'Allen傳了{Allen_ct}個字')
    print(f'Allen傳了{Allen_cs}個貼圖')
    print(f'Allen傳了{Allen_cp}張圖片')        
    print(f'Viki傳了{Viki_ct}個字')
    print(f'Viki傳了{Viki_cs}個貼圖')
    print(f'Viki傳了{Viki_cp}張圖片')


def main():
    rfilename = 'LINE-Viki.txt'
    # wfilename = 'LINE_output.txt'
    chat = readfile(rfilename)
    convert(chat)

if __name__ == '__main__':
    main()