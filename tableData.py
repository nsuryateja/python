tableData= [['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']]
for i in range(len(tableData[0])):
      for j in range(len(tableData)):
             print(tableData[j][i].rjust(8),end ='')
      print('\n')
