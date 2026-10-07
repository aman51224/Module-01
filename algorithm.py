def getOnlyEvens(array):
    evens = []
    for index in range(len(array)):
        if index % 2 == 0 and array[index] % 2 == 0:
            evens.append(array[index])
    print(evens)
    

getOnlyEvens([1, 2, 3, 6, 4, 8])
getOnlyEvens([0, 1, 2, 3, 4])


# Question 2
# ● Create a function that takes a two-digit number as an parameter and prints "Ok" inthe console if the given string is greater than its reversed digit version. If not, the function will print "Not ok"
#      ○ Test 1: reverseCompare(72) prints "ok" because 72 > 27
#      ○ reverseCompare(23) prints "Not ok", because 23 is not greater than 32

def reverseCompare(number):
    number_string = str(number)
    if number_string[0] > number_string[1]:
        print("Ok")
    else:
        print("Not ok")

reverseCompare(72)
reverseCompare(23)




def returnFactorial(number):
    if number <= 1:
        return 1

    return number * returnFactorial(number - 1)

print(returnFactorial(5))
print(returnFactorial(6))
print(returnFactorial(0))






def checkMeera(array):
    array_size = len(array)
    is_not_meera_array = False
    for i in range(array_size):
        for j in range(array_size):
            if i == j:
                continue
            if array[i] == (array[j] * 2):
                print("I am NOT a Meera array")
                is_not_meera_array = True
                break
            j += 1
        if is_not_meera_array == True:
            break
        i += 1
    if is_not_meera_array == False:
        print("I am a Meera array")


checkMeera([10, 4, 0, 5])
checkMeera([7, 4, 9])
checkMeera([1, -6, 4, -3])
                

def isDual(array):
    array_size = len(array)
    visited = {}
    for i in range(array_size):
        if array[i] not in visited:
            visited[array[i]] = 1
        else:
            visited[array[i]] = visited[array[i]] + 1

    for count in visited.values():
        if count != 2:
            return 0
    return 1

print(isDual([1, 2, 1, 3, 3, 2]))
print(isDual([2, 5, 2, 5, 5]))
print(isDual([3, 1, 1, 2, 2]))




# Question 6
# ● Write a function that takes the number of seconds and returns the digital format clock time as a string. Time should be counted from 00:00:00.
#       ○ Examples: digitalClock(5025) as "01:23:45" 5025 seconds is 1 hour, 23 mins, 45secs.
#       ■ digitalClock(61201) as "17:00:01" No AM/PM. 24h format.
#       ■ digitalClock(87000) as "00:10:00" It's 00:10 next day.


# def digitalClock(seconds):
#     time_in_hours = (seconds // 3600) % 24
#     time_in_minutes = (seconds // 60) % 60
#     time_in_seconds = seconds % 60

#     if time_in_hours < 10:
#         time_in_hours = "0" + str(time_in_hours)

#     if time_in_minutes < 10:
#         time_in_minutes = "0" + str(time_in_minutes)

#     if time_in_seconds < 10:
#         time_in_seconds = "0" + str(time_in_seconds)
    
#     return str(time_in_hours) + ":" + str(time_in_minutes) + ":" + str(time_in_seconds)

    

def digitalClock(seconds):
    time_in_hours = (seconds // 3600) % 24
    remainder = seconds % 3600

    time_in_minutes = (remainder // 60)
    time_in_seconds = remainder % 60

    hours_string = str(time_in_hours)
    minutes_string = str(time_in_minutes)
    seconds_string = str(time_in_seconds)

    if time_in_hours < 10:
        hours_string = "0" + hours_string
    
    if time_in_minutes < 10:
        minutes_string = "0" + minutes_string

    if time_in_seconds < 10:
        seconds_string = "0" + seconds_string
    
    return f"{hours_string}:{minutes_string}:{seconds_string}"




print(digitalClock(5025))
print(digitalClock(61201))
print(digitalClock(87000))


