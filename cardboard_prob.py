'''
Submitted by : Arghyadeep Bhattacharjee

Algorithm : First I created the dictionary of all the exposed outline points. Then
            I looked for change of y-axis value (height)in the sorted dictionary. The
            points of height change are collected in a list and returned.
'''





def cardboard(rect_cord):

    if rect_cord==[] :
        print("List empty")
        return
    result=[]
    cord_dict={}

    for i in rect_cord:
        count=0
        for j in range(i[0],i[1]):
            
            cord_dict[j]=max(i[2],cord_dict.get(j,float('-inf')))
        cord_dict[i[1]]=max(0,cord_dict.get(i[1],float('-inf')))
        
    #print(cord_dict)
    y=None

    for i in sorted(cord_dict):
        if cord_dict[i] != y :
            y=cord_dict[i]
            result.append((i,y))

    return result        
    
       
