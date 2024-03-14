
print("Nim game!!\nWe are having 12 tokens")
def getTokens(curTokens):
    global tokens
    print("How many tokens would you like to take? ", end='')
    take = int(input())
    if (take < 1 or take > 3):
        print("Number must be between 1 and 3.\n")
        getTokens(curTokens)
        return
    tokens = curTokens - take
    print('You take',take ,'tokens.')
    print(tokens ,'tokens remaining.\n')
def compTurn(curTokens):
    global tokens
    take = curTokens % 4
    tokens = curTokens - take
    print ('Computer takes ',take, ' tokens.')
    print (tokens,' tokens remaining.\n') 
tokens = 12
while (tokens > 0):
    getTokens(tokens)
    compTurn(tokens)
print("Computer wins!")
