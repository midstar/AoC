
function isSafe(report) {
  const diffs = new Set();
  for (let i = 1 ; i < report.length ; i++) {
    diffs.add(report[i-1] - report[i]);
  }
  const max = Math.max(...diffs);
  const min = Math.min(...diffs);
  if ((min > 0 && max <=3) || (min >= -3 && max < 0)) {
    return true;
  }
  return false;
}
function solve(input) {
  const reports = input.split('\n').map((row) => row.split(' ').map((v) => parseInt(v))).sort();
  return reports.filter(isSafe).length;
}

console.log(solve(require('node:fs').readFileSync(process.argv[2], 'utf8').trim()));