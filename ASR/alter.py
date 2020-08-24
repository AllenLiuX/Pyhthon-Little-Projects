from xpinyin import Pinyin
import pypinyin as py


def to_pinyin(word):
    return py.pinyin(word, style=py.NORMAL)


def main():
    with open('wordbank', 'r') as f:
        file = f.read()
        words = file.split('\n')
    pinyin = [to_pinyin(i) for i in words ]
    print(pinyin)

    f= open(r'words2.txt')
    lines = f.readlines()
    f.close()
    # temp = lines[3000]
    # w = temp.split(' ')
    # wp = to_pinyin(w[0])
    # print(wp)
    altered=0
    i = 0
    for line in lines:
        w = line.split(' ')
        wp = to_pinyin(w[0])
        if wp in pinyin:
            ind = pinyin.index(wp)
            new_line = words[ind]+str(altered)+line[len(wp):]
            print(new_line)
            lines[i] = new_line
            # print(wp, w)
            altered += 1
        i += 1
    print("aaaaaaaa:", altered)
    f = open('words3.txt', 'w')
    f.writelines(lines)
    f.close()

if __name__=='__main__':
    main()