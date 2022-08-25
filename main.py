import math

'''
Given k, scale_factor in (0, 1) and bias_threshold, returns the minimum number of
kmers required to make sure the bias is larger than the provided threshold.
Example: scale_factor = 0.1, threshold = 0.99, k = 21 will return 44. This means
we need >= 44 kmers to make sure the resulting bias factor >= 0.99, and hence the bias is <= 0.01
'''
def required_num_kmers(scale_factor, k, bias_threshold=0.99999):
    num_kmers = math.ceil(math.log(1.0 - bias_threshold) / math.log(1.0 - scale_factor))
    return int(num_kmers)

if __name__ == "__main__":
    scale_factor = 0.1
    bias_threshold = 0.99
    k = 21

    print( required_num_kmers(scale_factor, k, bias_threshold) )
