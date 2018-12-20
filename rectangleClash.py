print('Please input the cordinates of the rectangles')
if (x2<l2 and x2>l1) and (y1<k1 and y1>k2):
        print(l1,y1,x2,k2)
elif (x1<l1 and x1>l2) and (y1<k1 and y1>k2):
        print(x1,y1,l2,k2)
elif (k1<y1 and k1>y2) and (l2<x2 and l2>x1):
        print(x1,k1,l2,y2)
elif (l1<x2 and l1>x1) and (k1<y1 and k1>y2):
        print(l1,y2,x2,k1)
else:
        print('No Match')
