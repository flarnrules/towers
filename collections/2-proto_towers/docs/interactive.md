# how to make the interactive nfts
first, need to create an image with a map of where the character can exist.
I'm using the color blue to represent where the character can exist.

## simple approach
This is the only implementation I have discovered I can get working so far:
1. the character can move forward or backward through a sequence of positions.
2. the space where the character moves is colored blue (0,0, 255)
3. create a folder with a png file with the path identified in blue.
4. run `python3 generate_collision_map.py` from `towers/collections/2-proto_towers` after updating file names correctly.
5. go into the newly created json and replace all 1s with the sequence the character should move in.
    - this can eventually be replaced with the A* pathfinding algorithm that works, I can't get this working yet.
6. 