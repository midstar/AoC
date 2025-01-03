# Script to run one or multiple puzzles
import argparse, time, sys, os

def run(full_path):
    path, filename = os.path.split(full_path)
    name = os.path.splitext(filename)[0]
    name_path = os.path.join(path,name)
    input_path = os.path.join(path,'input',f'{filename[:2]}.txt')

    sys.path.append(path)
    puzzle = __import__(name)
    
    print(f'{name_path}',end='',flush=True)
    start_time = time.time()
    result = puzzle.solve(open(input_path).read())
    print(f' Result: {result} (execution time {time.time() - start_time:.4f} s)')

def run_dir(path):
    for root, _, files in os.walk(path, topdown=True):
        for file in sorted(files):
            if os.path.splitext(file)[1] == '.py' and file[:2].isnumeric():
                run(os.path.join(root,file))

def main():
    parser = argparse.ArgumentParser(description=f'Advent Of Code Runner')
    parser.add_argument('path', help='Python file with puzzle solution or directory of puzzles', nargs='?', default='.')
    args = vars(parser.parse_args())

    if os.path.isdir(args['path']):
        run_dir(args['path'])
    else:
        run(args['path'])

if __name__ == '__main__':
    main()   