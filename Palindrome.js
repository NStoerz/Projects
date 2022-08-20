function palindrome(str) {
  //change string to lowercase
  str = str.toLowerCase();
  //remove all non-alphanumeric characters
  const noSpecialCharacters = str.replace(/[^a-zA-Z0-9]/g, '');

  //turn string into an array
  const forward = noSpecialCharacters.split("");

  //make a copy in reverse
  let reverse = forward.slice();
  reverse = reverse.reverse();
  let length = forward.length;

  //convert to string
  const forwardStr = forward.toString();
  const reverseStr = reverse.toString()

  //compare
  if (forwardStr === reverseStr) {
    return true;
  }
  else {
    return false;
  }

}


palindrome("almostomla");