n=3
count=0
mat=[['*']*n for _ in range (n)]
def print_matrix():
    for i in range(n):
        for j in range(n):
          print(mat[i][j]," ",end="")
        print('')
def condition():
    while True:
        x=int(input("Enter the row index: "))
        y=int(input("Enter the col index: "))
        if mat[x][y]!='*':
            print("Invalid Index. Try again!!")
        else:
            break
    return x,y
def game(PL,count):
    count+=1
    if count>9:
       print("Tie Game")
       exit(0)
    print("")
    print(f'Player {PL}')
    x,y=condition()
    mat[x][y]=PL
    st2=0
    st1=0
    print_matrix()
    for z in range(3):
        if mat[z][0]==mat[z][1]==mat[z][2]=='O' or mat[0][z]==mat[1][z]==mat[2][z]=='O':
         st2=1
         break
        if mat[z][0]==mat[z][1]==mat[z][2]=='X' or mat[0][z]==mat[1][z]==mat[2][z]=='X':
         st1=1
         break
    if mat[0][2]==mat[1][1]==mat[2][0]=='X' or st1==1  or mat[0][0]==mat[1][1]==mat[2][2]=='X':
        print("Player 1 won the game")
        exit(0)
    if mat[0][2]==mat[1][1]==mat[2][0]=='O' or st2==1  or mat[0][0]==mat[1][1]==mat[2][2]=='O':
        print("Player 2 won the game")
        exit(0)
    return count
while(True):
    count=game('X',count)
    count=game("O",count)
