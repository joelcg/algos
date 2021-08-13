# RETURN ARRAY
function fizzbuzz(n) {
  var array = [];
  for (var i = 1; i <= n; i++) {
    let fizz = (i % 3 == 0),
        buzz = (i % 5 == 0);
    if (fizz || buzz) {
      array.push(
        (fizz?"Fizz":"") + 
        (buzz?"Buzz":"")
        );
    } else {
      array.push(i);
    }
  }
  return array;
}


# RETURN OUTPUT ON EACH LINES
function fizzBuzz(n) {
  for (let i = 1; i <= n; i++) {
    let output = '',
      fizz = (i % 3 == 0),
      buzz = (i % 5 == 0);
    if (fizz || buzz) {
      (fizz? output += "Fizz" : "") + 
      (buzz? output += "Buzz" : "")
    } else { 
      output = i 
    }
    console.log(output);
  }
}
