# wisper
Noita spell wisp and lifetime change calculator.
Uses BFS and garuntees best solutions, very fast for normal searches.

## usage

```
python ./main.py
```

when running, you will be prompted for `target: ` which is the lifetime delta, or the number of frames you want to change a spell's lifetime by. as an example: Spiral Shot has a lifetime of 100 frames. to make a Spiral Shot wisp, its lifetime needs to be set to -1, so the `target` delta should be `-101`. you will then be prompted for `find: ` which is the number of different solutions you want to find 
