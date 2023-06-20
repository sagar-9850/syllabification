import eng_to_ipa as pa
def count_syl(word):
    delim = "ˈ"
    vowels = ['æ','ɛ','ɪ','ʊ','i','ə','ɑ','u','a','e']
    diphthongs=  ['aʊ','aɪ','ɔɪ','oʊ','eɪ']
    phon = pa.convert(word)
    count=0
    for j in vowels:
        if j in phon:
            count +=phon.count(j)
    for k in diphthongs:
        if k in phon:
            count -=phon.count(k)
    return count



def phone(word):
    phon = pa.convert(word)
    return phon