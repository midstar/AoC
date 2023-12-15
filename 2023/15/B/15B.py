import argparse

def hash(input):
    h = 0
    for c in input:
        h += ord(c)
        h *= 17
        h = h % 256
    return h

def solve(input):
    #lines = input.splitlines()
    #matrix = [list(line) for line in lines]
    result = 0

    labels = []
    boxes = []
    for i in range(0, 256):
        boxes.append([])
        labels.append({})

    words = input.split(',')
    for word in words:
        if '-' in word:
            label = word.split('-')[0]
            box = hash(label)
            #print(box, 'remove', label)
            if label in boxes[box]:
                boxes[box].pop(boxes[box].index(label))
        if '=' in word:
            label = word.split('=')[0]
            lens = int(word.split('=')[1])
            box = hash(label)
            labels[box][label] = lens
            #print(box, 'add', label)
            if label not in boxes[box]:
                boxes[box].append(label)
        #for i in range(0, len(boxes)):
        #    if len(boxes[i]) > 0:
        #        print(i, boxes[i])
        #print()

    #for i in range(0, len(boxes)):
    #    if len(boxes[i]) > 0:
    #        print(i, boxes[i])
    result = 0
    for box in range(0, len(boxes)):
        for slot in range(0, len(boxes[box])):
            result += (box + 1) * (slot + 1) * labels[box][boxes[box][slot]]

    print('Result: %s' % result)

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        solve(f.read())

if __name__ == '__main__':
    main()    