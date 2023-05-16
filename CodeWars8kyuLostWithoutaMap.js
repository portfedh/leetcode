// 16 May 2023

// CodeWars

// JavaScript

// Given an array of integers, return a new array with each value doubled.

// My Solution
function maps(x){
  y = [...x]
  y.forEach((element, index) => {y[index] = element * 2} )
  return y
}

// Better Solution
function maps(x){
  return x.map(n => n * 2);
}
