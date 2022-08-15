class translator:

    def deciToRoman(self, num):
        roman = ''

        while(num != 0):
            if num >= 1000:
                roman = roman+'M'
                num = num-1000
            elif num >= 900:
                roman = roman+'CM'
                num = num-900
            elif num >= 500:
                roman = roman+'D'
                num = num-500
            elif num >= 400:
                roman = roman+'CD'
                num = num-400
            elif num >= 100:
                roman = roman+'C'
                num = num-100
            elif num >= 90:
                roman = roman+'XC'
                num = num-90
            elif num >= 50:
                roman = roman+'L'
                num = num-50
            elif num >= 40:
                roman = roman+'XL'
                num = num-40
            elif num >= 10:
                roman = roman+'X'
                num = num-10
            elif num >= 9:
                roman = roman+'IX'
                num = num-9
            elif num >= 5:
                roman = roman+'V'
                num = num-5
            elif num >= 4:
                roman = roman+'IV'
                num = num-4
            elif num >= 1:
                roman = roman+'I'
                num = num-1
        return roman

    def romanToDeci(self, s):
        num1 = 0
        while(s != ''):
            if s[0] == 'M':
                num1 = num1 + 1000
                s = s[1:]
            elif s[0] == 'C':
                if len(s) > 1:
                    if s[1] == 'M':
                        num1 = num1 + 900
                        s = s[2:]
                    elif s[1] == 'D':
                        num1 = num1 + 400
                        s = s[2:]
                    else:
                        num1 = num1 + 100
                        s = s[1:]
                else:
                    num1 = num1 + 100
                    s = s = s[1:]
            elif s[0] == 'D':
                num1 = num1 + 500
                s = s = s[1:]
            elif s[0] == 'X':
                if len(s) > 1:
                    if s[1] == 'C':
                        num1 = num1 + 90
                        s = s[2:]
                    elif s[1] == 'L':
                        num1 = num1 + 40
                        s = s[2:]
                    else:
                        num1 = num1 + 10
                        s = s[1:]
                else:
                    num1 = num1 + 10
                    s = s[1:]
            elif s[0] == 'L':
                num1 = num1 + 50
                s = s[1:]
            elif s[0] == 'V':
                num1 = num1 + 5
                s = s = s[1:]
            elif s[0] == 'I':
                if len(s) > 1:
                    if s[1] == 'X':
                        num1 = num1 + 9
                        s = s[2:]
                    elif s[1] == 'V':
                        num1 = num1 + 4
                        s = s[2:]
                    else:
                        num1 = num1 + 1
                        s = s[1:]
                else:
                    num1 = num1 + 1
                    s = s[1:]
        return num1


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))
