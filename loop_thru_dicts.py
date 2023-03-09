

theBoard ={'top-L': 'x','top-M':'o','top-R':'x',
           'mid-L': 'o','mid-M':'x','mid-R':'o',
           'low-L': 'o','low-M':'x','low-R':'o'}


wintop  ={'top-L': 'x','top-M':'x','top-R':'x'}
winmid  ={'mid-L': 'x','mid-M':'x','mid-R':'x'}
winbottom  = {'low-L': 'x','low-M':'x','low-R':'x'}
windiag_ltor  ={'top-L': 'x','mid-M':'x','low-R':'x'}
windiag_rtol  ={'low-L': 'x','mid-M':'x','top-R':'x'}
winleftcol  ={'low-L': 'x','mid-L':'x','top-L':'x'}
winmidcol  ={'mid-M': 'x','top-M':'x','low-M':'x'}
winrightcol  ={'top-R': 'x','mid-R':'x','low-R':'x'}

winlist=[wintop,winmid,winbottom,windiag_ltor,windiag_rtol,winleftcol,winmidcol,winrightcol]

loop=True
win= False
while loop == True:
    for winlistindex in range(0,8):

        x=winlist[winlistindex]
        keylistforwin= list(x.keys())  #keylist is a list of the keys in that dictionary
        print(x,'is the winlist we are looping through')
        if all(x[key] == theBoard[key] for key in keylistforwin):   # compare all the key-value pairs in
                                                                #keylistforwin match between x and theBoard
            print('that test worked and x wins')
            win=True
            loop=False
            break
        else:
            print(x,"didn't work.")
            if winlistindex == 7:
                loop = False
                print('x did not win yet')
            #endif
        #endif
    #endfor
#endwhile


