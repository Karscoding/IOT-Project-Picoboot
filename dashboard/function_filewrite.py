from imports_n_vars import os, sys

def WritetoFile(value):
    """
    Value = string
    
    Value :
    L = Bakboord (Links)
    R = Stuurboord (Rechts)
    P = Passeerlampen UIT
    X = Alle verlichting AAN
    U = Alle verlichting UIT
    """
    path = os.path.join(sys.path[0], '../Texts/opdracht.txt')
    current = ''
    
    #Function attempts to open file
    try:
        f= open(path, 'r')
        current = f.read()
        f.close()
    #Exception creates the file
    except:
        f = open(path, 'x')
    
    #File opens
    with open(path, 'w') as f:
        if value == 'L' or value == 'R' or value == 'P':
            newstring = current.replace(current[1], value, 1)
            f.write(newstring)
            
        elif value == 'X' or value == 'U' or value == 'N':
            newstring = current.replace(current[0], value, 1)
            f.write(newstring)