// 17 May 2023

// CodeWars

// JavaScript

// Remove the first and last character

// In this simple assignment you are given a number and have to make it negative. 
// But maybe the number is already negative?


function makeNegative(num) {
  if(num > 0 ) {
    num = num * -1
  }
  return num
}


// makeNegative(1);    // return -1
// makeNegative(-5);   // return -5
// makeNegative(0);    // return 0
// makeNegative(0.12); // return -0.12
