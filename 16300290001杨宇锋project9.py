import re
text = '''
    1.   abc  2016-10-31  
    2.   xyz   2016-9-4
    3.   aef   2016-10-aa
    4.    asasf asdf 10-14
    5.  2013-10-3  234234
    6.  1945-8-15 abc  1945
    7.  1972-01-30 asdf  1988-10-1
'''

def main():
    match=re.findall(r'(\d{4})-(\d{1,2})-(\d{1,2})',text)
    new_match=[]

    for tup in match:
        tmp=[]
        for j in range(1,3):
            if len(tup[j])<2:
                tmp.append('0'+tup[j])
            else:
                tmp.append(tup[j])
        new_match.append([tup[0],tmp[0],tmp[1]])
            

    for i in range(len(new_match)):
        print('%d.%s/%s/%s\n'%(i+1,new_match[i][1],\
                               new_match[i][2],new_match[i][0]))




if __name__=='__main__':
    main()
