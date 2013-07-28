"""
https://www.spotify.com/us/jobs/tech/zipfsong/
Zipf's song
Problem ID: zipfsong

Sample input 1
4 2
30 one
30 two
15 three
25 four

Sample output 1
four
two

Sample input 2
15 3
197812 re_hash
78906 5_4
189518 tomorrow_comes_today
39453 new_genious
210492 clint_eastwood
26302 man_research
22544 punk
19727 sound_check
17535 double_bass
18782 rock_the_house
198189 19_2000
13151 latin_simone
12139 starshine
11272 slow_country
10521 m1_a1

Sample output 2
19_2000
clint_eastwood
tomorrow_comes_today
"""

#-----------------------------------------------------------------#
import sys

#-----------------------------------------------------------------#
"""
Read user input and return it in form of a list
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
Calculate song quality based on Zipf's Law and return 
the songs in decreasing order of quality
"""

def calc_quality(info):
    zipfsong = []
    
    for i in xrange(2, len(info), 2):
        name = info[i+1]
        quality = i/2 * int(info[i])
        zipfsong.append((quality, name))

    zipfsong.sort(reverse=True)
    return zipfsong

#-----------------------------------------------------------------#
"""
"""

def main():

    info = raw_input()

    try:
        zipfsong = calc_quality(info)

        for i in range(int(info[1])):
            print zipfsong[i][1]

    except Exception:         # if not expected input, then print an error message
        print 'hey Spotify, please check your input!'

#-----------------------------------------------------------------#
"""
Assert statements using the above sample test cases
"""

def test():
    test1 = ['4', '2', '30', 'one', '30', 'two', '15', 'three', '25', 'four']
    assert calc_quality(test1)[0:2] == [(100, 'four'), (60, 'two')]
    test2 = ['15', '3', '197812', 're_hash', '78906', '5_4', '189518', 'tomorrow_comes_today', 
            '39453', 'new_genious', '210492', 'clint_eastwood', '26302', 'man_research', \
            '22544', 'punk', '19727', 'sound_check', '17535', 'double_bass', '18782', \
            'rock_the_house', '198189', '19_2000', '13151', 'latin_simone', '12139', \
            'starshine', '11272', 'slow_country', '10521', 'm1_a1']
    assert calc_quality(test2)[0:3] ==  [(2180079, '19_2000'), (1052460, 'clint_eastwood'), (568554, 'tomorrow_comes_today')]

#-----------------------------------------------------------------#
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------#
