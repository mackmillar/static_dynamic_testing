### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  # syntax error (no semicolon after else)
  # needs to be == not =
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
  # syntax error (dif instead of def);
  # syntax error (no comma between card1 & card2)
  # cant return just card needs to be card1 or card2

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# need to define variable total
# wrong identation on the return statement

def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
