# AutocompleteSpelunker
Retrieve all autocomplete results for a particular string. 

`autocomplete-spelunker.py` iterates through character combinations to a depth that you specify (example: `how can i a` ,`how can i b`, `how can i c`) and fetches the autocomplete results for all of them, mashing them together into one big sorted de-duplicated list.


## Usage

```
python autocomplete-spelunker.py [keyword] [char depth]
```

## Output

```
combs$ python autocomplete-spelunker.py dc 0
Running with keyword dc%20 and char depth 0 ... Run with params [keyword] [chardepth] to change
dc auto show
dc craigslist
dc dmv
dc improv
dc metro
dc metro map
dc metro trip planner
dc public library
dc restaurant week
dc weather

```

