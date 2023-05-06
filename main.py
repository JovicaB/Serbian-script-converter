class SerbianScriptConverter:

    CHR_DICT = {'A': 'А', 'a': 'а', 'B': 'Б', 'b': 'б', 'C': 'Ц', 'c': 'ц', 'D': 'Д', 'd': 'д', 'E': 'Е', 'e': 'е',
                'F': 'Ф', 'f': 'ф', 'G': 'Г', 'g': 'г', 'H': 'Х', 'h': 'х', 'I': 'И', 'i': 'и', 'J': 'Ј', 'j': 'ј',
                'K': 'К', 'k': 'к', 'L': 'Л', 'l': 'л', 'M': 'М', 'm': 'м', 'N': 'Н', 'n': 'н', 'O': 'О', 'o': 'о',
                'P': 'П', 'p': 'п', 'R': 'Р', 'r': 'р', 'S': 'С', 's': 'с', 'T': 'т', 't': 'т', 'U': 'У', 'u': 'у',
                'V': 'В', 'v': 'в', 'Z': 'З', 'z': 'з', 'Š': 'Ш', 'š': 'ш', 'Đ': 'Ђ', 'đ': 'ђ', 'Č': 'Ч', 'č': 'ч',
                'Ć': 'Ћ', 'ć': 'ћ', ' ': ' '}
    SPECIAL_CHR_DICT = {'Nj': 'Њ', 'nj': 'њ', 'Lj': 'Љ', 'lj': 'љ', 'Dž': 'Џ', 'dž': 'џ'}

    def __init__(self, input_str):
        self.input_str = input_str

    def lat_cyr(self):
        final_text = []
        input_str = self.input_str + " "
        i = 0
        while i < len(self.input_str):
            if input_str[i] + input_str[i + 1] in SerbianScriptConverter.SPECIAL_CHR_DICT:
                final_text.append(SerbianScriptConverter.SPECIAL_CHR_DICT[input_str[i] + input_str[i + 1]])
                i += 2
            elif input_str[i] in SerbianScriptConverter.CHR_DICT:
                final_text.append(SerbianScriptConverter.CHR_DICT[input_str[i]])
                i += 1
            else:
                final_text.append(input_str[i])
                i += 1
        return ''.join(final_text)

    def cyr_lat(self):
        new_dict = {**SerbianScriptConverter.CHR_DICT, **SerbianScriptConverter.SPECIAL_CHR_DICT}
        new_dict = {v: k for k, v in new_dict.items()}
        final_text = ''.join(map(lambda x: new_dict.get(x, x), self.input_str))
        return final_text

    @property
    def convert_script(self):
        if any(i in SerbianScriptConverter.CHR_DICT.values() for i in self.input_str):
            return self.cyr_lat()
        else:
            return self.lat_cyr()
