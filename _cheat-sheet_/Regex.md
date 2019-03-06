# Regex in Python

## How to Use
```python
import re

text = "Mary is 13 years old. John is 102 years old."

# Returns a list of matched strings
ages = re.findall(r'\d{1,3}', text)
names = re.findall(r'[A-Z][a-z]*', text)
allwords = re.findall(r'\w*', text, flags = re.IGNORECASE)

# Returns a match object:
search_is = re.search(r'is', text) 
match_Ma = re.match(r'Ma', text) # Match only from the beginning of the 'text' string

```

## Compile Regex

### Identifiers:
| Symbol | Description |
|---------------|-------------|
|\  | used to escape a character|
|\d  | any number|
|\D  | anything but a number|
|\s  | space|
|\S  | anything but a space|
|\w  | any character|
|\W  | anything but a character|
|.  | any character except a new line|
|`\.`  | actually a period|
|\b  | whitespace around words|

### Modifiers:
| Symbol | Description |
|---------------|-------------|
|{1,3}  | we're expecting 1-3|
|+  | Match 1 or more|
|?  | Match 0 or 1|
|*  | Match 0 or more|
|$  | match the end of a string|
|^  | match the beginning of a string|
||  | matches either or e.g. \d{1-3}|\w{5-6}|
|[]  | Match range or "variance" e.g. [A-Za-z] or [1-5a-qA-Z]|
|{x}  | expecting "x" amount|

### White Space Characters:
| Symbol | Description |
|---------------|-------------|
|\n  | new line |
|\s |  space |
|\t  | tab |
|\e  | escape (rare) |
|\f  | form feed (rare) |
|\r  | return |

### Special Characters need to be escaped:
```
. + * ? [ ] $ ^ ( ) { } \ |
```

Adapted from [sentdex's Youtube Channel](https://www.youtube.com/watch?v=sZyAn2TW7GY)