class IntegerToString:
    def numberBelowThousand(self, num):
        d = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten',
             11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen',
             19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Fourty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninty',
             }

        if not num:
            return ''
        elif num in d:
            return d[num]
        elif num <=99:
            return ' '.join(d[num-num%10], d[num%10])
        else:
            hundred = d[int(num/100)]
            if not num%100:
                return ' '.join(d[hundred], "Hundred")
    def convertNums(self, num):
        flag = 0
        d = {0:'', 1:' Thousand', 2:' Million', 3:' Billion'}
        res = []
        if not num:
            return 'Zero'
        while num > 0:
            if num%1000 == 0:
                flag += 1
                num = int(num/1000)
                continue
            part1 = self.numberBelowThousand(num%1000)
            part2 = d[flag]
            res.append(part1+part2)
            num = num//1000
            flag += 1
        return ' '.join(res[::-1])