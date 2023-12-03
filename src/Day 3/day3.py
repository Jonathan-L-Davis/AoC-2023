total = 0

valid_symbols = ['*', '-', '%', '$', '=', '@', '#', '/', '&', '+']#, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 517103 - too high
# 517021 - actual number
# 516902 - too low

# 516889 // removed 132, subtracted 13, is the end case

#for symbol in valid_symbols:
#    print(symbol)

def get_part_number(start_pos, end_pos, line_no):
    
    valid = False
    for symbol in valid_symbols:
        if( line_no > 1 and schematic[line_no-1][max(start_pos-1,0):min(end_pos+1,length)].find(symbol) != -1 ):
            valid = True
        if( line_no < ( len(schematic)-1 ) and schematic[line_no+1][max(start_pos-1,0):min(end_pos+1,length)].find(symbol) != -1 ):
            valid = True
        if( schematic[line_no][max(start_pos-1,0):start_pos].find(symbol) != -1 ):
            valid = True
        if( schematic[line_no][end_pos:min(end_pos+1,length)].find(symbol) != -1 ):
            valid = True
            assert end_pos < (length-1) or not schematic[line_no][end_pos:min(end_pos+1,length)].isdigit()
    if valid:
        return int( schematic[line_no][start_pos:end_pos] )
    else:
        return 0
schematic = []

length = 0
line_no = 0
pos = 0
start_pos = 0
end_pos = 0
no_start_num = True
no_end_num = True
with open("input.txt") as file:
    for line in file:
        schematic.append(line.strip())
        length = len(line)
    
    for line in schematic:
        pos = 0
        no_start_num = True
        no_end_num = True
        for char in line:
            if( char.isdigit() and no_start_num ):
                start_pos = pos
                no_start_num = False
            if( pos == len(line)-1 or ( (not char.isdigit() ) and no_end_num and not no_start_num ) ):
                end_pos = pos
                if(pos == len(line)-1 and line[-1].isdigit() ):
                    end_pos += 1
                no_end_num = False
            
            if (not no_start_num) and (not no_end_num):# if both start num and end num are found
                total += int( get_part_number(start_pos, end_pos, line_no) )
                no_start_num = True
                no_end_num = True
            pos += 1
        line_no += 1
print(total)
