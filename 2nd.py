def AngleCheaker(h,m):
        if (h < 0 or m < 0 or h > 12 or m > 60):
            print('Wrong input')
         
        if (h == 12):
            h = 0
        if (m == 60):
            m = 0
            h += 1
            if(h>12):
                   h = h-12
        hour = 0.5 * (h * 60 + m)
        minute = 6 * m
        angle = int(abs(hour - minute))
        angle = min(360 - angle, angle)
        if angle == 90:
          print('90 deg are formed',h,':',m)
        else:
          print('90 deg are not formed')  


h = int(input("Enter the hour (eg: 4)"))
m = int((input("Enter the mint (eg: 20)")))

AngleCheaker(h,m)