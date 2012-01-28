#!/usr/bin/envs python
#-*- coding: utf-8 -*-#

def main(offset=6):
    string = u'静夜思 李白床前明月光，疑似地上霜。举头望明月，低头思故乡。090131'
    a = [[' ']*offset for row in xrange(offset)]
    for i in xrange(offset):
        for j in xrange(offset):
            a[i][j] = string[j + i*offset]
    b = [[r[col] for r in a[::-1]] for col in xrange(len(a[0]))]
    print '\n'.join([u'┊'.join(unicode(c) for c in row)for row in b])

if __name__ == "__main__":
    main()    
