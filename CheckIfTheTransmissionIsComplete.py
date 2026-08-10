import string

def check_if_complete_transmission(transmission):
    """
    :type transmission: str
    :rtype: bool
    """
    alphabet = string.ascii_lowercase 
    freqMap = {}
    for item in transmission:
        freqMap[item] = freqMap.get(item, 0) + 1
    for letter in alphabet:
        if freqMap.get(letter) == None:
            return False
    return True

transmission1 = "thequickbrownfoxjumpsoverthelazydog"
transmission2 = "spacetravel"

print(check_if_complete_transmission(transmission1))
print(check_if_complete_transmission(transmission2))