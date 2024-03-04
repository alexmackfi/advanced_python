def tail(count = 1, filenames=[]):
    if count == 1:
        for i in filenames[0].split('\n')[-17::]: print(i)
    else:
        ans = []
        for filename in filenames:
             with open(filename) as f:
                strings = []
                for i in f: strings.append(i.rstrip())
                ans.append((filename, strings))
        for name, i in ans:
            if count > 2: print('==>', name, '<==')
            for j in i[-10::]: print(j)

if __name__ == "__main__":
    import sys

    arg = len(sys.argv)
    if len(sys.argv)>1:tail(arg,sys.argv[1::])
    else: tail(arg, [''.join(sys.stdin.readlines())])
