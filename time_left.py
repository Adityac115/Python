def time_left(seconds):
    hours = seconds // 3600 
    minutes = (seconds - hours*3600 ) //60
    seconds = seconds - hours*3600 - minutes * 60
    return hours, minutes, seconds

seconds = int(input("Enter seconds: "))
hours,minutes,seconds = time_left(seconds)
print("hours:",hours,"minutes:",minutes,"seconds:",seconds)