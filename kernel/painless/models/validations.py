import re
import string
from django import forms

def validate_charachters(value):
    letters = set(string.punctuation)
    digits = set(string.digits)
    v = set(value)
    if not v.isdisjoint(letters) or not v.isdisjoint(digits):
        raise forms.ValidationError('نام تنها باید از کاراکتر تشکیل شده باشد.')

def validate_phone_number(value):
    pattern = r'^(09)[1-3][0-9]\d{7}$'
    if not re.match(pattern, value):
        raise forms.ValidationError('شماره صحیح وارد نشده است.')

def validate_national_code(value):
    if not len(value) == 10:
        raise forms.ValidationError('کد ملی معتبر نیست')
    positions = [i for i in range(1, 11)]
    code = value
    codes = [int(num) for num in code]
    # control number created by some operations on first 9 numbers of code
    control_number = codes[9]
    total = 0
    for i in range(10):
        row = codes[i] * positions[i]
        total += row
    
    extant = total % 11

    if not extant < 2 and not extant == control_number:
        raise forms.ValidationError('کد ملی معتبر نیست')
    elif extant >= 2:
        extant = 11 - extant
        if not extant == control_number:
            raise forms.ValidationError('کد ملی معتبر نیست')

def validate_postal_code(value):
    if not len(value) == 10:
        raise forms.ValidationError('کد پستی صحیح نیست')
    elif '2' in value or '0' in value:
        raise forms.ValidationError('کد پستی صحیح نیست')
    elif value[4] == 5:
        raise forms.ValidationError('کد پستی صحیح نیست')
    elif len(set(value)) == 1:
        raise forms.ValidationError('کد پستی صحیح نیست')
    else:
        pass
    
def validate_plaque(value):
    if not len(value) == 8:
        raise forms.ValidationError('پلاک معتبر نیست')

    # import pdb; pdb.set_trace()
    
    pattern = r'^[1-9]{2}\w[1-9]{3}[1-9]{2}$'
    if not re.match(pattern, value):
        raise forms.ValidationError('پلاک معتبر نیست.')
    
    states = ['الف', 'پ', 'ت', 'ث', 'ز', 'ژ', 'ش', 'ک', 'ف', 'گ']
    letters = string.ascii_letters

    for state in states:
        if state in value:
            raise forms.ValidationError('پلاک معتبر نیست.')
    
    for letter in letters:
        if letter in value:
            raise forms.ValidationError('پلاک معتبر نیست.')
        
def validate_bank_names(value):
    bank_names = [
        #government
        'ملی',
        'سپه',
        'صنعت و معدن',
        'کشاورزی',
        'مسکن',
        'توسعه صادرات',
        'توسعه تعاون',
        'پست بانک ایران',
        # non-goverment
        'اقتصاد نوین',
        'پارسیان',
        'کارآفرین',
        'سامان',
        'سینا',
        'خاورمیانه',
        'شهر',
        'دی',
        'صادرات',
        'ملت',
        'تجارت',
        'رفاه',
        'حکمت ایرانیان',
        'گردشگری',
        'قوامین',
        'انصار',
        'ایران زمین',
        'سرمایه',
        'پاسارگاد',
        # gharzol hasane
        'قرض الحسنه مهر',
        'قرض الحسنه رسالت',
    ]
    if not value in bank_names:
        raise forms.ValidationError('نام بانک معتبر نیست')

def validate_bank_iban(value):
    if not len(value) == 26:
        raise forms.ValidationError('شماره شبا معتبر نیست')
    code = list(value)
    ir_code = code[0:4]
    main_code = code[4:]
    new_code = list(main_code + ir_code)

    code_dictionary = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 18,
        "J": 19,
        "K": 20,
        "L": 21,
        "M": 22,
        "N": 23,
        "O": 24,
        "P": 25,
        "Q": 26,
        "R": 27,
        "S": 28,
        "T": 29,
        "U": 30,
        "V": 31,
        "W": 32,
        "X": 33,
        "Y": 34,
        "Z": 35,
    }

    for key, value in code_dictionary.items():
        if new_code[22] == key:
            new_code[22] = str(value)
        if new_code[23] == key:
            new_code[23] = str(value)
    result = "".join(new_code)
    if not len(result) == 28:
        raise forms.ValidationError('Error: call to company.')

    if not int(result) % 97 == 1:
        raise forms.ValidationError('شماره شبا معتبر نیست ')

def validate_bank_card(value):
    if not len(value) == 16:
        raise forms.ValidationError('شماره کارت معتبر نیست')
    # import pdb; pdb.set_trace()
    value = [int(val) for val in value]
    temp_codes = [val * 2 if index % 2 == 0 else val * 1 for index, val in enumerate(value)]
    codes = [x - 9 if x > 9 else x for x in temp_codes]
    result = sum(codes)
    if not result % 10 == 0:
        raise forms.ValidationError('شماره کارت معتبر نیست')

class FileUploadValidator:
    def __init__(self, exclude = False, *args, **kwargs):
        self.exlude = exclude

    def __file_extention_validation(self, file_path, ext_list):
        """file extension validation support.
        
        Arguments:
            file_path {[str]} -- [file path with extention]
            ext_list {[list]} -- [support or unsupport extension list]
        
        Keyword Arguments:
            exclude {bool} -- [if exclude set to True does not support ext_list else support ext_list] (default: {False})
        
        """

        ext = '.' + file_path.split('.')[-1]

        if self.exclude:
            if ext in ext_list:
                raise ValidationError(u'File not supported.')
        else:
            if not ext in ext_list:
                raise ValidationError(u'File not supported.')

    def let_movie(self, value):
        self.__file_extention_validation(value, ['.mov', '.mp4', '.wmv', '.avi'])
    
    def let_pic(self, value):
        self.__file_extention_validation(value, ['.jpg', '.png', '.gif'])
    
    def let_svg(self, value):
        self.__file_extention_validation(value, ['.svg'])


