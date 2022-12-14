from Overlaped_Lines import OverlapedLines

if __name__ == '__main__':
    
    try:

        def numberLine(numberOfline):
            text_line= input("Please enter points x1 x2 For line #"+str(numberOfline)+" separated by a space:  ")  
            line =tuple(int(item) for item in text_line.split())
            if( len(line) != 2):
                print("Input should have 2 numbers seperated by a space : x1 x2 ")
            return line
                

        line_1 = numberLine(1)
        line_2 = numberLine(2)


        result = OverlapedLines(line_1, line_2)
        print(result)

    
    except ValueError:
    
        print("Please make sure to enter 2 numbers separated by a space:  ")