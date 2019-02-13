"""
pixel1 = [111,0,222]
pixel2 = [123,111,223]
pixel3 = [157,235,0]
pixel4 = [111,0,222]
pixel5 = [123,111,223]
pixel6 = [157,235,0]
pixel7 = [111,0,222]
pixel8 = [123,111,223]
pixel9 = [157,235,0]

photo = [[pixel1,pixel2,pixel3],
         [pixel4,pixel5,pixel6],
         [pixel7,pixel8,pixel9]]

"""
photo = [[[111,0,222],[123,111,223],[157,235,0]],
         [[234,502,401],[103,151,723],[357,835,206]],
         [[185,320,282],[178,634,854],[154,236,450]]]

photoGrey = photo
for i in range(0 , len(photoGrey)):
    for j in range (0, len(photoGrey[i])):
        total = 0
        for k in range (0, len(photoGrey[i][j])):
            total = total + photoGrey[i][j][k]

        total = total//3

        for n in range (0,len(photoGrey[i][j])):
            photoGrey[i][j][n] = total

print("================Grey Scale Of Photo===============")
print(photoGrey)
"""
"""
photo = [[[111,0,222],[111,0,222],[111,0,222]],
         [[111,0,222],[111,0,222],[111,0,222]],
         [[111,0,222],[111,0,222],[111,0,222]]]

photoRotate = photo
for i in range(0,len(photoRotate)):
    for j in range (0,len(photoRotate[i]),3):
        for k in range (0,len(photoRotate[i][j])):

            photoRotate[i][j][k] = photoRotate[i][j][0]

for i in range(0,len(photoRotate)):
    for j in range (1,len(photoRotate[i]),3):
        for k in range (0,len(photoRotate[i][j])):

            photoRotate[i][j][k] = photoRotate[i][j][1]

for i in range(0,len(photoRotate)):
    for j in range (2,len(photoRotate[i]),3):
        for k in range (0,len(photoRotate[i][j])):

            photoRotate[i][j][k] = photoRotate[i][j][2]
print(">>>>>>>>>>>>Rotation of Photo<<<<<<<<<<<<<")
print(photoRotate)
