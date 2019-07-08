# Regular expressions

![make file](https://www.computerhope.com/jargon/r/regular-expression.gif)
reference(https://www.computerhope.com/unix/regex-quickref.htm)


Regular expressions are a powerful tool for finding and replacing text in a program, or at the command line. This document describes the most common regular expression symbols, and how to use them.

# Description

Regular expressions (shortened as "regex") are special strings representing a pattern to be matched in a search operation. They are an important tool in a wide variety of computing applications, from programming languages like Java and Perl, to text processing tools like grep, sed, and the text editor vim. Below is an example of a regular expression.


The power of regular expressions comes from its use of metacharacters, which are special characters (or sequences of characters) that are used to represent something else. For instance, in a regular expression the metacharacter ^ means "not". So, while "a" means "match lowercase a", "^a" means "do not match lowercase a".

The tables below describe many standard components of regular expressions.


## Anchors and Boundaries

Anchors and boundaries allow you to describe text in terms of where it's located. For instance, you might want to search for a certain word, but only if it's the first word on a line. Or you might want to look for a certain series of letters, but only if they appear at the very end of a word.

## Character Classes

When searching for text, it's useful to be able to choose characters based solely upon their classification. The fundamental classes of character are "word" characters (such as numbers and letters) and "non-word" characters (such as spaces and punctuation marks).

## Quantifiers

Quantifiers allow you to declare quantities of data as part of your pattern. For instance, you might need to match exactly six spaces, or locate every numeric string that is between four and eight digits in length.

## Literal Characters and Sequences

Metacharacters are a powerful tool because they have special meaning, but sometimes they need to be matched literally. For instance, you might need to search for a literal dollar sign ("$") as part of a price list, or in a computer program as part of a variable name. Since the dollar sign is a metacharacter which means "end of line" in regex, you must escape it with a backslash to use it literally.

## Character Sets and Ranges

A character set is an explicit list of the characters that may qualify for a match in a search. A character set is indicated by enclosing a set of characters in brackets ([ and ]). For instance, the character set [abz] will match any of the characters a, b, or z, or a combination of these such as ab, za, or baz.

Ranges are a type of character set which uses a dash in between characters to imply the entire range of characters between them, as well as the beginning and end characters themselves. For instance, the range [e-h] would match any of the characters e, f, g, or h, or any combination of these, such as hef. The range [3-5] would match any of the digits 3, 4, or 5, or a combination of these such as 45.

When defining a range of characters, you can figure out the exact order in which they appear by looking at an ASCII character table.

## Grouping

Grouping allows you to treat another expression as a single unit.

## Extended Regular Expressions

Extended Regular Expressions, or ERE, are an extension of basic regular expressions.

EREs support additional quantifiers, do not require certain metacharacters to be escaped, and obey other special rules. If your application supports extended regex, consult your manual for their proper syntax.


-----
