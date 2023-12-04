from itertools import compress

total = 0

valid_symbols = ['*', '-', '%', '$', '=', '@', '#', '/', '&', '+']#, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 517103 - too high
# 517021 - actual number
# 516902 - too low

# 516889 // removed 132, subtracted 13, is the end case



# 81296995 - cheated to get, still working out my last issue
# 80337639 - too low
# 66334255 - too low - not accounting for more than 1 gear per substring

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def BIG_FIND ( string, sub,_line_no ):
    #print( _line_no,":",list(find_all( string,sub) ), ":"+string)
    return( list(find_all( string,sub) ) )


def find_gears(string,_line_no,_pos):
    #print(string)
    #print( BIG_FIND(string,"*",_line_no) )
    for positon in BIG_FIND(string,"*",_line_no):
        gear_set.append( list( (_line_no, _pos+positon, int( schematic[line_no][start_pos:end_pos] ) ) ) )
    

def get_part_number(start_pos, end_pos, line_no):
    
    valid = False
    
    
    for symbol in valid_symbols:
        st = max(start_pos-1,0)
        en = min(end_pos+1,length)
        
        
        if( line_no > 0 and schematic[line_no-1][st:en].find(symbol) != -1 ):
            valid = True
            if( symbol == "*" ):
                find_gears(schematic[line_no-1][st:en],line_no-1,st)
        if( line_no < ( len(schematic)-1 ) and schematic[line_no+1][st:en].find(symbol) != -1 ):
            valid = True
            if( symbol == "*" ):
                find_gears(schematic[line_no+1][st:en],line_no+1,st)
        
        if( schematic[line_no][st:start_pos].find(symbol) != -1 ):
            valid = True
            if( symbol == "*" ):
                find_gears(schematic[line_no][st:start_pos],line_no,st)
        
        if( schematic[line_no][end_pos:en].find(symbol) != -1 ):
            valid = True
            if( symbol == "*" ):
                find_gears(schematic[line_no][end_pos:en],line_no,en-1)
                print(schematic[line_no][end_pos:en])
    
    if valid:
        #print(schematic[line_no][start_pos:end_pos])
        return int( schematic[line_no][start_pos:end_pos] )
    else:
        return 0

schematic = []
gear_set = [[]]
gear_sum = 0
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
                    #print(schematic[line_no][start_pos:end_pos])
                no_end_num = False
            
            if (not no_start_num) and (not no_end_num):# if both start num and end num are found
                total += int( get_part_number(start_pos, end_pos, line_no) )
                no_start_num = True
                no_end_num = True
            pos += 1
        line_no += 1
print(total)




gear_set.pop(0)
for gear in gear_set :
    print(gear)
    
    new_set = [ elem[0]==gear[0] and elem[1] == gear[1] for elem in gear_set ]
    new_set = [i for i, x in enumerate(new_set) if x]
    #print(new_set)
    mul = 1;
    if(len(new_set) == 2):
        for idx in new_set:
            mul*=  gear_set[idx][2]
        gear_sum += mul



print(int(gear_sum/2))
