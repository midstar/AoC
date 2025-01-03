# Script to run one or multiple puzzles
import argparse, time, sys, os

def run(full_path):
    path, filename = os.path.split(full_path)
    name = os.path.splitext(filename)[0]
    name_path = os.path.join(path,name)
    input_path = os.path.join(path,'input',f'{filename[:2]}.txt')

    answer = ''
    answer_path = os.path.join(path,'input',f'{filename[:3]}_answer.txt')
    if os.path.isfile(answer_path):
        answer = open(answer_path).read()

    sys.path.append(path)
    puzzle = __import__(name)
    
    print(f'{name_path}',end='',flush=True)
    start_time = time.time()
    result = puzzle.solve(open(input_path).read())
    execution_time = time.time() - start_time

    correct = ''
    if answer == '':
        res = '?   '
    elif answer.strip() == str(result):
        res = 'PASS'
    else:
        correct = f' (correct {answer.strip()})'
        res = 'FAIL'

    minutes = int(execution_time) // 60
    seconds = execution_time - minutes * 60

    print(f'  {minutes:02} m {seconds:06.3f} s  {res}  {result}{correct}')

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