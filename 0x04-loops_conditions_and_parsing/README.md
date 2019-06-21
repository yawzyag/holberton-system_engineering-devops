# Loops, conditions and parsing

[![N|holi](https://i.redd.it/dzddok0jf5ny.jpg)
reference(https://www.linuxtopia.org/online_books/advanced_bash_scripting_guide/loops1.html)]


A loop is a block of code that iterates (repeats) a list of commands as long as the loop control condition is true.

  - Type some Markdown on the left
  - See HTML in the right
  - Magic

# for loops

    for arg in [list]
    
This is the basic looping construct. It differs significantly from its C counterpart.

    for arg in [list]
    do 
    command(s)... 
    done

### Example

    #!/bin/bash
    # Listing the planets.

     for planet in Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto
    do
      echo $planet  # Each planet on a separate line.
    done

    echo

    for planet in "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto"
    # All planets on same line.
    # Entire 'list' enclosed in quotes creates a single variable.
    do
       echo $planet
    done

    exit 0
