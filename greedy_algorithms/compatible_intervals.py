# intervals 
intervals = [
    [4, 36], [17, 147], [5, 18], [62, 67], [16, 32], [96, 128], [21, 117], 
    [19, 122], [64, 168], [45, 99], [12, 55], [20, 26], [79, 126], [3, 9], 
    [89, 101], [55, 112], [26, 157], [1, 2], [16, 116], [49, 70], [26, 60], 
    [52, 153], [16, 28], [20, 83], [158, 166], [3, 7], [7, 8], [61, 140], 
    [1, 4], [12, 170], [19, 57], [35, 110], [54, 155], [93, 137], [47, 58], 
    [49, 114], [115, 174], [60, 61], [64, 90], [3, 142], [4, 145], [89, 119], 
    [24, 76], [22, 154], [63, 108], [8, 27], [26, 49], [18, 77], [106, 175], 
    [2, 87], [7, 148], [65, 66], [36, 135], [17, 118], [96, 130], [38, 171], 
    [4, 40], [24, 38], [22, 132], [129, 144]
]

def interval_scheduling(intervals):

    # sort by non decreasing endtime
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    S = [] # stores selected intervals
    
    # iterating thru sorted intervals
    for interval in sorted_intervals:
        start, end = interval #start of the current interval
        
        # if s is empty, add the interval with the earliest start time
        if not S:
            S.append(interval)
        else: 
            # finding the last intervals end time 
            last_end_time = S[-1][1]
            
            #checking that the start time is greater than the last intervals start time
            if start > last_end_time:
                S.append(interval) # adding it to the list
                
    return S

if __name__ == "__main__":
    selected_intervals = interval_scheduling(intervals)
    
    print(f"Total intervals selected: {len(selected_intervals)}")
    print(f"All selected intervals: {selected_intervals}")
    print("-" * 30)

# RUNTIME: O(n log n) - Sorting the intervals takes O(n log n). The subsequent iteration 
# through the list takes O(n) time to check for conflicts. 
# Total time = O(n log n) + O(n) = O(n log n)