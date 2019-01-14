
testphrase = "I want you to remove every vowel from this sentence."


def devowel(phrase) -> str:
    table = str.maketrans(dict.fromkeys('aeiouAEIOU'))
    phrase = phrase.translate(table)
    return phrase

print(devowel(testphrase))