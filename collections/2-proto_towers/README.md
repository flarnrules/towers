

#################
# PROTO TOWERS ##
#################

This is proto towers. a multimedia collection of proto towers, minted as IPFS links and metadata hosted on the Stargaze blockchain.

Proto towers is important, because it is the beginning.

>Proto ~ < insert definition here >

>Tower ~ < insert definition here >

What do we have in this directory right now?
Hey how do I use Obsidian to make this work better...

This is an exercise in learning how to develop little ways to automate the boring stuff.

And just... get right into the interesting stuff.
But sometimes *building* the tools to get there is more interesting than the origin *or* destination.

########################
# DIRECTORY STRUCTURE ##
########################

Structure works like this.

The repo name is Towers, there are 4 subdirectories.

1. collections
2. media
3. utilities
4. web_stuff

I only really know what's in collections and utilities right now. I've basically forgotten what's inside web_stuff entirely, and media probably has some original drawings or generated pieces of art for the main collection. 

Speaking of that... I should probably also use those pieces as Proto Towers, as long as I know for sure they aren't gonna be minted in the main collection, or modify them in some way. This could make it easy to mint one on a day where perhaps I'm too busy to do a bunch of art, I could just run some special command and it mints from a big pile of old concept art at random. That would be really cool.

#################################
# types of deployment
#################################

Standard - i mint and list 5 towers, all of the same dimensions, and sometimes following similar thematic elements. the decision for what to do currently is literally whatever comes to my head first. i could eventually standardize this process a bit, like demonstrate certain holidays or special occasions result in topically significant choices in the designs. That would be really cool. (only type as of proto tower 65.)

8x8 Blitz - i mint and list 10 towers, all of them 8x8 dimensions. the metadata is typically copied from previous blitz'z and basically there's only 64 squares to work with so it's kind of challenging to draw anything of substance. (never been done)

others - to be determined

blitz steps:

1. First, you need to be in the `towers/collections/2-proto_towers/metadata` directory.

2. Then, you need to navigate to `template.json` and make changes based on the base template you want.

3. Then once you feel ready, you need to know the starting id number and ending id number for the nfts you are going to drop.

4. Then you run the following in the command line: `for i in {66..75}; do cp template.json "$i.json; done` and you will get 10 freshly created <number.json> files.
