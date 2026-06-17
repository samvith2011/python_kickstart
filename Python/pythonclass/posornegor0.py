'''
Algorithm:
1.Create function with the number as a paramenter
2. Create if statements to check if number is positive or negartive or zero
3. Print results



'''

def check_number(n):
    if n < 0:
        return "negative"
    elif n > 0:
        return "positive"
    elif n == 0:
        return "zero"

print(check_number(-12))
