// Problem Statement #

// Given a set of numbers that might contain duplicates, find all of its distinct subsets.
/**
   * 
[1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
append empty array
append array itself
We can iterate through nums using a loop

append each number as a sub array as long as the subarray isnt a duplicate
current = []

   * 
   */

const find_subsets = function (nums) {
  subsets = [];

  // TODO: Write your code here
  return subsets;
};

console.log(`Here is the list of subsets: ${find_subsets([1, 3, 3])}`);
console.log(`Here is the list of subsets: ${find_subsets([1, 5, 3, 3])}`);
