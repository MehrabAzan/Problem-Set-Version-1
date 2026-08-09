def get_winner(votes):
    freqMap = {}
    for item in votes:
        freqMap[item] = freqMap.get(item, 0) + 1
    return max(freqMap, key=freqMap.get)

votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

print(get_winner(votes1))
print(get_winner(votes2))