s = raw_input()
s = list(s)
zc = list()
k = 0
for i in range(len(s)):
    if s[i] not in zc:
        zc.append(s[i])
    for j in range(i+1, len(s)):
        if s[i] != s[j]:
            break
        ss = s[i:j]
#        print 'ss is ', ss
#        print 's_u is ' ,s_u
        if  ss not in zc:
            zc.append(ss)
#            zc.append(ss)
            

print len(zc)

