
import numpy as np

def hex2binary(hex_string):
    """

    :param hexdecimal string:
    :return: numpy array of binary representation of the hexadecimal input

    """

    value = bin(int('1' + hex_string, 16))[3:]
    binary = np.fromiter(map(lambda x: int(x) if x.isdigit() else x, value), dtype=np.int)
    return binary
