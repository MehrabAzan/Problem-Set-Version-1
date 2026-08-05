def get_direct_flights(flights, source):
    temp = flights[source]
    result = []
    if source > len(flights) - 1:
        return []
    for i in range(len(temp)):
        if temp[i] == 1:
            result.append(i)
    return result

flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))