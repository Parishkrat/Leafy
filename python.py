from string import ascii_lowercase

while True:
    proceed_c=0
    proceed_r=0
    while (proceed_c==0):
        column=input("Edit value at:\nColumn: ")
        if(ord(column)<ord("j") and ord(column)>ord("a")):
            proceed_c=1
        
        else:
            proceed_c=0 
            print("Invalid Column")
        
        
    while (proceed_r==0):
        row=input("Row: ")
        if(int(row)>10 or int(row)<1):
            proceed_r=0
            print("Invalid Row")
        else:
            proceed_r=1
    new_value=input("New Value: ")
    loc=[column,row]
    #print(loc,new_value)

    def calculate_line_index(loc):

        index = ord(loc[0]) - 97
        calculated=(index*10)+int(loc[1])
        print("Line Number Calculated: "+str(int(calculated+1)))
        return calculated

    with open('data.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    #print(data)
    line_index= calculate_line_index(loc)
    data[line_index] = column.upper()+",v"+row+","+new_value+"\n"
    
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)

    print("Updated Value at "+column.upper()+","+row+" | New Value: "+ new_value+"\n")
