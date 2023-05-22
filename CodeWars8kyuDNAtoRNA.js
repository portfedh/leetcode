// 22 May 2023

// CodeWars

// JavaScript

// Summation

// Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

// Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

// Create a function which translates a given DNA string into RNA.

// For example:

// "GCAT"  =>  "GCAU"


function DNAtoRNA(string){
    string.toUpperCase()
    let myArray = []
    for(i=0; i<string.length; i++){
        if(string[i] == 'T'){
            myArray.push('U')
        } else{
            myArray.push(string[i])
        }
    }
    myArray = myArray.join('')
    return myArray
}


