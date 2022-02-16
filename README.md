# Hitori
Hitori game in Python, made as a class project


## How to play
The objective is to eliminate some squares to transform the grid to a state where all the three rules are respected


Red cell: Eliminated  
Green cell: Considered as safe  
White cell: Neutral

### Buttons
- Left -> Confirm and check if you won
- Middle -> Pause the game & timer
- Right -> Click to reset all cells to white or Shift+Click to get another board


### Rules
  1. No row or column can have more than one occurence of any number
  2. Eliminated cells cannot be horizontally or vertically adjacent (Diagonal allowed)
  3. All the remaining cells must be connected to each other, horizontally or vertically (No diagonal)


### Developed with
  - [pygame](https://pypi.org/project/pygame/) (Interface)
  - [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) (Scraping of the boards)
  - [requests](https://pypi.org/project/requests/) (Scraping of the boards)



## Credits
Thought and developed by [@ZeyXs](https://github.com/ZeyXs), [@ghrlt](https://github.com/ghrlt) and [@myaalicewendy](https://github.com/myaalicewendy)  
