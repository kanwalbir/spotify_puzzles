"""
https://www.spotify.com/us/jobs/tech/reversed-binary/
Reversed Binary Numbers
Problem ID: reversebinary

Sample input 1
13

Sample output 1
11

Sample input 2
47

Sample output 2
61
"""

#-----------------------------------------------------------------#
import sys

#---------------------------------------------------------------------#
"""
Convert integer into binary, reverse the binary, convert binary back 
into integer
"""

def rev_bin(r):
    n = int(r)                 # convert the raw input string into an integer
    n_bin = str(bin(n))[2:]    # convert the integer into a binary string, excluding '0b' in front
    n_bin_rev = n_bin[::-1]    # reverse the binary string characters
    n_rev = int(n_bin_rev, 2)  # convert the binary string back into an integer
    
    return n_rev

#---------------------------------------------------------------------#
"""
"""

def main():

    info = raw_input()

    try: 
        print rev_bin(info)

    except ValueError:          # if invalid entry, then print an error message
        print 'hey Spotify, thats not a valid positive integer!'

#---------------------------------------------------------------------#
"""
Assert statements using the above sample test cases
"""
def test():
    assert rev_bin(13) == 11
    assert rev_bin(47) == 61

#---------------------------------------------------------------------#
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------#
