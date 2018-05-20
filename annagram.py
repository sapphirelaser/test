def check_anagram(string1,string2):
    if len(string1) == len(string2):
        annagram1 = True
        annagram2 = True
        for s1 in string1:
            t = string2.find(s1)
            if t==-1:
                annagram1 = False
                break
        for s2 in string2:
            t = string1.find(s2)
            if t==-1:
                annagram2 = False
                break
        if annagram1 and annagram2:
            annagram = True
        else:
            annagram = False
    else:
        annagram = False
    return annagram


temp = check_anagram("helll","hello")

print(temp)
