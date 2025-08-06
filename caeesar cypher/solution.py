

def caesar_cypher_encrypt(s, key):
    input_string_list = list(s)
    ans = []
    for i in range(len(input_string_list)):
        if not input_string_list[i].isalpha():
            ans.append(input_string_list[i])
            continue

        if ord(input_string_list[i])<97:
        
            if ord(input_string_list[i]) + key > ord("Z"):
                val = chr(ord(input_string_list[i]) - (26 - key))
            else:
                val = chr(ord(input_string_list[i]) + key)
        else:

            if ord(input_string_list[i]) + key > ord("z"):
                val = chr(ord(input_string_list[i]) - (26 - key))
            else:
                val = chr(ord(input_string_list[i]) + key)

        ans.append(val)
    res = "".join(ans)
    return res


def caesar_cypher_decrypt(s, key):
    input_string_list = list(s)
    ans = []
    for i in range(len(input_string_list)):
        if not input_string_list[i].isalpha():
            ans.append(input_string_list[i])
            continue


        if ord(input_string_list[i])<97:
            if ord(input_string_list[i]) - key < ord("A"):
                val = chr(ord(input_string_list[i]) + (26 - key))
            else:
                val = chr(ord(input_string_list[i]) - key)
        else:
            if ord(input_string_list[i]) - key < ord("a"):
                val = chr(ord(input_string_list[i]) + (26 - key))
            else:
                val = chr(ord(input_string_list[i]) - key)

        ans.append(val)
    res = "".join(ans)
    return res