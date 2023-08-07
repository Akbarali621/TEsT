from uzwords import words
from difflib import get_close_matches
from transliterate import to_cyrillic,to_latin
# print(get_close_matches('тарих',words))
def checkWord(word,words=words):
    word=word.lower()
    word=to_cyrillic(word)
    matches=set(get_close_matches(word,words))
    available=False

    if word in matches:
        available=True
        matches=word
    elif 'ҳ' in word:
        word=word.replace('ҳ','х')
        matches.update(get_close_matches(word,words))


    elif 'х' in word:
        word = word.replace('х','ҳ')
        matches.update(get_close_matches(word,words))

    return {'available':available,'matches':matches}
if __name__=='__main__':
    print(checkWord("Хато"))
    print(checkWord("тарих"))
    print(checkWord("олм"))