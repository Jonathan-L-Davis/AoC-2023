total = 0
first = 'c'
last = 'c'

valid_digits = ['1','2','3','4','5','6','7','8','9','one','two','three','four','five','six','seven','eight','nine']

with open("input.txt") as file:
    for line in file:
        first_pos = 10000
        last_pos = -1
        for dig in valid_digits:
        
            if( line.find(dig) < first_pos and line.find(dig) >= 0 ):
                first = dig
                first_pos = line.find(dig)
            if( line.rfind(dig) > last_pos ):
                last = dig
            last_pos = max( line.rfind(dig), last_pos )
        match first:
            case 'one':
                first = "1"
            case 'two':
                first = "2"
            case 'three':
                first = "3"
            case 'four':
                first = "4"
            case 'five':
                first = "5"
            case 'six':
                first = "6"
            case 'seven':
                first = "7"
            case 'eight':
                first = "8"
            case 'nine':
                first = "9"
        match last:
            case 'one':
                last = "1"
            case 'two':
                last = "2"
            case 'three':
                last = "3"
            case 'four':
                last = "4"
            case 'five':
                last = "5"
            case 'six':
                last = "6"
            case 'seven':
                last = "7"
            case 'eight':
                last = "8"
            case 'nine':
                last = "9"
        print( str(first)+" "+str(last) )
        total += int( str(first)+str(last) )
        
print(total)
