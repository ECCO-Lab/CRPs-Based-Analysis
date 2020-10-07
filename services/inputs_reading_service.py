
import csv
import datetime
from views.analysis import *
from services.conversing_service import *


def getFilesObjects(files,path,i,chunk):
    """
    # For CSV Inputs
    :param files: list of files names
    :param path: path to files directory
    :param i: index to start the inputs chunk reading
    :param chunk: chunk size
    :return: a list of generator objects, each represent a chunk for each file.
    """
    for file in files:
        with open(f'{path}/{file}', 'r') as f:
            reader = list(csv.reader(f))[i:i+chunk]
            yield reader


def matrix_generator(data, NFiles, multi_dev=1):

    """

    :param data: input data
    :param NFiles: number of files
    :param multi_dev: conditional variable if data provided is for mutple devices, default is 1(yes)
    :return: matrix
    """

    UniformityResultsArray = []
    UniquenessResultsArray = []
    BitAliasingResultsArray = []
    ReliabilityResultsArray = []

    for k, v in data.items():
        temp = []
        for val in v:
            temp.append(hex2binary(val))

        NBits = len(temp[0])

        if multi_dev == 1:

            UniformityResultsArray.append(Uniformity(temp, NBits, NFiles))  # The result will be of (#CRP x NFiles) dimensions
            UniquenessResultsArray.append((2 / (NFiles * (NFiles - 1))) * Uniqueness(temp, NBits, NFiles))
            BitAliasingResultsArray.append(BitAliasing(temp, NFiles))

        elif multi_dev == 0:

            ReliabilityResultsArray.append(Reliability(temp, NFiles))

    return [UniformityResultsArray, UniquenessResultsArray, BitAliasingResultsArray, ReliabilityResultsArray]





def csvAdapter(files, path, chunk=10000):

    """

    :param files: lsit of files names
    :param path: path to files directory
    :param chunk: chunk size
    :return: Common matrix, input for the Analysis fns
    """

    results = []

    with open(path + files[0]) as f:
        lines = sum(1 for line in f)

    for i in range(0, int(lines), chunk):
        print('Current Chunk ',i*len(files), (chunk + i)*len(files))

        output = {}
        data = getFilesObjects(files, path, i, chunk)

        for ll in list(data):
            for line in ll:
                key, value = line

                if key not in output.keys():
                    output.setdefault(key, [])
                    output[key].append(value.strip())

                else:
                    output[key].append(value.strip())

        NFiles = len(files)
        results.append(matrix_generator(output,NFiles))

    return results


