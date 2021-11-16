def roman(number):

    try:
        jedności = number%10
        dziesiatki = int((number%100 - jedności)/10)
        setki = int((number%1000 - dziesiatki - jedności)/100)
        tysiace = int((number%10000 -setki - dziesiatki - jedności)/1000)

        znaki = {"IVX": jedności, "XLC": dziesiatki, "CDM": setki}
        roman_number = ""

        for cykl in znaki:
        
            if znaki[cykl]<4:
                roman_number =  znaki[cykl]*cykl[0] + roman_number
            elif znaki[cykl]==4:
                roman_number = cykl[:2] + roman_number
            elif znaki[cykl]<9:
                roman_number = cykl[1] + (znaki[cykl]-5)*cykl[0] + roman_number
            else:
                roman_number = cykl[0] + cykl[2] + roman_number

        roman_number = tysiace*"M" + roman_number

        return roman_number
    
    except ConnectionError:
        raise Exception("Wrong number")
