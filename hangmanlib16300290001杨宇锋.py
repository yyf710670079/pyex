'''
hangmanlib.py
   A set of library functions for use with your Hangman game
   Actually you can add all help functions here, and just 
   import you can use all functions! 
   Enjoy!
'''

LINEPERIMAGE = 9  #Every LINEPERIMAGE is a perfect picture of hangman

def print_hangman(wordlist, mistakes = 6):
    '''
    print hangman : from 0 (hang) to 6 (hanged)
    '''

    lines = LINES.split('\n')
    start = mistakes * LINEPERIMAGE
    i=0
    for line in lines[start: start+ LINEPERIMAGE]:
        i += 1
        if i == 6:
            print('{0}{1}{2}'.format(wordlist, ' '*int(25-int(len(wordlist))), line))
        else:
            print('{0}{1}'.format(' ' * 25, line))
#end print_hangman_image

# We intentionally add LINES below: it's too long
LINES = ''' ______
|  |
|  
| 
|  
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| 
|  
| 
|_____
|     |____
|__________|
 ______
|  |
|  O
| /
|  
| 
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|
|  |
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
| /  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
| / \ 
|_____
|     |____
|__________|

'''
