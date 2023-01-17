# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def encode(user):
    result = ""
    preChar = ''
    count = 1
    for index, elem in enumerate(user):
        if index == 0:
            preChar = elem
            continue

        if preChar == elem:
            count += 1
            if index == len(user)-1:
                result += f"{count}{preChar}"
        else:
            if index != len(user)-1:
                result += f"{count}{preChar}"
                count = 1
            else:
                result += f"{count}{preChar}1{elem}"

        if count >= 10:
            result += f"9{preChar}"
            count -= 9

        preChar = elem
    return result

def decode(user):
    result = ""
    user = list(user)
    amounts = []
    chars = []
    for elem in user[::2]:
        if elem != None:
            amounts.append(elem)
    for elem in user[1::2]:
        if elem != None:
            chars.append(elem)
    for index, amount in enumerate(amounts):
        for i in range(int(amount)):
            result += chars[index]
    
    return result

if __name__ == "__main__":
    print(decode("519242233415"))
    print(encode("111112222334445"))


