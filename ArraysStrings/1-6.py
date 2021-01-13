"""
String Compression: Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should 
return the original string. You can assume the string has only uppercase and lowercase 
letters (a - z).
"""

def StringCompress(string):
    compString = ""
    i, count = 0, 0
    while i < len(string):
        count += 1
        if i + 1 >= len(string) or string[i] != string[i+1]:
            compString += string[i] + str(count)
            count = 0
        i += 1
    if compString > string:
        return string
    else:
        return compString

# test
print(StringCompress("aabcccccaaa"))
