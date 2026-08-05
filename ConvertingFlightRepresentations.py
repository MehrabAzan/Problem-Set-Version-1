def get_adj_dict(flights):
    dictionary = {}
    for origin, dest in flights:
        if origin not in dictionary:
            dictionary[origin] = [dest]
        else:
            dictionary[origin].append(dest)
    return dictionary[origin]

flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))