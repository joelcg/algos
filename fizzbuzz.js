'use strict';

function fizzbuzz(n)
{
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
