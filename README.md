In this project, we will programmatically generate tables for permutations P(n, r) and combinations C(n, r), as well as count various hands for the game of Poker. 

[1] Create a function print_table(name, func, n) that prints a (n+1) x (n+1) table for the function f(i, j) where both i and j iterate over 0 thru n inclusive. 

Print the name of the table
Add column headings
Use Python's rjust() function to right-justify your columns so your table looks neat.
Print a blank line after the table 

[2] From your main function, call print_table using "Permutations" and the built-in math.perm

[3] From your main function, call print_table using "Permutations" and your own my_perm

[4] From your main function, call print_table using "Combinations" and the built-in math.comb

[5] From your main function, call print_table using "Combinations" and your own my_comb

Manually verify that your answers to 2 match 3, and answers from 4 match 5.
 
Your output might look something like this, with 0's instead of the blank cells:

http://jwilson.coe.uga.edu/EMAT6680/Parsons/MVP6690/Essay1/excel.html 
 
[6] In the standard game of poker, one is dealt a "hand" of five cards which is classified into one of several categories. For example, "Four of a Kind" means four cards of one rank and one card of another rank. "Full House'' means three cards of one rank, and two cards of another rank. We want to compute the number of possible ways to get a given hand. Then, use this function to compare your calculated answer with the known correct answer and then call it for all standard hands. 

def compare_comb(hand_name, known_answer, computed_answer):
    print("Hand Name:", hand_name, "Known:", known_answer, "Computed:", computed_answer, 
"MATCH" if computed_answer == known_answer else "ERROR")

Here are the two aforementioned examples:

compare_comb("Four of a Kind", 624, comb(13,1)*comb(4,4)*comb(12,1)*comb(4,1))  
compare_comb("Full House", 3744, comb(13,1)*comb(4,3)*comb(12,1)*comb(4,2))  

See https://en.wikipedia.org/wiki/List_of_poker_hands and https://en.wikipedia.org/wiki/Poker_probability. The known and computed answers can be respectively found in the "Frequency" and "Mathematical Expression" columns of the latter link.
