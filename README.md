# Chemical Reactions

Everybody knows that a huge number of different chemical reactions happen in cells. A reaction takes as an input a set of chemicals (substrates) and converts them to another set (products). Here we consider all reactions to be one-directional. A substrates for a reaction could be chemicals from the environment or products from other reactions.

A scientist John Doe was given a cell and a list of chemicals that are present in the environment at the beginning. He already knows what reactions could happen in the cell. You should help him to understand which chemicals could appear in the cell.

## Input Format

The first line contains initial chemicals separated by spaces. There is always at least one initial chemical. Each chemical is represented by a random positive integer that fits in 4-byte integer type. Each of the following lines describes a reaction, one per line. Each reaction is presented as two lists of integers separated by "->": the list of chemicals, separated by "+", that is needed to perform a reaction and the list of chemicals, separated by "+", that are produced as a result of the reaction. Each chemical could be present in each reaction maximum 2 times: one time at the left part and the other time at the right part (for example, a catalyst could appear in both parts).

Constraints for the easy version: a total number of chemicals through all reactions does not exceed 10<sup>3</sup>.  
Constraints for the hard version: a total number of chemicals through all reactions does not exceed 10<sup>5</sup>.

## Output Format

The sole line of the output should contain the unordered list of all chemicals that could appear in the cell at any moment of time.

## Examples

### Sample Input 1

```
4
4+6->1
2->3+5
4->6
6+4->5
```

### Sample Output 1

```
1 4 5 6
```

### Sample Input 2

```
1 2
1+2->4
1+2->3
3->4+5
4->4
```

### Sample Output 2

```
1 5 2 4 3
```

## Limits

Memory limit per test: 256 Megabytes  
Time limit per test: 2 seconds

# The Secondary Structure of RNA

RNA consists of ribonucleotides of 4 types: adenine (A), cytosine (C), guanine (G), uracil (U). Therefore RNA can be represented as a string that consists of the characters A, C, G, U. It is known that the ribonucleotides A-U and C-G are complementary to each other.

RNA consists of one strand (chain of ribonucleotides) most of the time, and sometimes it can fold into the secondary structure. In this problem we consider a simpler secondary form than in real life. In this form, some pairs of complementary ribonucleotides build hydrogen bonds between them and each ribonucleotide can build at most one bond. Each bond can be represented as a pair of indices `(i, j), i < j` of the string S that represents RNA. These indices indicate the positions of the symbols in S corresponding to these ribonucleotides.

The string S with even length is **perfect** if the corresponding RNA could have a secondary structure in which each nucleotide is contained in a bond.
The string S with odd length is **almost perfect** if we could get a perfect string by removing exactly one symbol.

Your task is to check if the given string S is perfect, almost perfect or imperfect.

## Input Format

The only line of the input contains string S of symbols A, G, C, U. The length of S is greater than 1.

Constraints for the easy version: the length of the string S does not exceed 151.  
Constraints for the hard version: the length of the string S does not exceed 3⋅10<sup>5</sup> + 1.

## Output Format

If the string S is perfect, the sole line of the output should contain the string "perfect" (without quotes). If the string S is almost perfect, the sole line of the output should contain the string "almost perfect" (without quotes). Otherwise, the sole line should contain "imperfect" (without quotes).

## Examples

### Sample Input 1

```
UGCA
```

### Sample Output 1

```
perfect
```

### Sample Input 2

```
AGUCU
```

### Sample Output 2

```
almost perfect
```

### Sample Input 3

```
CAGUU
```

### Sample Output 3

```
imperfect
```

## Limits

Memory limit per test: 256 Megabytes  
Time limit per test: 2 seconds
