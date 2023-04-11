#!/usr/bin/node
// computes and prints a factorial
function factorial(n) {
	if (n > 1) {
		return n * factorial(n - 1);
	} else {
		return 1;
	}
}
const n = parseInt(process.argv[2]);
console.log(factorial(n));
