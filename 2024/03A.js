function solve(input) {
  let result = 0;
  for (match of input.matchAll(/mul\((\d+),(\d+)\)/g)) {
    result += match[1] * match[2];
  }
  return result;
}

console.log(solve(require('node:fs').readFileSync(process.argv[2], 'utf8').trim()));