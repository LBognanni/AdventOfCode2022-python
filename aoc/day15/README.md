# Advent of Code - Day 15

OMG this took forever.

(!!SPOILER!!) Hints:
 - Because the distance is in Manhattan geometry, the area observed by a sensor is in a diamond shape - not a circle
 - Because it's a diamond shape, it's quite easy to find a sensor's range leftmost and rightmost `X` values at coordinate `Y`

## Part One

The tricky part here was just excluding the beacons from the observed line

## Part Two

The naive approach was to:
- cycle through every point in the grid
- for each point, find if it's contained in a sensor's range
- if it's not, bingo!
- This however means cycling through 4million x 4million coordinates, which unsurprisingly takes much longer than it's practical to wait for

The revised approach was:
 - Cycle through the 4 million Y coordinates
 - figure out the "free" X value, if any at line Y
    - this is done by merging the "ranges" of each sensor's area at that line, and picking every x value not in the merged ranges

Because we're still cycling through 4 million Y values, the run time was still longer than I would have liked. There might be a better way to do this :thinking:

