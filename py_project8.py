def main():
    text = r'''  The King and Queen of Hearts were seated on their throne when they arrived,
    with a great crowd assembled about them--all sorts of little birds and beasts,   
    as well as the whole pack of cards: the Knave was standing before them, in  
    chains, with a soldier on each side to guard him; and near the King was the    
    White Rabbit, with a trumpet in one hand, and a scroll of parchment in the     
    other. In the very middle of the court was a table, with a large dish of tarts
    upon it: they looked so good, that it made Alice quite hungry to look at them--   
    `I wish they'd get the trial done,' she thought, `and hand round the     
    refreshments!'
    
      But there seemed to be no chance of this, so she began looking at everything   
    about her, to pass away the time.
      '''
    '''
    整体思路：先用\n分割text，找最大长度的一行，让其他行末尾加上空格与最大长度行长度相等。
    之后让每个list元素前后都加|
    最后用\njoin整个list
    '''

    text_list=text.split('\n')
    new_text_list=[i.strip() for i in text_list]
    for k in range(len(new_text_list)):
        if k==0 or k==10:new_text_list[k]='  '+new_text_list[k]   #段首空两格

    max_length=max([len(m) for m in new_text_list])
    cache_text_list=[]
    for n in new_text_list:
        n=n+' '*(max_length-len(n))
        cache_text_list.append(n)
    new2_text_list=['|'+j+'|' for j in cache_text_list]
    text_str='\n'.join(new2_text_list)

    if isinstance(text_str, str):
        print('+'+'-'*max_length+'+')
        print(text_str)
        print('+' + '-' * max_length + '+')



if __name__=='__main__':
    main()