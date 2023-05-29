class SerbianScriptConverter:

    CHR_DICT = {'A': 'А', 'a': 'а', 'B': 'Б', 'b': 'б', 'C': 'Ц', 'c': 'ц', 'D': 'Д', 'd': 'д', 'E': 'Е', 'e': 'е',
                'F': 'Ф', 'f': 'ф', 'G': 'Г', 'g': 'г', 'H': 'Х', 'h': 'х', 'I': 'И', 'i': 'и', 'J': 'Ј', 'j': 'ј',
                'K': 'К', 'k': 'к', 'L': 'Л', 'l': 'л', 'M': 'М', 'm': 'м', 'N': 'Н', 'n': 'н', 'O': 'О', 'o': 'о',
                'P': 'П', 'p': 'п', 'R': 'Р', 'r': 'р', 'S': 'С', 's': 'с', 'T': 'т', 't': 'т', 'U': 'У', 'u': 'у',
                'V': 'В', 'v': 'в', 'Z': 'З', 'z': 'з', 'Š': 'Ш', 'š': 'ш', 'Đ': 'Ђ', 'đ': 'ђ', 'Č': 'Ч', 'č': 'ч',
                'Ć': 'Ћ', 'ć': 'ћ', "Ž": "Ж", "ž": "ж"}
    SPECIAL_CHR_DICT = {'Nj': 'Њ', 'nj': 'њ', 'Lj': 'Љ', 'lj': 'љ', 'Dž': 'Џ', 'dž': 'џ'}

    def __init__(self, input_str):
        self.input_str = input_str

    def lat_to_cyr(self):
        converted_text= []
        input_str = self.input_str + " "
        i = 0
        while i < len(self.input_str):
            if input_str[i] + input_str[i + 1] in self.SPECIAL_CHR_DICT:
                converted_text.append(self.SPECIAL_CHR_DICT[input_str[i] + input_str[i + 1]])
                i += 2
            elif input_str[i] in self.CHR_DICT:
                converted_text.append(self.CHR_DICT[input_str[i]])
                i += 1
            else:
                converted_text.append(input_str[i])
                i += 1
        return ''.join(converted_text)

    def cyr_to_lat(self):
        new_dict = {**self.CHR_DICT, **self.SPECIAL_CHR_DICT}
        new_dict = {v: k for k, v in new_dict.items()}
        converted_text = ''.join(map(lambda x: new_dict.get(x, x), self.input_str))
        return converted_text

    @property
    def convert_script(self):
        if any(char in self.CHR_DICT.values() for char in self.input_str):
            return self.cyr_to_lat()
        else:
            return self.lat_to_cyr()



str_lat = "Odredbe ovog zakona primenjuju se na zaposlene strane državljane i lica bez državljanstva koji rade kod poslodavca na teritoriji Republike Srbije, ako zakonom"
str_cyr = "Одредбе овог закона примењују се на запослене који раде на територији Републике. Србије, код домаћег или страног правног, односно физичког лица "

print(SerbianScriptConverter(str_cyr).convert_script)