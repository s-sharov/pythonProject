

def rle(in_text):
    if in_text == "":
        return "Неккоректный формат"
    result = list()
    last_sym = in_text[0]
    count = 0
    for sym in (list(in_text) + [None]):
        if sym != last_sym:
            if count == 1:
                result.append(last_sym)
            else:
                result.append(f'{last_sym}{str(count)}')
            count = 1
            last_sym = sym
        else:
            count += 1
    return "".join(result)


input_text = str(input("Введите текст: ")).upper()
print(input_text)

print(rle(input_text))
