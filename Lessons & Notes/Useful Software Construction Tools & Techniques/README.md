# Filters

## What are filters?
A **filter** is a program that transforms a byte stream

On a Unix-like system, filters are commands that

- read bytes from their standard input or specified file
- perform useful transformation on the stream
- write the transformed bytes to their standard output

Shell I/O redirection can be used to specify the source and destination files

For example
```commandline
filter < abc > xyz
```
In this example

- `abc` is the source file
- we give `filter` `abc` 
- `xyz` is the output

Alternatively, some filters can take multiple inputs. For example:
```commandline
filter abc def ghi > xyz
```

- We are giving the `filter` `abc`, `def`, and `ghi` and storing the output in `xyz`

## Using filters

To make use filter easier, we specify certain formats

`|` lets use run one after the other (the following command is an example of this)
```commandline
filter1 | filter2 | ... | filterN
```

`-` is a filename that represents the standard input

## Options
Most filters have options that control their behaviour  
To use them, use `-k` where is a letter with some special meaning


## Useful filters

### cat

One of the simplest is `cat`

- Will pass the byte stream unchanged
- The following command will print the contents of the file to the terminal

```commandline
cat {filename}
```
Has the following options
- `-n` numbers output line starting from 1
- `-A` displays non-printing character
  - Handy for debugging
- `s` squeezes consecutive blank lines into a single blank line

### wc

Stands for word count
- Prints the result in the format `{number of lines} {number of words} {number of characters}`

Options
- `-c` print the number of characters
- `-w` prints the number of words (non-white space) only
- `-l` prints the number of lines only

### head/tail

Selects the first and last lines

- Head will print the first `n` lines
  - default is 10
- Tail will print the last `n` lines
    - default is 10

Options
-`-n {N}` changes the number of lines to `N`

### cut

Prints select field, column seperator defaults to tab

- cut can select a range of character positions

Options

- -f{listOfCols} prints only the specified field (tab-separated) on output
- -c{listoOfPos} prints only characters in the specified position
- -dc use the character c as the field seperator

```commandline
cut -f1 data                // Prints first column
cut -f1-3 data              // Prints the first three columns
```

## sort

Copies output to output but ensures that the output is arranged in some particular order of lines  
By default, sorting is based on the first characters in the line

Options

- `-r` sort in descending order (reverse order)
- `-n` sort numerically rather than lexicographically
- `-d` dictionary order, ignore non-letters and non-digits
- `tc` use character c to separate columns (default is space)
- `-kn` sort on column `n`

## Unique 

Removes all but one copy of adjacent identical lines

Options
- `-c` also prints number of times each line is duplicated
- `-d` only prints (one copy of) duplicated lines
- `-u` only prints lines that occur once

## find

Search files based on specified properties

Invocation: `find directories tests actions`

- `tests` examines the file properties
- `actions` can be simply print the name of execute arbitrary command

## join

Merges two files using the value in a field in each file as a common key

Options
- `-1 k` key field in file 1 is `k`
- `-2 k` key field in file 2 is `k`
- `-a N` print a line for each unpairable line in file `N` (can be one or two)
- `-i` ignore case
- `-t c` tab character is `c`

## paste

Displays multiple files in parallel

# Regular Expression (Regex)

A regular expression (regex) often thought of as a pattern

## Writing Regex

- Unless a character has a special meaning it matches itself
- `p*` denotes zero or more repetitions of `p`
  - `p*` is the same as ``, `p`, `pp`,...
- `p?` denotes zero or one more occurrence of p
- `p+` denotes one or more repetitions of p
- `p{n}` denotes `n` repetitions of `p`
- `p{n, m}` denotes `n` to `m` repetitions of `p
- `p{n,}` denotes `n` or more repetitions of p
- `|` means union
  - Use to check if an expressions matches a number of expressions
- `()` parentheses are used for grouping
  - `c(, c)*` matches `c`, `c, c`, `c, c, c`,...
- `\` backslash gets rid of any special meaning to a character
  - `\*` just means `*` without the repetition
- `.` matches any single character
- `[]` square brackets provide convenient matching of any one of a set of characters
  - `[abc]` means if it matches any of `a`, `b` or `c`
  - A shorthand is available for ranges of characters `[first - last]`
    - `[a-e]`, `[a-z]`, `[0-9]`, `[a-zA-z]`, [A-Za-z]`, and `[a-zA-Z0-9]`
- `^` Square bracket matching can be inverted with ``^`
  - i.e. Match any character except what is in square brackets
  - Also used to denote the start of a string
- `$` is used to denote the end of a string