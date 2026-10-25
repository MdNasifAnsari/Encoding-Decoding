from random import randint as rd
def encoding():

    text = input("Enter your text: ")

    alphanums = list("qwertyuiopasdfghjklzxcvbnm1234567890")

    special = [
         ")", "~", "!", "@", "#", "$", "%", "^", "&", "*",
        "(", "`", "-", "_", "=", "+", "[", "]", "{", "}",
        "\\", "|", ";", ":", "'", '"', ",", "<", ".", ">",
        "/", "?", " "
    ]

    a1 = rd(0, len(alphanums) - 1)
    b1 = rd(0, len(alphanums) - 1)
    c1 = rd(0, len(alphanums) - 1)

    a2 = rd(0, len(alphanums) - 1)
    b2 = rd(0, len(alphanums) - 1)
    c2 = rd(0, len(alphanums) - 1)

    d = [alphanums[a1], alphanums[b1], alphanums[c1]]
    e = [alphanums[a2], alphanums[b2], alphanums[c2]]

    lst = list(text.lower())
    lst.reverse()

    fin_lst = []
    fin_lst.extend(d)

    for i in lst:
        if i in alphanums:
            index = alphanums.index(i)
            fin_lst.append(alphanums[(index + 1) % len(alphanums)])
        elif i in special:
            index = special.index(i)
            fin_lst.append(special[(index + 1) % len(special)])
        else:
            fin_lst.append(i)

    fin_lst.extend(e)

    result = "".join(fin_lst)

    print("---Encoded text:", result)
