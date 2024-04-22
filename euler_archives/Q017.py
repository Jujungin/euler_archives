number_dict = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

def change_number_word(n):
    if n <= 20:
        return number_dict[n]
    elif n < 100:
        return number_dict[n - n % 10] + ('-' + number_dict[n % 10] if n % 10 != 0 else '')
    elif n < 1000:
        return number_dict[n // 100] + ' hundred' + (' and ' + change_number_word(n % 100) if n % 100 != 0 else '')
    elif n == 1000:
        return 'one thousand'
    else:
        return "Error: out of range"

def number_letter_counts(start, end):
    count = 0
    for i in range(start, end + 1):
        count += len(change_number_word(i).replace(" ","").replace("-",""))
    return count
    

start_require = 25
end_require = 25
print(change_number_word(start_require).replace(" ","").replace("-",""))

result = number_letter_counts(start_require, end_require)
print(f"count : {result}")
