def filee():
    name = input("Enter file:")
    if len(name) < 1:
        name = "mbox-short.txt"
        handle = open(name)
    return handle

def main():
    d = dict()
    #op = []
    for i in filee() :
        if i.strip().startswith('From ') :
            l = i.split()
            l = l[5][:2]
            d[l] = d.get(l, 0) + 1
    #for k,v in d.items():     
    #    op.append((k,v))        
    #print(sorted(''.join((k,v)for k, v in d.items())))
    for k,v in sorted(d.items()) :
        print(k,v)

if __name__ == '__main__':
    main()