def counter(words=0,bits=0,shifts=0, mas=[]):
    for i in mas:
        words+=len(i.split())
        bits+=len(i.encode('utf-8'))
        if '\n' in i: shifts+=1
        # print(shifts, words, bits)
    return shifts, words, bits

def wc(count = 1, filenames = []):
    words,bits,shifts  = 0,0,0
    if count < 2:
        shifts = len(filenames[0].split('\n'))-1
        print(counter(words,bits,shifts,filenames[0].split('\n'))[0], 
              counter(words,bits,shifts,filenames[0].split('\n'))[1], 
              counter(words,bits,shifts,filenames[0].split('\n'))[2]+shifts)
    else:
        total_words,total_bits,total_shifts  = 0,0,0
        for j in filenames:
            with open(j) as f:
                shifts, words, bits= counter(words,bits,shifts,f)
            print(shifts, words, bits+shifts, j)
            total_words+=words
            total_bits+=(bits+shifts)
            total_shifts+=shifts
            words, bits, shifts  = 0,0,0
        if count>2:
            print(total_shifts, total_words, total_bits,'total')

if __name__ == "__main__":
    import sys

    arg = len(sys.argv)
    if len(sys.argv)>1:wc(arg,sys.argv[1::])
    else: wc(arg, [''.join(sys.stdin.readlines())])