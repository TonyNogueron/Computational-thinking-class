class Solution:
    def romanToInt(self, s: str) -> int:
        romans = list(s)
        total = 0
        for i in range(len(romans)):
            try:
                if romans[i] == "I" and romans[i + 1] == "M":
                    total += 999
                    i += 1
                    break
                elif romans[i] == "X" and romans[i + 1] == "M":
                    total += 990
                    i += 1
                    break
                elif romans[i] == "C" and romans[i + 1] == "M":
                    total += 900
                    i += 1
                    break
                elif romans[i] == "I" and romans[i + 1] == "D":
                    total += 499
                    i += 1
                    break
                elif romans[i] == "X" and romans[i + 1] == "D":
                    total += 490
                    i += 1
                    break
                elif romans[i] == "C" and romans[i + 1] == "D":
                    total += 400
                    i += 1
                    break
                elif romans[i] == "I" and romans[i + 1] == "C":
                    total += 99
                    i += 1
                    break
                elif romans[i] == "X" and romans[i + 1] == "C":
                    total += 90
                    i += 1
                    break
                elif romans[i] == "I" and romans[i + 1] == "L":
                    total += 49
                    i += 1
                    break
                elif romans[i] == "X" and romans[i + 1] == "L":
                    total += 40
                    i += 1
                    break
                elif romans[i] == "I" and romans[i + 1] == "X":
                    total += 9
                    i += 1
                    break
                elif romans[i] == "I" and romans[i + 1] == "V":
                    total += 4
                    i += 1
                    break
                elif romans[i] == "M":
                    total += 1000
                elif romans[i] == "D":
                    total += 500
                elif romans[i] == "C":
                    total += 100
                elif romans[i] == "L":
                    total += 50
                elif romans[i] == "X":
                    total += 10
                elif romans[i] == "V":
                    total += 5
                elif romans[i] == "I":
                    total += 1
            except:
                if romans[i] == "M":
                    total += 1000
                elif romans[i] == "D":
                    total += 500
                elif romans[i] == "C":
                    total += 100
                elif romans[i] == "L":
                    total += 50
                elif romans[i] == "X":
                    total += 10
                elif romans[i] == "V":
                    total += 5
                elif romans[i] == "I":
                    total += 1
                else:
                    total += 0
        return total
    
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        s.replace("IV","IIII")
        s.replace("IX","VIIII")
        s.replace("XL","XXXX")
        s.replace("IL","XXXXVIIII")
        s.replace("XC","LXXXX")
        s.replace("IC","LXXXXVIIII")
        s.replace("CD","CCCC")    
        s.replace("XD","CCCCLXXXX")
        s.replace("ID","CCCCLXXXXVIIII")
        s.replace("CM","DCCCC")
        s.replace("XM","DCCCCLXXXX")
        s.replace("IM","DCCCCLXXXXVIIII")
        total = 0
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for letter in s:
            total += roman[letter]
        return total
"""


"""


class Solution:
    def romanToInt(self, s: str) -> int:
        romans = list(s)
        total = 0
        for i in range(len(romans)):
            try:
                if romans[i] == "I":
                    if romans[i+1] == "V":
                        total += 4
                        i += 1
                        break
                    elif romans[i+1] == "X":
                        total += 9
                        i += 1
                        break
                    else:
                        total += 1
                elif romans[i] == "X":
                    if romans[i+1] == "L":
                        total += 40
                        i += 1
                        break
                    elif romans[i+1] == "C":
                        total += 90
                        i += 1
                        break
                    else:
                        total += 10
                elif romans[i] == "C":
                    if romans[i+1] == "D":
                        total += 400
                        i += 1
                        break
                    elif romans[i+1] == "M":
                        total += 900  
                        i += 1
                        break
                    else:
                        total += 100
                elif romans[i] == "M":
                    total += 1000
                elif romans[i] == "D":
                    total += 500
                elif romans[i] == "L":
                    total += 50
                elif romans[i] == "V":
                    total += 5
            except:
                if romans[i] == "M":
                    total += 1000
                elif romans[i] == "D":
                    total += 500
                elif romans[i] == "C":
                    total += 100
                elif romans[i] == "L":
                    total += 50
                elif romans[i] == "X":
                    total += 10
                elif romans[i] == "V":
                    total += 5
                elif romans[i] == "I":
                    total += 1
        return total
"""