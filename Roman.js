function convertToRoman(num) {
  const arr = [];
  while (num > 0) {
    if (num >= 1000) {
     arr.push('M');
     num -= 1000;
    }
    else if (num < 1000 && num > 899) {
      arr.push('CM');
      num -= 900;
    }
    else if (num < 900 && num > 499) {
      arr.push('D');
      num -= 500;
    }
    else if (num < 500 && num > 399) {
      arr.push('CD');
      num -= 400;
    }
    else if (num < 400 && num > 99) {
      arr.push('C');
      num -= 100;
    }
    else if (num < 100 && num > 89) {
      arr.push('XC');
      num -= 90;
    }
    else if (num < 90 && num > 49) {
      arr.push('L');
      num -= 50;
    }
    else if (num < 50 && num > 39) {
      arr.push('XL');
      num -= 40;
    }
    else if (num < 40 && num > 9) {
      arr.push('X');
      num -= 10;
    }
    else if (num < 10 && num > 8) {
      arr.push('IX');
      num -= 9;
    }
    else if (num < 10 && num > 4) {
      arr.push('V');
      num -= 5;
    }
    else if (num < 5 && num > 3) {
      arr.push('IV');
      num -= 4;
    }
    else (num < 4 && num > 0) {
      arr.push('I');
      num -= 1;
    }
  }

 var roman = arr.join('');
 console.log(roman);
 return roman;
}

convertToRoman(2);