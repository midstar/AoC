# Script to run one or multiple puzzles
import argparse, time, sys, os

def time_str(execution_time):
    minutes = int(execution_time) // 60
    seconds = execution_time - minutes * 60

    return f'  {minutes:02} m {seconds:06.3f} s'

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

    print(f'  {time_str(execution_time)} {res}  {result}{correct}')
    
    del puzzle # clean-up

    return res

def run_dir(path):
    result = []
    start_time = time.time()

    for root, _, files in os.walk(path, topdown=True):
        for file in sorted(files):
            if os.path.splitext(file)[1] == '.py' and file[:2].isnumeric():
                result.append(run(os.path.join(root,file)))
    
    execution_time = time.time() - start_time
    print()
    print(f'Total:  {time_str(execution_time)}  PASS: {result.count("PASS")}  FAIL: {result.count("FAIL")}  ?: {result.count("?   ")}')


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