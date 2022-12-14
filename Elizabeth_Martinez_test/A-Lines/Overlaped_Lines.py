


def OverlapedLines(line_1, line_2):
   
    line_1 = sorted(line_1)
    line_2 = sorted(line_2)  

    Count_position = 0     
    Flag = False              
    message = "The line"+ str(line_1) + " and the line" + str(line_2) + " does not overlap"
                 

           
    for i in range(2):
        
            while Count_position < len(line_1) and not Flag :
                if line_1[0] <= line_2[Count_position] and line_1[1] >= line_2[Count_position]  :
                    message = "The line "+ str(line_1) + " and the line " + str(line_2) + " overlap"
                    Flag = True
                else:
                    Count_position = Count_position + 1;

    
    return "\n" + message