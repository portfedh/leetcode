// 13 May 2023

// CodeWars

// JavaScript

// Clock shows h hours, m minutes and s seconds after midnight.

// Your task is to write a function which returns the time since midnight in milliseconds.


// Example

// h = 0
// m = 1
// s = 1

// result = 61000

function past(h, m, s){
  let hourSeconds = h * 60 * 60;
  let minuteSeconds = m * 60;
  let seconds = s;
  let totalSeconds = hourSeconds + minuteSeconds + seconds;
  let miliSeconds = totalSeconds * 1000;
 
  return miliSeconds;

}