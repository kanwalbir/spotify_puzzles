"""
https://www.spotify.com/us/jobs/tech/catvsdog/
Cat vs. Dog
Problem ID: catvsdog

Sample input 1
2
1 1 2
C1 D1
D1 C1
1 2 4
C1 D1
C1 D1
C1 D2
D2 C1

Sample output 1
1
3
"""

#-----------------------------------------------------------------#
"""
Read user input and return it in form of list
"""

def read_input():
    info = []
    while True:
        line = raw_input()
        if not line:
            break
        info += line.split(' ')
    return info

#-----------------------------------------------------------------#
"""
Read each test case and return a list of maximum votes for each 
test case
"""

def cat_dog(info):

    p = 3           # Index pointer in the info list
    satisfied = []  # Keeps track of all maximum votes from all test cases
    
    while p < len(info):

        num_votes = int(info[p]) * 2  # number of votes is equal to number of voters times 2
        
        start = p + 1
        end = start + num_votes

        maximum = max_votes(info[start:end])
        satisfied.append(maximum)

        p = end + 2

    return satisfied

#-----------------------------------------------------------------#
"""
Calculate the maximum up/down votes that each animal recevied 
and return the maximum vote value
"""

def max_votes(test_case):

    i = 0
    maximum = 0
    vote_info = {}

    for animal in test_case:
        
        v = '_down'
        if i % 2 == 0:  # If i is even, then it an up vote, otherwise it's a down vote
            v = '_up'

        if animal+v not in vote_info:
            vote_info[animal+v] = 1
        else:
            vote_info[animal+v] += 1

        if vote_info[animal+v] > maximum:
            maximum = vote_info[animal+v]
        
        i += 1

    return maximum

#-----------------------------------------------------------------#
"""
"""

def main():

    info = read_input()

    try:
        satisfied = cat_dog(info)

        if not satisfied:
            raise Exception

        for votes in satisfied:
            print votes

    except Exception:         # if not expected input, then print an error message
        print 'hey Spotify, please check your input!'

#-----------------------------------------------------------------#
"""
Assert statements using the above sample test cases
"""

def test():
    test1 = ['2', '1', '1', '2', 'C1', 'D1', 'D1', 'C1', '1', '2', '4', \
             'C1', 'D1', 'C1', 'D1', 'C1', 'D2', 'D2', 'C1']
    assert cat_dog(test1) == [1, 3]

#-----------------------------------------------------------------#
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------#
