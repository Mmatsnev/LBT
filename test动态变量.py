#!usr/bin/python3
# -*- coding: utf-8 -*-

# class test(object):
#     def __init__(self):
#         super().__init__()

#         for i in range(5):
#             exec('var{} = {}'.format(i, i))
#             print(var0)

# if __name__ == "__main__":
#     test = test()
    
gridLayoutRow = 0
gridLayoutCol = 0
for i in range(15):
    print(gridLayoutRow, gridLayoutCol)
    gridLayoutCol += 1
    if gridLayoutCol == 4:
        gridLayoutCol = 0
        gridLayoutRow += 1
