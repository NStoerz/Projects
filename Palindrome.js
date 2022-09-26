/*This project takes a user input and checks to see if it is a palindrome. 
It will automatically remove any non-alphanumeric characters.
*/

//Insert a string below to check to see if it is a palindrome
palindrome("almostomla");

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
  const reverseStr = reverse.toString();

  //compare
  if (forwardStr === reverseStr) {
    return true,
    console.log('true');
  }
  else {
    return false,
    console.log('false');
  }

}