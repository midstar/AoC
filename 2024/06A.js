
const DIR = {
  '^' : [-1,  0],
  'v' : [ 1,  0],
  '<' : [ 0, -1],
  '>' : [ 0,  1]
};

function get_new_pos(pos, dir) {
  p = pos.split(',').map((v) => parseInt(v));
  return [p[0] + DIR[dir][0], p[1] + DIR[dir][1]].toString();
}

const DIR_ORDER = ['^', '>', 'v', '<']
function get_new_dir(dir) {
  return DIR_ORDER[(DIR_ORDER.indexOf(dir) + 1) % DIR_ORDER.length];
}

function run(grid, dir, pos) {
  let visited = new Set([[pos,dir]]);
  while(true) {
    next = get_new_pos(pos, dir);
    if (next in grid == false) {
      return (new Set([...visited].map((p) => p[0])));
    }
    if (grid[next] == '#') {
      dir = get_new_dir(dir);
    } else {
      pos = next;
      if ([...visited].filter((p) => p[0] == pos && p[1] == dir).length > 0) {
        return undefined; // In forewer loop
      }
      visited.add([pos, dir]);
    }
  }
}

function solve(input) {
  let grid = {};
  let start = undefined;
  input.split('\n').forEach((line,row) => {
    line.split('').forEach((val,col) => {
      grid[[row,col]] = val;
      if (val == '^') {
        start = [row,col].toString();
      }
    });
  });
  return run(grid,grid[start],start).size;
}

console.log(solve(require('node:fs').readFileSync(process.argv[2], 'utf8').trim()));