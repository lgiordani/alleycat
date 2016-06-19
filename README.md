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

When the simulation ends some metrics of the execution are printed.

## Internals

The program is divided into 3 main parts:

* Graph
* Actors
* Board

The simulation is based on a simple graph implemented in `alleycat/graph.py`. The graph does not store any information about the simulation or the players, it only a simple graph that stores nodes and connections. A feature of this graph is that nodes can be removed and restored: this is useful in the simulation when a node shall be considered closed.

Actors are just plain objects that know their current position and that can travel to a new one among a list of choices. The `Cat` class just subclasses `Actor`, while the `Human` class adds some custom rules to the movement since owners shall choose unvisited positions first. Every `Actor` knows its path, that is the list of visited positions: this is mandatory for owners but useful for other actors too, for example to allow metrics to be computed.

The `Board` class manages actors and the graph and encompasses the main structures used to run the simulation, which are mostly lists of `(owner, cat)` tuples.
