#!/usr/bin/env python
# -- encoding: utf8 --
# Prints names for any numbers given in the command line.
# For details on the large numbers, see:
# http://www.isthe.com/chongo/tech/math/number/howhigh.html

# Copyright © 2010  Eric Wald
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

def latin_cardinal(n):
    r'''Collects the Latin cardinal prefix for the number.
        Only works for numbers less than a thousand, so far.
        
        >>> print latin_cardinal(1)
        million
        >>> print latin_cardinal(2)
        billion
        >>> print latin_cardinal(14)
        quattuordecillion
        >>> print latin_cardinal(27)
        septenvigintillion
        >>> print latin_cardinal(68)
        octosexagintillion
        >>> print latin_cardinal(100)
        centillion
        >>> print latin_cardinal(108)
        cenoctotillion
        >>> print latin_cardinal(253)
        ducentrequinquagintillion
        >>> print latin_cardinal(1000)
        milliatillion
        >>> print latin_cardinal(1234)
        milliaducenquattuortrigintillion
        >>> print latin_cardinal(2000)
        domilliatillion
        >>> print latin_cardinal(12345)
        dodecmilliatrecenquinquadragintillion
        >>> print latin_cardinal(987067)
        nongenseptenoctoginmilliaseptensexagintillion
        >>> print latin_cardinal(1000000)
        milliamilliatillion
        >>> print latin_cardinal(1001000)
        milliamilliaunmilliatillion
        >>> print latin_cardinal(987000000067)
        nongenseptenoctoginmilliamilliamilliaseptensexagintillion
        >>> print latin_cardinal(232092170119936)
        ducendotriginmilliamilliamilliamilliadononaginmilliamilliamilliacenseptuaginmilliamilliacennovemdecmillianongensextrigintillion
    '''#"""#'''
    
    simple = ["thousand", "mi", "bi", "tri", "quadri", "quinti", "sexti", "septi", "octi", "noni"]
    units = ["", "un", "do", "tre", "quattuor", "quin", "sex", "septen", "octo", "novem"]
    tens = ["", "dec", "vigin", "trigin", "quadragin", "quinquagin", "sexagin", "septuagin", "octogin", "nonagin"]
    hundreds = ["", "cen", "ducen", "trecen", "quadringen", "quingen", "sescen", "septingen", "octingen", "nongen"]
    
    suffixes = {
        "i": "llion",
        "c": "illion",
        "a": "tillion",
        "e": "tillion",
        "m": "tillion",
        "n": "tillion",
        "o": "tillion",
        "r": "tillion",
        "x": "tillion",
        "d": "",
    }
    
    results = []
    if n < 10:
        results.append(simple[n])
    else:
        thousands = 0
        while n:
            n, unit = divmod(n, 10)
            n, ten = divmod(n, 10)
            n, hun = divmod(n, 10)
            if hun or ten or unit:
                results.extend(["millia"] * thousands)
            if n or (hun, ten, unit) != (0, 0, 1):
                results.extend(filter(None, [tens[ten], units[unit], hundreds[hun]]))
            thousands += 1
    results.insert(0, suffixes[results[0][-1]])
    return str.join("", reversed(results))

def nn1000(number):
    # Tables
    names = {
        0: None,
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'forteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
    }
    
    hundreds = tens = None
    if number >= 100:
        h, number = divmod(number, 100)
        hundreds = names[h] + ' hundred'
    if number >= 20:
        tens = names[number - (number % 10)]
        number %= 10
    result = names[number]
    if tens: result = result and (tens + '-' + result) or tens
    if hundreds: result = result and (hundreds + ' ' + result) or hundreds
    return result

def num2name(number):
    r'''Converts an integer into an English phrase.
        >>> print num2name(2000)
        two thousand
        >>> print num2name(1900)
        one thousand, nine hundred
        >>> print num2name(816)
        eight hundred sixteen
        >>> print num2name(1)
        one
        >>> print num2name(42)
        forty-two
        >>> print num2name(987654321)
        nine hundred eighty-seven million, six hundred fifty-four thousand, three hundred twenty-one
        >>> print num2name(123456789246801357)
        one hundred twenty-three quadrillion, four hundred fifty-six trillion, seven hundred eighty-nine billion, two hundred forty-six million, eight hundred one thousand, three hundred fifty-seven
        >>> print num2name(123456789246801357000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        one hundred twenty-three doseptuagintillion, four hundred fifty-six unseptuagintillion, seven hundred eighty-nine septuagintillion, two hundred forty-six novemsexagintillion, eight hundred one octosexagintillion, three hundred fifty-seven septensexagintillion
        >>> print num2name(1000**15)
        one quattuordecillion
        >>> print num2name(1000**1001)
        one milliatillion
        >>> print num2name(1000**1002)
        one milliauntillion
        >>> print num2name(357 * 1000**2068)
        three hundred fifty-seven domilliaseptensexagintillion
        
        # These take an extremely long time to complete.
        >>> print num2name(357 * 1000**987068)
        three hundred fifty-seven nongenseptenoctoginmilliaseptensexagintillion
        >>> print num2name(357 * 1000**987000000068)
        three hundred fifty-seven nongenseptenoctoginmilliamilliamilliaseptensexagintillion
        >>> print num2name(1000**232092170119937)
        one ducendotriginmilliamilliamilliamilliadononaginmilliamilliamilliacenseptuagin milliamilliacennovemdecmillianongensextrigintillion
    '''#'''
    negative = number < 0
    if negative:
        number = -number
    if not number:
        return 'zero'
    
    groups = []
    thousands = 0
    while number:
        number, n = divmod(number, 1000)
        if n:
            name = nn1000(n)
            if thousands:
                name += " " + latin_cardinal(thousands - 1)
            groups.insert(0, name)
        thousands += 1
    result = str.join(", ", groups)
    
    if negative:
        result = "negative " + result
    return result

def _test():
    import doctest
    doctest.testmod()

def run():
    import sys
    if len(sys.argv) > 1:
        for num in sys.argv[1:]:
            print num2name(int(num))
    else:
        n = 0
        while True:
            print num2name(n)
            n += 1

if __name__ == "__main__":
    run()
