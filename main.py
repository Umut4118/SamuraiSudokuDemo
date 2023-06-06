import numpy as np
import time
import threading


File = open("Data.txt", "r")
Data = File.read()
File.close()
File = open("Points.txt", "w")
grid1 = [[Data[0],Data[1],Data[2],Data[3],Data[4],Data[5],Data[6],Data[7],Data[8]],
         [Data[19],Data[20],Data[21],Data[22],Data[23],Data[24],Data[25],Data[26],Data[27]],
         [Data[38],Data[39],Data[40],Data[41],Data[42],Data[43],Data[44],Data[45],Data[46]],
         [Data[57],Data[58],Data[59],Data[60],Data[61], Data[62], Data[63], Data[64], Data[65]],
         [Data[76], Data[77], Data[78], Data[79], Data[80], Data[81], Data[82], Data[83], Data[84]],
         [Data[95], Data[96], Data[97], Data[98], Data[99], Data[100], Data[101], Data[102], Data[103]],
         [Data[114], Data[115], Data[116], Data[117], Data[118], Data[119], Data[120], Data[121], Data[122]],
         [Data[136],Data[137],Data[138],Data[139],Data[140],Data[141],Data[142],Data[143],Data[144]],
         [Data[158],Data[159],Data[160],Data[161],Data[162],Data[163],Data[164],Data[165],Data[166]]]
g1 = [   [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
g1l = [   [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        if grid1[i][j] == "*":
            g1[i][j] = 0
        else:
            g1[i][j] = int(grid1[i][j])
grid2 = [[Data[9],Data[10],Data[11],Data[12],Data[13],Data[14],Data[15],Data[16],Data[17]],
         [Data[28],Data[29],Data[30],Data[31],Data[32],Data[33],Data[34],Data[35],Data[36]],
         [Data[47],Data[48],Data[49],Data[50],Data[51],Data[52],Data[53],Data[54],Data[55]],
         [Data[66], Data[67], Data[68], Data[69], Data[70], Data[71], Data[72], Data[73], Data[74]],
         [Data[85], Data[86], Data[87], Data[88], Data[89], Data[90], Data[91], Data[92], Data[93]],
         [Data[104], Data[105], Data[106], Data[107], Data[108], Data[109], Data[110], Data[111], Data[112]],
         [Data[126],Data[127],Data[128],Data[129],Data[130],Data[131],Data[132],Data[133],Data[134]],
         [Data[148],Data[149],Data[150],Data[151],Data[152],Data[153],Data[154],Data[155],Data[156]],
         [Data[170],Data[171],Data[172],Data[173],Data[174],Data[175],Data[176],Data[177],Data[178]]]
g2 = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
g2l = [   [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        if grid2[i][j] == "*":
            g2[i][j] = 0
        else:
            g2[i][j] = int(grid2[i][j])
grid3 = [[Data[120],Data[121],Data[122],Data[123],Data[124],Data[125],Data[126],Data[127],Data[128]],
         [Data[142],Data[143],Data[144],Data[145],Data[146],Data[147],Data[148],Data[149],Data[150]],
         [Data[164],Data[165],Data[166],Data[167],Data[168],Data[169],Data[170],Data[171],Data[172]],
         [Data[180],Data[181],Data[182],Data[183],Data[184],Data[185],Data[186],Data[187],Data[188]],
         [Data[190], Data[191], Data[192], Data[193], Data[194], Data[195], Data[196], Data[197], Data[198]],
         [Data[200], Data[201], Data[202], Data[203], Data[204], Data[205], Data[206], Data[207], Data[208]],
         [Data[216],Data[217],Data[218],Data[219],Data[220],Data[221],Data[222],Data[223],Data[224]],
         [Data[238],Data[239],Data[240],Data[241],Data[242],Data[243],Data[244],Data[245],Data[246]],
         [Data[260],Data[261],Data[262],Data[263],Data[264],Data[265],Data[266],Data[267],Data[268]]]
g3 = [   [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
g3l = [   [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        if grid3[i][j] == "*":
            g3[i][j] = 0
        else:
            g3[i][j] = int(grid3[i][j])
grid4 = [[Data[210],Data[211],Data[212],Data[213],Data[214],Data[215],Data[216],Data[217],Data[218]],
         [Data[232],Data[233],Data[234],Data[235],Data[236],Data[237],Data[238],Data[239],Data[240]],
         [Data[254],Data[255],Data[256],Data[257],Data[258],Data[259],Data[260],Data[261],Data[262]],
         [Data[276],Data[277],Data[278],Data[279],Data[280],Data[281],Data[282],Data[283],Data[284]],
         [Data[295],Data[296],Data[297],Data[298],Data[299],Data[300],Data[301],Data[302],Data[303]],
         [Data[314],Data[315],Data[316],Data[317],Data[318],Data[319],Data[320],Data[321],Data[322]],
         [Data[333],Data[334],Data[335],Data[336],Data[337],Data[338],Data[339],Data[340],Data[341]],
         [Data[352],Data[353],Data[354],Data[355],Data[356],Data[357],Data[358],Data[359],Data[360]],
         [Data[371],Data[372],Data[373],Data[374],Data[375],Data[376],Data[377],Data[378],Data[379]]]
g4 = [   [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
g4l = [   [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        if grid4[i][j] == "*":
            g4[i][j] = 0
        else:
            g4[i][j] = int(grid4[i][j])
grid5 = [[Data[222],Data[223],Data[224],Data[225],Data[226],Data[227],Data[228],Data[229],Data[230]],
         [Data[244],Data[245],Data[246],Data[247],Data[248],Data[249],Data[250],Data[251],Data[252]],
         [Data[266],Data[267],Data[268],Data[269],Data[270],Data[271],Data[272],Data[273],Data[274]],
         [Data[285],Data[286],Data[287],Data[288],Data[289],Data[290],Data[291],Data[292],Data[293]],
         [Data[304],Data[305],Data[306],Data[307],Data[308],Data[309],Data[310],Data[311],Data[312]],
         [Data[323],Data[324],Data[325],Data[326],Data[327],Data[328],Data[329],Data[330],Data[331]],
         [Data[342],Data[343],Data[344],Data[345],Data[346],Data[347],Data[348],Data[349],Data[350]],
         [Data[361],Data[362],Data[363],Data[364],Data[365],Data[366],Data[367],Data[368],Data[369]],
         [Data[380],Data[381],Data[382],Data[383],Data[384],Data[385],Data[386],Data[387],Data[388]]]
g5 = [   [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
g5l = [   [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        if grid5[i][j] == "*":
            g5[i][j] = 0
        else:
            g5[i][j] = int(grid5[i][j])

"""for i in range(0, 9):
 print(g1[i])
print("\n")
for i in range(0, 9):
 print(g2[i])
print("\n")
for i in range(0, 9):
 print(g3[i])
print("\n")
for i in range(0, 9):
 print(g4[i])
print("\n")
for i in range(0, 9):
 print(g5[i])
print("\n")
"""
def possiableg1(row, column, number):

   if row > 5 and column > 5:
       for i in range(0, 9):
          if g3[row-6][i] == number:
           return False

       for i in range(0, 9):
        if g3[i][column-6] == number:
           return False

   for i in range(0, 9):
      if g1[row][i] == number:
          return False

   for i in range(0, 9):
     if g1[i][column] == number:
      return False

   x0 = (column // 3) * 3
   y0 = (row // 3) * 3
   for i in range(x0, x0 + 3):
    for j in range(y0, y0 + 3):
        if g1[j][i] == number:
          return False

   return True
def possiableg2(row, column, number):
   if row > 5 and column < 3:


       for i in range(0, 9):
          if g3[row - 6][i] == number:

           return False


       for i in range(0, 9):
        if g3[i][column + 6] == number:

         return False

   for i in range(0, 9):
      if g2[row][i] == number:
          return False

   for i in range(0, 9):
     if g2[i][column] == number:
      return False

   x0 = (column // 3) * 3
   y0 = (row // 3) * 3
   for i in range(x0, x0 + 3):
    for j in range(y0, y0 + 3):
        if g2[j][i] == number:
          return False

   return True
def possiableg3(row, column, number):

   if row < 3 and column < 3:
       for i in range(0, 9):
          if g1[row + 6][i] == number:
           return False

       for i in range(0, 9):
        if g1[i][column + 6] == number:
         return False
   if row < 3 and column > 5:
       for i in range(0, 9):
           if g2[row + 6][i] == number:
               return False

       for i in range(0, 9):
           if g2[i][column - 6] == number:
               return False
   if row > 5 and column < 3:
       for i in range(0, 9):
           if g4[row - 6][i] == number:
               return False

       for i in range(0, 9):
           if g4[i][column + 6] == number:
               return False
   if row > 5 and column > 5:
       for i in range(0, 9):
           if g5[row - 6][i] == number:
               return False

       for i in range(0, 9):
           if g5[i][column - 6] == number:
               return False

   for i in range(0, 9):
      if g3[row][i] == number:
          return False

   for i in range(0, 9):
     if g3[i][column] == number:
      return False

   x0 = (column // 3) * 3
   y0 = (row // 3) * 3
   for i in range(x0, x0 + 3):
    for j in range(y0, y0 + 3):
        if g3[j][i] == number:
          return False

   return True
def possiableg4(row, column, number):

   if row < 3 and column > 5:
       for i in range(0, 9):
          if g3[row + 6][i] == number:
           return False

       for i in range(0, 9):
        if g3[i][column - 6] == number:
         return False

   for i in range(0, 9):
      if g4[row][i] == number:
          return False

   for i in range(0, 9):
     if g4[i][column] == number:
      return False

   x0 = (column // 3) * 3
   y0 = (row // 3) * 3
   for i in range(x0, x0 + 3):
    for j in range(y0, y0 + 3):
        if g4[j][i] == number:
          return False

   return True
def possiableg5(row, column, number):

   if row < 3 and column < 3:
       for i in range(0, 9):
          if g3[row + 6][i] == number:
           return False

       for i in range(0, 9):
        if g3[i][column + 6] == number:
         return False

   for i in range(0, 9):
      if g5[row][i] == number:
          return False

   for i in range(0, 9):
     if g5[i][column] == number:
      return False

   x0 = (column // 3) * 3
   y0 = (row // 3) * 3
   for i in range(x0, x0 + 3):
    for j in range(y0, y0 + 3):
        if g5[j][i] == number:
          return False

   return True

def solveg1():
    for row in range(0, 9):
        for column in range(0, 9):
            if g1[row][column] == 0:
                for number in range(1, 10):
                    if possiableg1(row, column, number):
                        g1[row][column] = number
                        File.write("grid1:"+str(row)+" "+str(column)+" "+str(number)+"\n")
                        solveg1()
                        g1[row][column] = 0
                return
    for i in range(0, 9):
        for j in range(0, 9):
             g1l[i][j]=g1[i][j]
def solveg11():
    for row in range(8, -1):
        for column in range(8, -1):
            if g5[row][column] == 0:
                for number in range(1, 10):
                    if possiableg5(row, column, number):
                        g5[row][column] = number
                        File.writelines("grid1*:" + str(row) + " " + str(column) + " " + str(number)+"\n")
                        solveg11()
                        g5[row][column] = 0
                return
def solveg2():
        for row in range(0, 9):
            for column in range(0, 9):
                if g2[row][column] == 0:
                    for number in range(1, 10):
                        if possiableg2(row, column, number):
                            g2[row][column] = number
                            File.write("grid2:" + str(row) + " " + str(column) + " " + str(number)+"\n")
                            solveg2()
                            g2[row][column] = 0
                    return
        for i in range(0, 9):
            for j in range(0, 9):
                g2l[i][j] = g2[i][j]
def solveg22():
    for row in range(8, -1):
        for column in range(8, -1):
            if g5[row][column] == 0:
                for number in range(1, 10):
                    if possiableg5(row, column, number):
                        g5[row][column] = number
                        File.writelines("grid2*:" + str(row) + " " + str(column) + " " + str(number)+"\n")
                        solveg22()
                        g5[row][column] = 0
                return
def solveg3():
    for row in range(0, 9):
        for column in range(0, 9):
            if g3[row][column] == 0:
                for number in range(1, 10):
                    if possiableg3(row, column, number):
                        g3[row][column] = number
                        """print(row)
                        print(column)
                        print(number)"""
                        File.write("grid3:" + str(row) + " " + str(column) + " " + str(number)+"\n")
                        solveg3()
                        g3[row][column] = 0
                return
    for i in range(0, 9):
        for j in range(0, 9):
            g3l[i][j] = g3[i][j]
def solveg33():
    for row in range(8, -1):
        for column in range(8, -1):
            if g5[row][column] == 0:
                for number in range(1, 10):
                    if possiableg5(row, column, number):
                        g5[row][column] = number
                        File.writelines("grid3*:" + str(row) + " " + str(column) + " " + str(number)+"\n")
                        solveg33()
                        g5[row][column] = 0
                return
def solveg4():
        for row in range(0, 9):
            for column in range(0, 9):
                if g4[row][column] == 0:
                    for number in range(1, 10):
                        if possiableg4(row, column, number):
                            g4[row][column] = number
                            File.write("grid4:" + str(row) + " " + str(column) + " " + str(number)+"\n")
                            solveg4()
                            g4[row][column] = 0
                    return
        for i in range(0, 9):
            for j in range(0, 9):
                g4l[i][j] = g4[i][j]
def solveg44():
    for row in range(8, -1):
        for column in range(8, -1):
            if g5[row][column] == 0:
                for number in range(1, 10):
                    if possiableg5(row, column, number):
                        g5[row][column] = number
                        File.writelines("grid4*:" + str(row) + " " + str(column) + " " + str(number)+"\n")
                        solveg44()
                        g5[row][column] = 0
                return
def solveg5():
      for row in range(0, 9):
            for column in range(0, 9):
                if g5[row][column] == 0:
                    for number in range(1, 10):
                        if possiableg5(row, column, number):
                            g5[row][column] = number
                            File.writelines("grid5:" + str(row) + " " + str(column) + " " + str(number)+"\n")
                            solveg5()
                            g5[row][column] = 0
                    return
      for i in range(0, 9):
          for j in range(0, 9):
              g5l[i][j] = g5[i][j]

def solveg55():
    for row in range(8, -1):
        for column in range(8, -1):
            if g5[row][column] == 0:
                for number in range(1, 10):
                    if possiableg5(row, column, number):
                        g5[row][column] = number
                        File.writelines("grid5:" + str(row) + " " + str(column) + " " + str(number)+"\n")
                        solveg55()
                        g5[row][column] = 0
                return


t1 = threading.Thread(target=solveg1())
t2 = threading.Thread(target=solveg2())
t3 = threading.Thread(target=solveg3())
t4 = threading.Thread(target=solveg4())
t5 = threading.Thread(target=solveg5())

t11 = threading.Thread(target=solveg11())
t22 = threading.Thread(target=solveg22())
t44 = threading.Thread(target=solveg44())
t33 = threading.Thread(target=solveg33())
t55 = threading.Thread(target=solveg55())

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t11.start()
t22.start()
t33.start()
t44.start()
t55.start()


print(str(g1l[0])+"               "+str(g2l[0]))
print(str(g1l[1])+"               "+str(g2l[1]))
print(str(g1l[2])+"               "+str(g2l[2]))
print(str(g1l[3])+"               "+str(g2l[3]))
print(str(g1l[4])+"               "+str(g2l[4]))
print(str(g1l[5])+"               "+str(g2l[5]))
print(str(g1l[6])+"               "+str(g2l[6]))
print(str(g1l[7])+"               "+str(g2l[7]))
print(str(g1l[8])+"               "+str(g2l[8]))
print("                     "+str(g3l[0]))
print("                     "+str(g3l[1]))
print("                     "+str(g3l[2]))
print("                     "+str(g3l[3]))
print("                     "+str(g3l[4]))
print("                     "+str(g3l[5]))
print("                     "+str(g3l[6]))
print("                     "+str(g3l[7]))
print("                     "+str(g3l[8]))
print(str(g4l[0])+"               "+str(g5l[0]))
print(str(g4l[1])+"               "+str(g5l[1]))
print(str(g4l[2])+"               "+str(g5l[2]))
print(str(g4l[3])+"               "+str(g5l[3]))
print(str(g4l[4])+"               "+str(g5l[4]))
print(str(g4l[5])+"               "+str(g5l[5]))
print(str(g4l[6])+"               "+str(g5l[6]))
print(str(g4l[7])+"               "+str(g5l[7]))
print(str(g4l[8])+"               "+str(g5l[8]))



