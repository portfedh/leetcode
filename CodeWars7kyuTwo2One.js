// 29 Jul 2023

// CodeWars

// JavaScript

// Take 2 strings s1 and s2 including only letters from a to z.
// Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

// Example:
// a = "xyaabbbccccdefww"
// b = "xxxxyyyyabklmopq"
// longest(a, b) -> "abcdefklmopqwxy"


function longest(s1, s2) {
  // Transform string into array
  const str1 = s1.split('');
  const str2 = s2.split('');
  console.log(`Array s1: ${str1}`)
  console.log(`Array s2: ${str2}`)

  // Merge both arrays
  const mergedArray = [...str1, ...str2];
  console.log(`Merged array: ${mergedArray}`)

  // Keep only unique elements
  let uniqueArray = [...new Set(mergedArray)];
  console.log(`Unique array: ${uniqueArray}`)

  // Sort array
  uniqueArray = uniqueArray.sort();
  console.log(`Sorted array: ${uniqueArray}`)

  return uniqueArray.join('');
}

// Test.assertEquals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
// Test.assertEquals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
// Test.assertEquals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")