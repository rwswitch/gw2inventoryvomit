# gw2inventoryvomit
This gets a dump of your guild wars 2 inventory. 
There are existing, way better tools out there. I didn't build them, though. 

Add your api key and hope I didn't break it recently. Currently only jams together a list. 

The idea was:
Grab the full inventory
Map the set of items to characters
Using the set, grab the item information, too. Uniqueness is built into set mechanics.
Figure out wherever I left the glob of globby goo


Now that I've typed this out, I have a way better idea of what I'll ultimately do if/when I pick this up again.

a) Store character + inventory information in sql(sqlite) tables
b) index map items to characters
c) download a set of data relating to items, store
d) set searches/indexes appropriate to the stuff you're looking for
e) refine data in second set for inventories

TODO: The following are appropriate additional broken down scripts:
1) Download/Refresh character and storage data (and store)
2) reMap stored data (probably something sql can just do already; index against item code; store item set
3) take stored/mapped set (assess if present) get extended item data information, store extended item information
4) make a search to make life easier
5) implement restful api :^^)

