import time 
import sys

def print_lyrics():
    lyrics = [
        "Teri nazron ka dil pe hua hai jo asar,",
        "Tu mera mehboob hai jaana",
        "Teri ulfat mein jeeta her pal",
        "Tu ik tohfa hai khuda ka"
    ]
   
    delays = [1.6, 1.4, 1.8, 2.1]

    print("\n Now Playing - Ehsaas \n")
    time.sleep(1.5)
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(delays[i])

print_lyrics()



