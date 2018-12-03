zero_to_nine = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 
                5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}

ten_to_nineteen = { 10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 
                    14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 
                    17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen'}

tens = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5 : 'fifty',
        6: 'sixty', 7 : 'seventy', 8 : 'eighty' , 9 : 'ninety'}

placewords = {3 : 'hundred', 4 : 'thousand', 7 : 'million', 10 : 'billion', 13: 'trillion' }

def number_to_word(number):
    num_str = str(number)
    if len(num_str) == 1:
        return zero_to_nine[number]
    elif 10 <= number <= 19:
        return ten_to_nineteen[number]
    else:
        numword = [ ]
        not_zero = False
        teen = False
        for i in range(len(num_str), 0, -1):
            curnum = int(num_str[i * -1])
            if not teen:
                if curnum != 0:
                    not_zero = True
                    if i % 3 == 2:
                        if curnum != 1:
                            numword.append(tens[curnum])
                        else:
                            numword.append(ten_to_nineteen[int(str(curnum) + num_str[(i - 1) * -1])])
                            teen = True
                    elif i % 3 == 1:
                        numword.append(zero_to_nine[curnum])
                    else:
                        numword.append(zero_to_nine[curnum])
            else:
                teen = False
            
            if i % 3 == 0 and curnum != 0 and i > 3:
                numword.append(placewords[3])
            
            if i in placewords and not_zero:
                numword.append(placewords[i])
                not_zero = False

        return ' '.join(numword)

def user_num():
    user_number = input("Type A Number: ")
    print (number_to_word(int(user_number)))

user_num()