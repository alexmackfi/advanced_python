def nl(filename):
    ans = []
    try:
        with open(filename) as f:
            for i in f:
                ans.append(i.rstrip())
    except:
        ans = filename.split('\n')
    for i in enumerate(ans,1):
        print('    ',*i)

if __name__ == "__main__":
    import sys

    if len(sys.argv)>1:nl(sys.argv[1])
    else: nl(''.join(sys.stdin.readlines()))

