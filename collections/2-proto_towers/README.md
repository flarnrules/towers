

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

4. Then you run the following in the command line: `for i in {66..75}; do cp template.json "$i.json"; done` and you will get 10 freshly created <number.json> files.
![Alt text](image.png). I'm so used to obsidian, i actually have no idea how real markdown works.

I need to do some research so these docs don't suck ass.

Anyways

5. If the command was configured correctly, you'll have 10 new metadata files, you still need to *manually* go in and change each "name" to the correct <Proto Tower Number> which is a pain. This could be fixed with a bit more automation in that script above, but at this time it feels easier to just manually go and change the names than to use my brain to figure out how to code that automation into the script. The funny Thing I find about software development is that... I don't have the basics down, so doing something as simple as adding another, slightly more complex `for` loop in the above BASH script is actually a huge and annoying task. a chore, rather than a mere inconvenience like flipping a light switch... I digress.

Anyways, after you get all of the metadata files with the correct "name" inside each JSON, you are ready for the next step.

6. Draw 10 8x8 towers. Just do whatever you want, as long as it is a tower. with 8x8 there's really not a whole lot of real estate, so it's kind of interesting the amount of restriction you have means it's super easy to just, draw a simple tower in 5 seconds. The tower needs a background pattern. so far ive only used the `sun` background pattern, but it's possible more patterns could emerge. for blitz'z it's best to not think about it, as that takes time.

6a --> this is an overlooked step. not the drawing itself, but the necessary setup. need to have access to a computer or a phone with pixel art software. thankfully MS Paint is a perfectly passable raster graphics software, but Aesprite is my personal favorite. If I have access to Aesprite and a drawing pad, I can create the coolest shit. Anyways, to get set up, you need to copy an aesprite file with an 8x8 canvas size 10 times to save time transition from 1 drawing to the next. this will increase the chances of entering into a flow state, and *generating* some really interesting art.

6b --> I need to write a script that does this for me. Should be relatively simple to do. I'll use a crane (🏗️) emoji to indicate things that need to be built: 🏗️. If you are a new developer or just reading through this, quick tip about emojis... if you are on windows you can access the emoji menu with: `windows key + .` -> that's Windows Key and Period at the same time. It's quite remarkable, having the emoji menu right at your fingertips. Just like... hundreds of well designed tiny representations of important concepts. emojis are actually pretty cool come to think of it... anyways... 🏗️ for good measure, this would be really helpful. and save a lot of tedium.




