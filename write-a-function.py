def is_leap(year):
    leap = False

    if 1900 <= year <= 10 ** 5:
        leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

    return leap


year = int(input())
print(is_leap(year))
