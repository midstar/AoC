

function solve(input) {
  const l1 = input.split('\n').map((row) => parseInt(row.split('  ')[0]));
  const l2 = input.split('\n').map((row) => parseInt(row.split('  ')[1]));

  var result = 0;
  for (let i = 0; i < l1.length ; i++){
    result += l1[i] * l2.filter((v) => v == l1[i]).length;
  }

  return result;
}

console.log(solve(require('node:fs').readFileSync(process.argv[2], 'utf8').trim()));