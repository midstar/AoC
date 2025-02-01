import sys
import math

def val_from_hex(hex,nbr_bits,lsb_bit):
    return (int(hex,16) >> lsb_bit) & int('1' * nbr_bits,2)

def get_val(hex,nbr_bits,start_bit):
    hex_start = start_bit // 4
    start_bit = start_bit % 4
    hex_size = math.ceil((nbr_bits + start_bit) / 4)
    lsb_bit = 4 * hex_size - (start_bit + nbr_bits)
    return val_from_hex(hex[hex_start:hex_start + hex_size], nbr_bits, lsb_bit)

def parse_packet(packet, offset):
    global version_sum
    version = get_val(packet,3,offset)
    offset += 3
    type_id = get_val(packet,3,offset)
    offset += 3
    result = {'version':version,'type_id':type_id}
    if type_id == 4:
        # Literal
        val = 0
        i = 0
        while True: 
            sub_val =  get_val(packet,5,offset) 
            offset += 5
            if i > 0:
                val = val << 4
            val = val + (0xF & sub_val) 
            i += 1
            if (sub_val & 0x10) == 0: break 
        result['value'] = val
    else:
        # Operator
        length_type_id = get_val(packet,1,offset)
        offset += 1
        result['sub_packets'] = []
        if length_type_id == 0:
            total_length = get_val(packet,15,offset)
            offset += 15
            stop_at = offset + total_length
            while offset < stop_at:
                sub_packet, offset = parse_packet(packet,offset)
                result['sub_packets'].append(sub_packet)
        else:
            total_subpackets = get_val(packet,11,offset)
            offset += 11
            for _ in range(total_subpackets):
                sub_packet, offset = parse_packet(packet,offset)
                result['sub_packets'].append(sub_packet)             
            
    return result, offset

def calc(node):
    if 'sub_packets' in node:
        values = [calc(node) for node in node['sub_packets']]
    match node['type_id']:
        case 0:
            return sum(values)
        case 1:
            return math.prod(values)
        case 2:
            return min(values)
        case 3:
            return max(values)
        case 4:
            return node['value']
        case 5:
            return values[0] > values[1]
        case 6:
            return values[0] < values[1]
        case 7:
            return values[0] == values[1]
    print('ERROR')

def solve(input):
    node, _ = parse_packet(input, 0)
    return calc(node)
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))