# wisper
Noita spell wisp and lifetime change calculator.
Uses BFS and garuntees best solutions, very fast for normal searches.

## usage

```
python ./main.py
```

when running, you will be prompted for `target: ` which is the lifetime delta, or the number of frames you want to change a spell's lifetime by. as an example: Spiral Shot has a lifetime of 100 frames. to make a Spiral Shot wisp, its lifetime needs to be set to -1, so the `target` delta should be `-101`. The `target` delta can also be a range in the form `min.max`, which is useful for spells that have a randomised lifetime, an example of this is Spark Bolt which has a lifetime of 40±7, so to find all wisp solutions you would input `-34.-48` you will then be prompted for `find: ` which is the number of different solutions you want to find 
