#!/usr/bin/env python3
# https://adventofcode.com/2021/day/16
from functools import reduce
from operator import mul

version_sum = 0


def to_bin(transmission):
    scale = 16
    num_of_bits = len(transmission) * 4
    return bin(int(transmission, scale))[2:].zfill(num_of_bits)


def to_dec(bits):
    return int(bits, 2)


def get_version(packet):
    return int(packet[0:3], 2)


def get_type_id(packet):
    return int(packet[3:6], 2)


def decode_literal_packet(packet):
    binary_number_carried = ""
    starting_bit = 6
    while True:
        binary = packet[starting_bit:starting_bit + 5]
        binary_number_carried += binary[1:]
        if binary[0] == '0':
            break
        else:
            starting_bit += 5
    return int(binary_number_carried, 2), starting_bit + 5


def get_length_type_id(packet):
    return packet[6]


def decode_packet(packet):
    global version_sum
    V = get_version(packet)
    version_sum += V
    T = get_type_id(packet)
    if T == 4:
        return decode_literal_packet(packet)
    else:
        return decode_operator_packet(packet)


def eval_packet(vals, type_id):
    if type_id == 0:
        return sum(vals)
    elif type_id == 1:
        return reduce(mul, vals, 1)
    elif type_id == 2:
        return min(vals)
    elif type_id == 3:
        return max(vals)
    elif type_id == 5:
        return int(vals[0] > vals[1])
    elif type_id == 6:
        return int(vals[0] < vals[1])
    elif type_id == 7:
        return int(vals[0] == vals[1])
    return vals


def decode_operator_packet(packet):
    I = get_length_type_id(packet)
    vals = []
    L_start = 7
    if I == '0':
        return decode_total_length_operator_packet(L_start, packet, vals)
    else:
        return decode_number_of_sub_packets_operator_packet(L_start, packet, vals)


def decode_number_of_sub_packets_operator_packet(L_start, packet, vals):
    L_end = L_start + 11
    total_number_of_packets = int(packet[L_start:L_end], 2)
    sub_packets = packet[L_end:]
    total_bits_read = L_end
    packets_read = 0
    while packets_read != total_number_of_packets:
        val, bits_read = decode_packet(sub_packets)
        vals.append(val)
        sub_packets = sub_packets[bits_read:]
        packets_read += 1
        total_bits_read += bits_read
    return eval_packet(vals, get_type_id(packet)), total_bits_read


def decode_total_length_operator_packet(L_start, packet, vals):
    L_end = L_start + 15
    total_number_of_bits = int(packet[L_start:L_end], 2)
    sub_packets_start = L_end
    sub_packets_end = sub_packets_start + total_number_of_bits
    sub_packets = packet[sub_packets_start:sub_packets_end]
    while sub_packets != "":
        val, bits_read = decode_packet(sub_packets)
        vals.append(val)
        total_number_of_bits -= bits_read
        sub_packets = sub_packets[bits_read:]
    return eval_packet(vals, get_type_id(packet)), sub_packets_end


if __name__ == "__main__":
    with open('i.txt', 'r') as f:
        hex_transmission = f.readline().strip()
    version_sum = 0
    transmission_evaluation, _ = decode_packet(to_bin(hex_transmission))
    print('p1 =', version_sum)
    print('p2 =', transmission_evaluation)
