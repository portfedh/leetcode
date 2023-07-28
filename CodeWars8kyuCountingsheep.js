// Counting Sheep

// Consider an array/list of sheep where some sheep may be missing from their place. 
// We need a function that counts the number of sheep present in the array (true means present).

function countSheeps(arrayOfSheep) {
  let presentSheep = 0;
  for(let i=0; i < arrayOfSheep.length; i++){
    if(arrayOfSheep[i] === true){
      presentSheep = presentSheep + 1
    }
  }
  return presentSheep
}

array1 = [true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true];


  console.log(countSheeps(array1))
  // Returns 17