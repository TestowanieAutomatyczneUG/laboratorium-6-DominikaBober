def roman(number):

    try:
        jedności = number%10
        dziesiatki = int((number%100 - jedności)/10)
        setki = int((number%1000 - dziesiatki - jedności)/100)
        tysiace = int((number%10000 -setki - dziesiatki - jedności)/1000)

        if jedności<4:
            roman_number = jedności*"I"
        elif jedności==4:
            roman_number = "IV"
        elif jedności<9:
            roman_number = "V" + (jedności-5)*"I"
        else:
            roman_number = "IX"
        
        if dziesiatki<4:
            roman_number =  dziesiatki*"X" + roman_number
        elif dziesiatki==4:
            roman_number = "XL" + roman_number
        elif dziesiatki<9:
            roman_number = "L" + (dziesiatki-5)*"X" + roman_number
        else:
            roman_number = "XC" + roman_number
        
        if setki<4:
            roman_number =  setki*"C" + roman_number
        elif setki==4:
            roman_number = "CD" + roman_number
        elif setki<9:
            roman_number = "D" + (setki-5)*"C" + roman_number
        else:
            roman_number = "CM" + roman_number

        roman_number = tysiace*"M" + roman_number

        return roman_number
    
    except ConnectionError:
        raise Exception("Wrong number")
