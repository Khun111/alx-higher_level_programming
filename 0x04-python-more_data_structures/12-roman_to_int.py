#!/usr/bin/python3
def roman_to_int(roman_string):
    inte = 0
    if not isinstance(roman_string, str) or len(roman_string) == 0:
        return (0)
    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    for i in range(len(roman_string)):
        if numeral_dict.get(roman_string[i], 0) == 0:
            return (0)
        if i != len(roman_string) - 1 and
        numeral_dict[roman_string[i]] < numeral_dict[roman_string[i + 1]]:
            inte += numeral_dict[roman_string[i]] * -1
        else:
            inte += numeral_dict[roman_string[i]]
    return (inte)
