# Advent of Code - Day 16

```mermaid
flowchart TD

AA[AA, 0] <--> DD[DD, 20]
AA <--> II[II, 0]
AA <--> BB[BB, 13]
BB <--> CC[CC, 2]
CC <--> DD
DD <--> EE[EE, 3]
EE <--> FF[FF, 0]
FF <--> GG[GG, 0]
GG <--> HH[HH, 22]
II <--> JJ
```


Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II





## Part One

TODO: Content

## Part Two

TODO: Content

