// 10 Jun 2023

// CodeWars

// JavaScript

// Find the smallest integer in the array

// Given an array of integers your solution should find the smallest integer.

// For example:

//     Given [34, 15, 88, 2] your solution will return 2
//     Given [34, -345, -1, 100] your solution will return -345

// You can assume, for the purpose of this kata, that the supplied array will not be empty.


class SmallestIntegerFinder {
  findSmallestInt(args) {
    let minNumber = args[0]
    for(i=0; i <args.length; i++){
      if(args[i] < minNumber) {
        minNumber = args[i];
      };
    };
    return minNumber
  }
}

let sif = new SmallestIntegerFinder();
sif.findSmallestInt([78,56,232,12,8]);


