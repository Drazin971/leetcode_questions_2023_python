class Solution:
  def intToRoman(self, num: int) -> str:
    roman_numerals = {
      1:'I',
      5:'V',
      10:'X',
      50:'L',
      100:'C',
      500:'D',
      1000:'M'
    }
    roman_number = ""
    decimal_place = 1
    while num>0:
      decimal_number = num % 10 
      num = num //10
      if decimal_number==4:
        roman_number = roman_numerals[1*decimal_place] +roman_numerals[5*decimal_place] + roman_number
      elif decimal_number==9:
        roman_number = roman_numerals[1*decimal_place] +roman_numerals[10*decimal_place] + roman_number
      elif decimal_number<4:
        roman_number = roman_numerals[1*decimal_place]*decimal_number + roman_number
      elif decimal_number<9:
        roman_number = roman_numerals[5*decimal_place]+roman_numerals[1*decimal_place]*(decimal_number-5) + roman_number
        
      decimal_place *= 10 
      #print(decimal_number, roman_number)
    return roman_number