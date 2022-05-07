# this code is a time calculator that converts the number of seconds entered to mins hours or days.
number_of_seconds = int(input("Enter number of seconds \n"))
msg = ""

if number_of_seconds < 0:
    msg = "Enter a number above 0. \n" +      "Rerun program and try again."

else:
    if number_of_seconds >= 0 and number_of_seconds < 60:
        secs = format(number_of_seconds % 60)
        msg = "Seconds = " + secs
    elif number_of_seconds >= 60 and number_of_seconds < 3600:
        mins = format(number_of_seconds // 60)
        secs =format(number_of_seconds % 60)
        msg = "Minutes = " + mins + "\n Seconds = " + secs
    
    elif number_of_seconds >= 3600 and number_of_seconds < 86400:
        hours = format(number_of_seconds // 3600)
        mins =format((number_of_seconds % 3600) // 60)
        secs = format((number_of_seconds % 3600) % 60)
        msg = "Hours = " + hours +  "\n Minutes = " + mins + "\n Seconds = " + secs
    
    elif number_of_seconds >= 86400:
        days = format(number_of_seconds // 86400)
        hours =format((number_of_seconds % 86400) // 3600)
        mins =format(((number_of_seconds % 86400) % 3600) // 60)
        secs =format(((number_of_seconds % 86400) % 3600) & 60)
        msg = "Days = " + days + "\n Hours = " + hours +  "\n Minutes = " + mins + "\n Seconds = " + secs
    
print(msg)
    
