# catwincheck

theBoard ={'top-L': 'x','top-M':'o','top-R':'x',
           'mid-L': 'o','mid-M':'o','mid-R':'o',
           'low-L': ' ','low-M':'x','low-R':'x'}



keylistfortheBoard= list(theBoard.keys())

if all(theBoard[key] != ' ' for key in keylistfortheBoard):
    print('the cat won.')
    #set whatever variables you need to so the Boss
    # knows the game is over
else:
    print("the game continues. It's o's turn.")
    #set whatever variables you need to so the Boss
    #knows the game is to continue.
#endif#
