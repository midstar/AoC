import sys

reg_a = 0
reg_b = 0
reg_c = 0

def combo(operand):
    match(operand):
        case 4:
            return reg_a
        case 5:
            return reg_b
        case 6:
            return reg_c
        case 7:
            print("Invalid operand!!!")
            return 0
    return operand

def debug(str):
    #print(str)
    return

def debug_regs(pc, operand):
    #print(f'A:{reg_a} B:{reg_b} C:{reg_c} PC:{pc} Operand:{operand} Combo:{combo(operand)}')
    return

def run(program,a,b,c):
    global reg_a, reg_b, reg_c
    reg_a = a
    reg_b = b
    reg_c = c
    pc = 0
    out = []
    while pc < len(program):
        debug_regs(pc, program[pc+1])
        match(program[pc]):
            case 0: # adv
                debug('adv')
                reg_a = int(reg_a / (2**combo(program[pc+1])))
            case 1: # bxl
                debug('bxl')
                reg_b = reg_b ^ program[pc+1]
            case 2: # bst
                debug('bst')
                reg_b = combo(program[pc+1]) % 8
            case 3: # jnz
                debug('jnz')
                if reg_a != 0:
                    pc = program[pc+1] - 2
            case 4: # bxc
                debug('bxc')
                reg_b = reg_b ^ reg_c
            case 5: # out
                debug('out')
                out.append(combo(program[pc+1]) % 8)
            case 6: # bdv
                debug('bdv')
                reg_b = int(reg_a / (2**combo(program[pc+1])))
            case 7: # cdv
                debug('cdv')
                reg_c = int(reg_a / (2**combo(program[pc+1])))
        pc += 2

    debug_regs(pc, 0)
    
    return out

def find_a(program, a=0, depth=0):
    target = program[::-1]
    if depth == len(target):
        return a
    for i in range(8):
        output = run(program, a*8 + i, 0, 0)
        if output and output[0] == target[depth]:
            if result := find_a(program, (a*8 + i), depth+1): 
                return result
    return 0

def solve(input):
    lines = input.splitlines()
    program = [int(v) for v in lines[4].split()[1].split(',')]
    
    return find_a(program)

        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))