class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        year_code = ((year%100) + (year%100)//4)%7
        month_codes = "033614625035"
        month_code = int(month_codes[month-1])
        if year // 100 >= 20:
            century_code = 6
        else:
            century_code = 0
        if year%400 == 0 or year%4 == 0:
            if month == 1 or month == 2:

                leap_year_code = 1
            else:
                leap_year_code = 0
        else:
            leap_year_code = 0
        result = (year_code + month_code + century_code + day - leap_year_code)%7
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return days[result]


day = 31
month = 8
year = 2019
day = 18
month = 7
year = 1999
day = 15
month = 8
year = 1993
day = 29
month = 2
year = 2016
print(Solution().dayOfTheWeek(day, month, year))