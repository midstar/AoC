# Script to run one or multiple puzzles
import argparse, time, sys, os, subprocess, inspect, glob

INTERPRETERS = {
    '.py'   : 'import', # Use if scripts has solve() function
    '.js'   : 'node',
    '.pl'   : 'perl',
    '.sh'   : 'sh',
    '.java' : 'java'
}

def execute_script(interpreter, full_path, input_path):
    if interpreter == 'import':
        return execute_python(full_path, input_path)
    
    args = [interpreter, full_path, input_path]

    try:
        output = subprocess.check_output(args)
    except subprocess.CalledProcessError as exception:
        raise RuntimeError(
            "Unable to run:\n"
            + f"{' '.join(args)}\n\n"
            + "Output:\n"
            + exception.output.decode()
        ) from exception

    return output.decode().strip()

# Python will be executed by import and run solve() method
def execute_python(full_path, input_path):
    path, filename = os.path.split(full_path)
    name, ext = os.path.splitext(filename)
    sys.path.append(path)
    puzzle = __import__(name)
    if (hasattr(puzzle, 'solve') and inspect.isfunction(puzzle.solve)):
        return puzzle.solve(open(input_path).read())
    else:
        print(f'\nError! Python script does not have any solve() function!')
        print('Please re-run with the -n argument')
        exit(1)

def time_str(execution_time):
    minutes = int(execution_time) // 60
    seconds = execution_time - minutes * 60

    return f'  {minutes:02} m {seconds:06.3f} s'

def run(full_path):
    path, filename = os.path.split(full_path)
    name, ext = os.path.splitext(filename)
    ext = ext.lower()
    name_path = os.path.join(path,name)
    input_path = os.path.join(path,'input',f'{filename[:2]}.txt')

    print(f'{full_path}',end='',flush=True)
    start_time = time.time()

    if ext not in INTERPRETERS.keys():
        print(f'Not supported file format {ext} in {full_path}')
        return
    else:
        result = execute_script(INTERPRETERS[ext], full_path, input_path) 

    execution_time = time.time() - start_time

    answer = ''
    answer_path = os.path.join(path,'input',f'{filename[:3]}_answer.txt')
    if os.path.isfile(answer_path):
        answer = open(answer_path).read()

    correct = ''
    if answer == '':
        res = '?   '
    elif answer.strip() == str(result):
        res = 'PASS'
    else:
        correct = f' (correct {answer.strip()})'
        res = 'FAIL'

    print(f'  {time_str(execution_time)}  {res}  {result}{correct}')

    return res

def run_multiple(interpreters, paths):
    result = []
    start_time = time.time()

    for path in paths:
        if os.path.isdir(path):
            for root, _, files in os.walk(path, topdown=True):
                for file in sorted(files):
                    if os.path.splitext(file)[1] in interpreters.keys() and file[:2].isnumeric():
                        result.append(run(os.path.join(root,file)))
        else:
            run(path)
    
    execution_time = time.time() - start_time
    print()
    print(f'Total:  {time_str(execution_time)}  PASS: {result.count("PASS")}  FAIL: {result.count("FAIL")}  ?: {result.count("?   ")}')


def main():
    parser = argparse.ArgumentParser(description=f'Advent Of Code Runner')
    parser.add_argument('path', help='Python files with puzzle solution or directories of puzzles', nargs='*', default='.')
    parser.add_argument('-e', '--extension', type=str,
                    help=f'Only run files with extension ({" ".join(INTERPRETERS)})')
    parser.add_argument('-n', '--no-import', action='store_true',
                    help=f'Do not run python scripts by import (use python3 instead)')
    args = vars(parser.parse_args())

    if args['extension'] == None:
        interpreters = INTERPRETERS
    elif args['extension'] in INTERPRETERS.keys():
        interpreters = {args['extension'] : INTERPRETERS[args['extension']]}
    else:
        print(f'{args["extension"]} not supported. Supported are: {" ".join(INTERPRETERS)}')
        exit(1)


    if args['no_import']:
        INTERPRETERS['.py'] = 'python3'

    if len(args['path']) == 1 and os.path.isdir(args['path'][0]) == False:
        run(args['path'][0])
    else:
        run_multiple(interpreters, args['path'])

if __name__ == '__main__':
    main()   