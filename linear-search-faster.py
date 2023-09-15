import random
import math
import time
from multiprocessing import Process, Value, Array
import os

def fastLinearSearch(nums, startIndex, randNumToFind, chunkSize, foundNumber, start_time):
    print('start index: ' + str(startIndex))
    print('chunk size: ' + str(chunkSize))
    if foundNumber == randNumToFind:
        print('done with ' + str(os.getpid()))
        return
    for i in range(startIndex, startIndex + chunkSize):
        if foundNumber == randNumToFind:
            print('done with ' + str(os.getpid()))
            return
        if randNumToFind == nums[i]:
            print('Found number ' + str(randNumToFind))
            print("Took " + str(time.time() - start_time) + " seconds")
            foundNumber = randNumToFind
            print('done with ' + str(os.getpid()))
            return
    print("done and didn't find anything with pid: " + str(os.getpid()))

if __name__ == '__main__':

    nums = Array('i', range(100000000))

    print('Generating nums array')
    for i in range(100000000):
        nums[i] = i
    print('Nums array generated')
    randNum = math.floor(random.random() * len(nums))

    # regular linear search
    print("Linear search for number " + str(randNum))
    start_time = time.time()
    for i in range(len(nums)):
        if (nums[i] == randNum):
            print("Found " + str(randNum))
            print("Took " + str(time.time() - start_time) + " seconds")
            break

    # multiprocessing linear search
    print("Fast linear search for number " + str(randNum))
    start_index_1 = 0
    processes_count = 8
    start_index_2 = math.floor(len(nums) / processes_count) * 1
    start_index_3 = math.floor(len(nums) / processes_count) * 2
    start_index_4 = math.floor(len(nums) / processes_count) * 3
    start_index_5 = math.floor(len(nums) / processes_count) * 4
    start_index_6 = math.floor(len(nums) / processes_count) * 5
    start_index_7 = math.floor(len(nums) / processes_count) * 6
    start_index_8 = math.floor(len(nums) / processes_count) * 7


    chunkSize = math.floor(len(nums) / processes_count)
    start_time = time.time()
    foundNumber = Value('d', -1)  # start at -1, a change shows it was found
    p1 = Process(target=fastLinearSearch, args=(
        nums, start_index_1, randNum, chunkSize, foundNumber, start_time))
    p2 = Process(target=fastLinearSearch, args=(
        nums, start_index_2, randNum, chunkSize, foundNumber, start_time))
    p3 = Process(target=fastLinearSearch, args=(
        nums, start_index_3, randNum, chunkSize, foundNumber, start_time))
    p4 = Process(target=fastLinearSearch, args=(
        nums, start_index_4, randNum, chunkSize, foundNumber, start_time))
    p5 = Process(target=fastLinearSearch, args=(
        nums, start_index_5, randNum, chunkSize, foundNumber, start_time))
    p6 = Process(target=fastLinearSearch, args=(
        nums, start_index_6, randNum, chunkSize, foundNumber, start_time))
    p7 = Process(target=fastLinearSearch, args=(
        nums, start_index_7, randNum, chunkSize, foundNumber, start_time))
    p8 = Process(target=fastLinearSearch, args=(
        nums, start_index_8, randNum, chunkSize, foundNumber, start_time))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
