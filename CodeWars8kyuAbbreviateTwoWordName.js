// Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

// The output should be two capital letters with a dot separating them.

// It should look like this:

// Sam Harris => S.H

// patrick feeney => P.F


function abbrevName(name){
    let nameList = []
    nameList = name.split(' ')
    let initial1 = nameList[0][0].toUpperCase()
    let initial2 = nameList[1][0].toUpperCase()
    abbreviated = initial1 + '.' + initial2
    return abbreviated
}

console.log(abbrevName('gochuki cruz'))