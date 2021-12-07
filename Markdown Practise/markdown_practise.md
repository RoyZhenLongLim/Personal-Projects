# This is file to learn how to create markdown files #

## Headings ##

Headings use "#"  
The heading will depend on how many "#" are used

## Wrapping ##

Make sure that you use two spaces otherwise the test will not wrap.  
Like so!
See how this doesn't get wrapped

## Gaps ##

If you  need to create extra breaks, you can use br like in html  
For example,
<br>

you can do this

## Horizontal Lines ##

----
There is now a horizontal line here!  
Can be created using 4 dashes (-)

## Emphasis ##

Can emphasis points by bolding and italics.  
Two stars means **bold**.  
Two underscores means __italics__.  
Both are achieved using 3 stars ***bold and italic***.  
This uses `emphasis using back ticks`.

## Links ##

### Basics links ###

[link to my file on github](https://github.com/RoyZhenLongLim/RoyZhenLongLim/tree/master/Markdown%20Practise)

### Mailto links ###

Make sure to use mailto links in case for emails.  
[royzhenlonglim@gmail.com](mailto:royzhenlonglim@gmail.com)

### Identifiers ###

If you need to reference a site multiple times, you can use an identifier
instead.  
[link to github](github_page)
<!-- Identifiers -->

[github_page]: https://github.com/RoyZhenLongLim/RoyZhenLongLim/blob/master/Markdown%20Practise/markdown_practise.md

## Lists ##

### Ordered Lists ###

Write 1, 2, ... and nest whe appropriate.  
E.g.  

1. Item 1
    1. Item 1.1
    2. Item 1.2
2. Item 2

Or you can just use all 1s,

1. Item 1
    1. Item 1.1
    1. Item 1.2
1. Item 2

### Unordered Lists ###

Use dashes (-) to denote unordered lists  
E.g.

- Item
  - Item
  - Item
- Item

## Code Blocks commands ##

To include code, type three ` followed by the language, and close with the same
three characters  
E.g.  

```bash
time
```

```python
i = 0
for i in range(n):
  print(i)
```

## Tables ##

Can create a table by drawing using - and |.  
Here is an example:  

|Heading1  | Heading2                                     |
|----------|----------------------------------------------|
|   1      | What can you do?                             |
|   2      | This is a table                              |
