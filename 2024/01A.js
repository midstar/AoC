

function solve(input) {
  const l1 = input.split('\n').map((row) => parseInt(row.split('  ')[0])).sort();
  const l2 = input.split('\n').map((row) => parseInt(row.split('  ')[1])).sort();

  var result = 0;
  for (let i = 0; i < l1.length ; i++){
    result += Math.abs(l1[i] - l2[i])
  }

  return result;
}

console.log(solve(require('node:fs').readFileSync(process.argv[2], 'utf8').trim()));
