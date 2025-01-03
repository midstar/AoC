import sys

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
    for input_name, outputs in input_outputs.items():
        for output in outputs:
            if output in machine:
                machine[output].add_input(input_name)

    # Run machine
    pulses = [0, 0]
    for i in range(0, 1000):
        #print('\nRound', i)
        signals = [('button', 0, 'broadcaster')]
        while signals:
            signal = signals.pop(0)
            #print(signal)
            input_name, value, output_name = signal
            pulses[value] += 1
            if output_name in machine:
                signals += machine[output_name].signal(input_name, value)
        
    #print(pulses)
    result = pulses[0] * pulses[1]
    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))