
'''
##Incomplete##

submitted by: Arghyadeep Bhattacharjee

Algorithm   : First I tried to check all the exposed(not under any other rectangle area)corners of all the rectangles
              Then I tried to find all the intersections of the rectangles and then filter all the exposed intersections.
              Finally, I added both these lists and then removed duplicates (converted to set), and then took the alternate
              index values which signifies change of outline.
              The code has some bugs, I am working to get to them.
              "outline(A)" is the main function
'''



##Finding all corners##

def find_corners(P):                

    result=[(P[0],0),(P[0],P[2]),(P[1],P[2]),(P[1],0)]
    return result
    


##Function to check if a given point is exposed (in outline) or not.

def exposed(c,A,pos):
    exp=True
    for i in A:
      if pos=='l':  
        if i[0][0] < c[0] and i[3][0] < c[0] : continue
        if i[0][0] > c[0] and i[3][0] > c[0] : continue
        if i[2][0] == c[0] :
            if i[2][1] == c[1] : return False
            else: continue
        elif i[1][0] == c[0]:
            if i[1][1] > c[1] : return False
            else: continue
        elif c[0] > i[0][0] and c[0] < i[2][0] :
            if c[1] > i[1][1]: continue
            else: return False
      if pos=='r':
        if i[0][0] < c[0] and i[3][0] < c[0] : continue
        if i[0][0] > c[0] and i[3][0] > c[0] : continue
        if i[2][0] == c[0]:
            if i[2][1] > c[1] : return False
            else: continue
        elif i[1][0] == c[0]:
            if c[1]==i[1][1] : return False
            else : continue
        elif c[0] >i[0][0] and c[0] < i[2][0]:
            if c[1] > i[1][1] : continue
            else: return False

      if pos=='g':
          if i[0][0] < c[0] and i[3][0] < c[0] : continue
          if i[0][0] > c[0] and i[3][0] > c[0] : continue
          if i[0][0] < c[0] and i[3][0] > c[0]:
              if i[1][1] > c[1]: return False
              else: continue              
          
    return exp        


### Main function
def outline(A):
    exposed_list=[]
    k=[]
    for i in A:
        k.append(find_corners(i))

    count=0   ##
    for i in k:
       for j in i:
           if j== i[0] or j==i[1] : pos='l'
           else: pos='r'
           if exposed(j,k[:count]+k[count+1:],pos): exposed_list.append(j)
       count+=1
    


    inter_list=[]
    inter_exposed=[]
    count=-1 ##
    for i in k:
        count+=1
        for j in k[count+1:]:
            if j[1][0] < i[1][0] and i[1][0] < j[2][0] :  #intersect True
                 if  j[1][1] < i[1][1]: inter_list.append((i[0][1],j[1][1]))
                 if  j[1][1] > i[1][1]: inter_list.append((j[2][0],i[1][1]))
            if j[0][0] > i[0][0] and j[3][0] < i[3][0] : #inside
                if j[1][1] > i[1][1]:
                    inter_list.append((j[0][0],i[1][1]))
                    inter_list.append((j[3][0],i[1][1]))
            if j[0][0] < i[2][0] and j[3][0] > i[2][0] :
                if j[1][1] < i[2][1]: inter_list.append((i[2][0],j[1][1]))
                if j[1][1] > i[2][1]: inter_list.append((j[0][0],i[1][1]))
       

    for i in inter_list :
        if exposed(i,k,'g') : inter_exposed.append(i)

    
    last_set= list(set(inter_exposed + exposed_list))
    
    final_set=[]
    for i in range(0,len(last_set),2):
        final_set.append(last_set[i])
   
    return sorted(final_set)
    
    
                    
                
        








           
