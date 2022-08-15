class translator:

    def deciToRoman(self, num):
        uint = num % 10
        ten = int(((num % 100)-uint)/10)
        hundreds = int(((num % 1000)-(ten+uint))/100)
        thousands = int((num % 10000-(hundreds+ten+uint))/1000)

        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L',
                 100: 'C', 500: 'D', 1000: 'M', 5000: 'G'}
        new = ""

        if thousands <= 3:
            new += (roman[1000]*thousands)
        elif thousands == 4:
            new += (roman[1000]+roman[5000])
        elif 5 <= thousands <= 8:
            new += (roman[5000]+roman[1000]*(thousands-5))
        elif thousands == 9:
            new += (roman[1000]+roman[10000])

        if hundreds <= 3:
            new += (roman[100]*hundreds)
        elif hundreds == 4:
            new += (roman[100]+roman[500])
        elif 5 <= hundreds <= 8:
            new += (roman[500]+roman[100]*(hundreds-5))
        elif hundreds == 9:
            new += (roman[100]+roman[1000])

        if ten <= 3:
            new += (roman[10]*ten)
        elif ten == 4:
            new += (roman[10]+roman[50])
        elif 5 <= ten <= 8:
            new += (roman[50]+roman[10]*(ten-5))
        elif ten == 9:
            new += (roman[10]+roman[100])

        if uint <= 3:
            new += (roman[1]*uint)
        elif uint == 4:
            new += (roman[1]+roman[5])
        elif 5 <= uint <= 8:
            new += (roman[5]+roman[1]*(uint-5))
        elif uint == 9:
            new += (roman[1]+roman[10])

        return new

    def romanToDeci(self, s):
        Deci = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000, 'G': 5000}
        i = 0
        num = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in Deci:
                num += Deci[s[i:i+2]]
                i += 2
            else:
                num += Deci[s[i]]
                i += 1
        return num


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))
