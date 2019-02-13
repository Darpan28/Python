TotalBricks = 0

def Bricks(BricksNum):
    global TotalBricks

    John = 1
    for John in range(John,BricksNum+1):
        TotalBricks = TotalBricks + John
        print("John")
        print(John)
        if (TotalBricks < BricksNum):
            for Mark in range(John,John+1):
                Mark = 2*John
                TotalBricks = TotalBricks+Mark
                print("Mark")
                print(Mark)
                print("Total No Bricks is: ",TotalBricks)


        if(TotalBricks >= BricksNum):

            break

def Condition():

Bricks(13)

