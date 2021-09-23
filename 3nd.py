from math import floor

def inputField(reset,current):
        cal =  floor((current - reset)*100/100)
        cal = cal*10
        cal = float(current - (cal/100))
        return cal
print('Current time should be 10 mint increase every hour')
r = float(input("Enter the Reset Time: (eg:- 14.00 ) "))
c = float(input("Enter the Current Time:(eg:- 16.20) "))

print("Actual Time ", inputField(r,c))