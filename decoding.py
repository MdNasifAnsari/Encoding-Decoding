def decoding():
    text = input("Enter encoded text: ")

    alphanums = list("qwertyuiopasdfghjklzxcvbnm1234567890")

    special = [
        ")", "~", "!", "@", "#", "$", "%", "^", "&", "*",
        "(", "`", "-", "_", "=", "+", "[", "]", "{", "}",
        "\\", "|", ";", ":", "'", '"', ",", "<", ".", ">",
        "/", "?", " "
    ]

    if len(text) < 6:
        print("Invalid encoded text: too short.")
        return

    lst = list(text.lower()[3:-3])

    fin_lst = []

    for char in lst:
        if char in alphanums:
            index = alphanums.index(char)
            fin_lst.append(
                alphanums[(index - 1) % len(alphanums)]
            )

        elif char in special:
            index = special.index(char)
            fin_lst.append(
                special[(index - 1) % len(special)]
            )

        else:
            fin_lst.append(char)

    fin_lst.reverse()

    result = "".join(fin_lst)
    print("---Decoded text:", result)
