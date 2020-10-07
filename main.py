

import sys
sys.path.append(".")

import os
print (os.getcwd())

# print(sys.path)
import datetime
import os
from views.analysis import *
from services.inputs_reading_service import *
from services.conversing_service import *









def start_analysis():

    start_time = datetime.datetime.now()

    path = 'datasets/xored_inputs/'
    # path = 'datasets/400/'

    arr = os.listdir(path)

    analysis = csvAdapter(arr, path, chunk=10000)

    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds()
    print(execution_time)

    # Total_UniformityResultsArray = []
    # Total_UniquenessResultsArra = []
    # Total_BitAliasingResultsArray = []
    # Total_ReliabilityResultsArray = []
    #
    # for i in range(0, len(analysis), 1):
    #     Total_UniformityResultsArray += analysis[i][0]
    #     Total_UniquenessResultsArra += analysis[i][1]
    #     Total_BitAliasingResultsArray += analysis[i][2]
    #     Total_ReliabilityResultsArray += analysis[i][3]
    #
    # data_final = [np.array(Total_UniformityResultsArray), np.array(Total_UniquenessResultsArra),np.array(Total_BitAliasingResultsArray), np.array(Total_ReliabilityResultsArray)]
    #
start_analysis()