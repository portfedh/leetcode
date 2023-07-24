// 24 Jul 2023

// CodeWars

// JavaScript

// 8 Ky

// This function should test if the factor is a factor of base.

// Return true if it is a factor or false if it is no.
// Factors are numbers you can multiply together to get another number.
// You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.

function checkForFactor (factor, base) {
    const remainder = factor % base;
    if(remainder === 0 ){
      console.log(`factor: ${factor}, base: ${base} remanider: ${remainder}`)
      return true
    } else {
      console.log(`factor: ${factor}, base: ${base} remanider: ${remainder}`)
      return false
    }
  }

