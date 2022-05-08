# Filters

## What are filters?
A **filter** is a program that transforms a byte stream

On a Unix-like system, filters are commands that

- read bytes from their standard input or specified file
- perform useful transformation on the stream
- write the transformed bytes to their standard output

Shell I/O redirection can be used to specificy the source and destination files

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

## Useful filters
One of the simplest is `cat`

- Will pass the byte stream unchanged
- The following command will print the contents of the file to the terminal

```commandline
cat {filename}
```
