# Queens College
# Dicrete Structures CSCI 220
# Winter 2024
# Assignment 4 Permutations & Combinations
# Mikdad Abdullah
# Collaborated With Class

import texttable
from math import factorial, perm, comb

#[1] Create a function print_table(name, func, n) that prints a (n+1) x (n+1) table for the function f(i, j) where both i and j iterate over 0 thru n inclusive.
#Print the name of the table
#Add column headings
#Use Python's rjust() function to right-justify your columns so your table looks neat.
#Print a blank line after the table
def print_table(title, headers, data, alignments):
   tt = texttable.Texttable(0)
   tt.set_cols_align(alignments)
   tt.add_rows([headers] + data, True)
   print(title)
   print(tt.draw())
   print()

def c(n,r):
    return comb(n,r)

def p(n,r):
    return perm(n,r)

def c2(n,r):
    return 0 if r > n else fact(n)/(fact(r)*fact(n-r))

def p2(n,r):
    return 0 if r > n else fact(n)/fact(n-r)

def fact(n):
    return 0 if n < 0 else factorial(n)


#[2] From your main function, call print_table using "Permutations" and the built-in math.perm
def functions(f, c, n, t):
    headers = [f"{c}(n,{r})" for r in range(n+1)]
    data = [[f(i, j) for j in range(n+1)] for i in range(n+1)]
    alignments = ["r"] * (n + 1)
    print_table(t, headers, data, alignments)


#[3] From your main function, call print_table using "Permutations" and your own my_perm


#[4] From your main function, call print_table using "Combinations" and the built-in math.comb


#[5] From your main function, call print_table using "Combinations" and your own my_comb
#Manually verify that your answers to 2 match 3, and answers from 4 match 5.
#Your output might look something like this, with 0's instead of the blank cells:


#[6] In the standard game of poker, one is dealt a "hand" of five cards which is classified into one of several categories. For example, "Four of a Kind" means four cards of one rank and one card of another rank. "Full House'' means three cards of one rank, and two cards of another rank. We want to compute the number of possible ways to get a given hand. Then, use this function to compare your calculated answer with the known correct answer and then call it for all standard hands.

def q6():
    hands = [["royal flush",4,c(4,1)],
             ["straight flush",36,c(10,1)*c(4,1)-c(4,1)],
             ["four of a kind",624,c(13,1)*c(4,4)*c(12,1)*c(4, 1)],
             ["full house",3744,c(13,1)*c(4,3)*c(12,1)*c(4,2)],
             ["flush",5108,c(4,1)*c(13,5)-c(10,1)*c(4,1)],
             ["straight",10200,c(4,1)**5 *c(10,1)-c(10,1)*c(4,1)],
             ["three of a kind",54912,c(13,1)*c(4,3)*c(12,2)*c(4,1)**2],
             ["two pair",123552,c(13,2)*c(4,2)**2 *c(11,1)*c(4,1)],
             ["one pair",1098240,c(13,1)*c(4,2)*c(12,3)*c(4,1)**3],
             ["no pairs",1302540,((c(13,5)-c(10,1))*(c(4,1)**5 -c(4,1)))]]


    headers = ["Name", "Frequency", "Computed"]
    alignments = ["l", "r", "r"]
    print_table("Poker hands", headers, hands, alignments)



def main():
    n = 10
    functions(p, "P", n, "permutations using built in perm")
    functions(p2, "P", n, "permutations using our perm function")
    functions(c, "C", n, "combinations using built in comb")
    functions(c2, "C", n, "combinations using our comb function")
    q6()

if __name__ == "__main__":
    main()