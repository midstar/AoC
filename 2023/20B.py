import sys
import math

class Broadcaster:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
    def signal(self, input_name, value):
        signals = []
        for output_name in self.outputs:
            signals.append((self.name, value, output_name))
        return signals

class FlipFlop:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.is_on = False
    def add_input(self, input_name):
        pass # Does not matter
    def signal(self, input_name, value):
        signals = []
        if value == 0:
            out_value = 1
            if self.is_on:
                out_value = 0
            for output_name in self.outputs:
                signals.append((self.name, out_value, output_name))
            self.is_on = not self.is_on
        return signals

class Conjunction:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.is_on = False
        self.inputs = {}
    def add_input(self, input_name):
        self.inputs[input_name] = 0
    def signal(self, input_name, value):
        signals = []
        self.inputs[input_name] = value
        out_value = 0
        for _, ivalue in self.inputs.items():
            if ivalue != 1:
                out_value = 1
        for output_name in self.outputs:
            signals.append((self.name, out_value, output_name))
        return signals
    def state(self):
        return self.inputs

def solve(input):
    machine = {}
    input_outputs = {}

    # Create all parts of machine
    for line in input.splitlines():
        name_outputs = line.split('->')
        name = name_outputs[0].strip()
        outputs = [s.strip() for s in name_outputs[1].split(',')]
        if name == 'broadcaster':
            machine[name] = Broadcaster(name, outputs)
        elif name[0] == '%':
            name = name[1:]
            machine[name] = FlipFlop(name, outputs)
        elif name[0] == '&':
            name = name[1:]
            machine[name] = Conjunction(name, outputs)
        input_outputs[name] = outputs

    # Connect all parts to inputs
    rx_input = ''
    for input_name, outputs in input_outputs.items():
        for output in outputs:
            if output == 'rx':
                rx_input = input_name
            if output in machine:
                machine[output].add_input(input_name)
    #print(rx_input)


    # Run machine
    rx_pulses = [0,0]
    period = {}
    for i in range(0, 15000):
        signals = [('button', 0, 'broadcaster')]
        while signals:
            signal = signals.pop(0)
            #print(signal)
            input_name, value, output_name = signal

            # Conjunction node connected to rx. Check
            # if inputs to this node are periodic. 
            if output_name == rx_input and value == 1:
                if input_name not in period:
                    period[input_name] = []
                period[input_name].append(i)

            if output_name in machine:
                signals += machine[output_name].signal(input_name, value)
    
    offset = []
    for p, l in period.items():
        #print(p, l)
        o = []
        for i in range(0, len(l) - 1):
            o.append(l[i+1] - l[i])
        #print('  ', o)
        offset.append(o[0])

    result = math.lcm(*offset)
    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))