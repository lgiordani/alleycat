# Alley Cat - a cat chasing simulation set in London

Alley Cat is a very simple simulation of a cat chase in London. The simulation starts with N owners and N cats starting in random positions, each turn both owners and cats can move, and when an owner finds their cat both are removed from the board.

The positions on the board are loaded from a JSON file of connections (a list of ('a', 'b') tuples that specify that node 'a' and node 'b' are linked), and both owners and cats move between those nodes. Cats move randomly, while owners try first a node they didn't yet visited if possible.

When an owner finds their cat the station (node) is closed and becomes unreachable from other nodes. It also becomes impossible to leave it, so other cats or owners that were in that station are trapped.

## Installation

This package is compatible with both Python 2 and Python 3

If you want to run the simulation

* Clone the repository
* Create a virtualenv and activate it
* Execute `pip install .`
* Run the `alleycat` script

If you want to run the test suite

* Clone the repository
* Create a virtualenv and activate it
* Execute `pip install -r requirements/testing.txt`
* Run `py.test -sv`
* Run `tox`

## Command line parameters

Typing `alleycat --help` one gets the following help

```sh
usage: alleycat [-h] [-c CONNECTIONS_FILE] [-s STATIONS_FILE] [-n NUM_CATS]
                [--closing-turns CLOSING_TURNS] [--max-turns MAX_TURNS]
                [--use-owner-names]

Simulates a cat chase in London

optional arguments:
  -h, --help            show this help message and exit
  -c CONNECTIONS_FILE, --connections-file CONNECTIONS_FILE
                        Connections file (JSON)
  -s STATIONS_FILE, --stations-file STATIONS_FILE
                        Stations file (JSON)
  -n NUM_CATS, --num-cats NUM_CATS
                        Number of cats (and owners) to spawn
  --closing-turns CLOSING_TURNS
                        Number of turns a station remains closed
  --max-turns MAX_TURNS
                        Maximum number of turns of the simulation
  --use-owner-names     Use names for owners instead of indexes
```

* CONNECTIONS_FILE is a JSON file containing connections between nodes (see the example file `tfl_connections.json` in the source code)
* STATIONS_FILE is an optional JSON file that maps station codes to names (see the example file `tfl_stations.json` in the source code)
* NUM_CATS is the number of cats and owners to spawn at the beginning of the simulation
* CLOSING_TURNS is the number of turns a station remains closed after an owner found their cat there. If not specified the stations remains closed until the simulation ends
* MAX_TURNS is the maximum number of turns of the simulation. If not specified the simulation lasts 100,000 turns.

The `--use-owner-names` makes use of the `Faker` package to create names for the spawned owners. If not specified owners are identified by their numerical index.

## Examples

This command line runs Alley Cat with the provided London tube map, spawning 200 cats (and relative owners) and lasts 100,000 turns (or until all cats have been found)

```sh
$ alleycat -c tfl_connections.json -s tfl_stations.json --num-cats 200
Turn      4 - Owner 190 found their cat! - Station Kennington is now closed
Turn      7 - Owner 52 found their cat! - Station Monument is now closed
Turn      9 - Owner 41 found their cat! - Station Temple is now closed
Turn     10 - Owner 121 found their cat! - Station Ealing Common is now closed
Turn     12 - Owner 77 found their cat! - Station Notting Hill Gate is now closed
Turn     12 - Owner 116 found their cat! - Station Bank is now closed
Turn     17 - Owner 23 found their cat! - Station Ruislip Gardens is now closed
Turn     28 - Owner 47 found their cat! - Station Mornington Crescent is now closed
Turn     38 - Owner 62 found their cat! - Station Holborn is now closed
Turn     62 - Owner 2 found their cat! - Station Mile End is now closed
Turn     73 - Owner 87 found their cat! - Station Manor House is now closed
Turn     81 - Owner 90 found their cat! - Station Baker Street is now closed
Turn     89 - Owner 151 found their cat! - Station Royal Oak is now closed
Turn     97 - Owner 129 found their cat! - Station Woodside Park is now closed
Turn     98 - Owner 163 found their cat! - Station Hounslow West is now closed
Turn    107 - Owner 53 found their cat! - Station Green Park is now closed
Turn    112 - Owner 44 found their cat! - Station Gloucester Road is now closed
Turn    114 - Owner 82 found their cat! - Station Whitechapel is now closed
Turn    119 - Owner 43 found their cat! - Station All Saints is now closed
Turn    127 - Owner 57 found their cat! - Station Rotherhithe is now closed
Turn    135 - Owner 198 found their cat! - Station Hammersmith is now closed
Turn    136 - Owner 183 found their cat! - Station Pimlico is now closed
Turn    142 - Owner 24 found their cat! - Station Canning Town is now closed
Turn    184 - Owner 36 found their cat! - Station Queensbury is now closed
Turn    198 - Owner 104 found their cat! - Station Liverpool Street is now closed
Turn    310 - Owner 7 found their cat! - Station Oxford Circus is now closed
Turn    311 - Owner 179 found their cat! - Station Goodge Street is now closed
Turn    386 - Owner 1 found their cat! - Station Mudchute is now closed
Turn    435 - Owner 105 found their cat! - Station Canary Wharf is now closed

##### SUMMARY #######

Total number of cats in play: 200
Total number of cats found: 29
Average number of movements required to find a cat: 119
Fastest owner 190 found the cat in 4 turns
Slowest owner 105 found the cat in 435 turns

Most visited stations:
  * Hounslow West had 499635 visits
  * Mansion House had 299980 visits
  * Woodside Park had 299838 visits
```

This command line runs Alley Cat with the example map, spawning 20 cats (and relative owners). It uses auto generated owner names and runs for maximum 1000 turns.

```sh
$ alleycat -c tfl_connections.json -s tfl_stations.json --num-cats 20 --use-owner-names --max-turns 1000
Turn    2 - Owner Bernie Smith found their cat! - Station Aldgate East is now closed
Turn   11 - Owner Selmer Klein found their cat! - Station Canada Water is now closed
Turn   97 - Owner Caiden Jones found their cat! - Station Hammersmith is now closed
Turn  113 - Owner Acie Oberbrunner found their cat! - Station Deptford Bridge is now closed

##### SUMMARY #######

Total number of cats in play: 20
Total number of cats found: 4
Average number of movements required to find a cat: 55
Fastest owner Bernie Smith found the cat in 2 turns
Slowest owner Acie Oberbrunner found the cat in 113 turns

Most visited stations:
  * Elverson Road had 898 visits
  * Lewisham had 891 visits
  * Kenton had 231 visits
```

This command line runs Alley Cat with the example map, spawning 200 cats (and relative owners). Closed stations will be opened again after 400 turns.

```sh
Turn      3 - Owner 83 found their cat! - Station Embankment is now closed
Turn      5 - Owner 4 found their cat! - Station Liverpool Street is now closed
Turn     12 - Owner 15 found their cat! - Station Acton Town is now closed
Turn     12 - Owner 187 found their cat! - Station Victoria is now closed
Turn     13 - Owner 113 found their cat! - Station East India is now closed
Turn     16 - Owner 0 found their cat! - Station Stockwell is now closed
Turn     61 - Owner 58 found their cat! - Station Holborn is now closed
Turn     62 - Owner 47 found their cat! - Station Prince Regent is now closed
Turn     71 - Owner 8 found their cat! - Station Finchley Road is now closed
Turn     77 - Owner 198 found their cat! - Station Kenton is now closed
Turn     78 - Owner 178 found their cat! - Station Baker Street is now closed
Turn     81 - Owner 73 found their cat! - Station Hammersmith is now closed
Turn     88 - Owner 157 found their cat! - Station Perivale is now closed
Turn     89 - Owner 125 found their cat! - Station Bank is now closed
Turn    101 - Owner 18 found their cat! - Station South Kensington is now closed
Turn    102 - Owner 141 found their cat! - Station East Ham is now closed
Turn    122 - Owner 158 found their cat! - Station North Ealing is now closed
Turn    136 - Owner 38 found their cat! - Station Highgate is now closed
Turn    140 - Owner 81 found their cat! - Station Picadilly Circus is now closed
Turn    157 - Owner 191 found their cat! - Station West Ham is now closed
Turn    187 - Owner 164 found their cat! - Station Hyde Park Corner is now closed
Turn    200 - Owner 12 found their cat! - Station Bermondsey is now closed
Turn    247 - Owner 16 found their cat! - Station King's Cross St. Pancras is now closed
Turn    277 - Owner 127 found their cat! - Station Lancaster Gate is now closed
Turn    280 - Owner 171 found their cat! - Station North Acton is now closed
Turn    284 - Owner 146 found their cat! - Station Waterloo is now closed
Turn    375 - Owner 3 found their cat! - Station Canning Town is now closed
Turn    404 - Station Embankment reopens clean and shiny
Turn    406 - Station Liverpool Street reopens clean and shiny
Turn    408 - Owner 186 found their cat! - Station Chalk Farm is now closed
[...]
Turn   7418 - Station King's Cross St. Pancras reopens clean and shiny
Turn   7711 - Owner 62 found their cat! - Station Notting Hill Gate is now closed
Turn   8112 - Station Notting Hill Gate reopens clean and shiny
Turn   9227 - Owner 115 found their cat! - Station Neasden is now closed

##### SUMMARY #######

Total number of cats in play: 200
Total number of cats found: 200
Average number of movements required to find a cat: 2203
Fastest owner 83 found the cat in 3 turns
Slowest owner 115 found the cat in 8850 turns

Most visited stations:
  * Chalfont & Latimer had 6575 visits
  * Moor Park had 4932 visits
  * Elverson Road had 4415 visits
```

## Internals

The program is divided into 3 main parts:

* Graph
* Actors
* Board

The simulation is based on a simple graph implemented in `alleycat/graph.py`. The graph does not store any information about the simulation or the players, it only a simple graph that stores nodes and connections. A feature of this graph is that nodes can be removed and restored: this is useful in the simulation when a node shall be considered closed.

Actors are just plain objects that know their current position and that can travel to a new one among a list of choices. The `Cat` class just subclasses `Actor`, while the `Human` class adds some custom rules to the movement since owners shall choose unvisited positions first. Every `Actor` knows its path, that is the list of visited positions: this is mandatory for owners but useful for other actors too, for example to allow metrics to be computed.

The `Board` class manages actors and the graph and encompasses the main structures used to run the simulation, which are mostly lists of `(owner, cat)` tuples.
