let array = new Array(100)

for (let element of array.keys()) {
  let printedValue = element + 1 
  
  printedValue = 
    printedValue % 15 === 0 ? "FizzBuzz" :
    printedValue % 5 === 0 ? "Buzz" : 
    printedValue % 3 === 0 ? "Fizz" : 
    printedValue
  
  console.log(printedValue)
}
