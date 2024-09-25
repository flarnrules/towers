# towers
a multimedia collection of towers with multiple artists

## current workflow

1. Draw towers in the same notebook until the notebook is filled to the brim with towers.
2. Get other people to draw towers in this notebook as well. Options: guest_artist, collaboration, guest_collaboration
3. Develop clean workflow from tower -> normalized image that is indistiguishably part of the overall collection.
4. The tower itself is an object. other pieces in the collection can have one of the towers as a trait.
5. There is a sort of heirarchy where the actual drawings of towers can have multiple variants that are descendents of the tower itself.

Draw tower or towers on page n
Scan page n
Create metadata for creation of contents of page n, (I should be writing this information down in pencil on the back of each page). I think I'll print out a little label for each page, where I can write in pen on a sticker or something.

traits to capture on the page itself:

```
{
"artists_names":" #string
    {
    "artist_name" : "person1"
    "artist_name" : "person2"
    "artist_name" : "person3"
    }
"date created": "2023-09-17" #integer
"page number": "7" #integer
"tower_number_begin": "12" #integer
"tower_number_end" : "13" #integer
"medium": "ink" #string
"tools": "Lamy Safari, red" #string
}
```

That's probably enough for now. Don't want to go too crazy.
Some observations:
- when `tower_number_begin` is the same as `tower_number_end`, both the `page` JSON object and the `tower` JSON object are said to be, have the trait of `prime`

I just need to keep building up these traits and encode them on the JSON object. Since this project is deployed after all of the art is created, the JSON object can just gradually add features as I learn more stuff.

For example, the JSON object that is generated *at mint time* will all be generated *at mint time* by the smart contract governing the minting of the nft. That means that each piece of art is generated with truly unique and spontaneous features.

One of the traits of this JSON object, which probably needs a good name... for now we will use `genesis`. No that doesnt work.. maybe `spark_of_life` no that's pretty weird, these are towers. I think `blueprint` works for now, because it's an architectural tool so it kinda matches with the theme.

What traits are in the `blueprint` JSON so far... none. What do I want to create:
- a glyph of of the full-scale drawing, that is a 100x100 pixel art version of the drawing itself.
- a bunch of interesting metadata about the drawing that is saved as a png. file that generates the original drawing's stats, like the color palette and other cool stuff. Could include pre/post processing stats too.


### Preprocessing
the images need to be scanned in, which from my scanner right now it's generating a pdf.
I wonder if taking a picture with my dslr would be better, or scanner better?
I also wonder if it's possible to scan in as a more compatible file format.
Either way, we follow these steps:

1. Raw scan goes into `towers/media/raw`
2. Pre-processed png: run `pdf_to_page_png.py` and these pages go into `towers/media/raw_formatted`
3. Preprocessing step: run `preprocessing.py` and these pages go into `towers/media/preprocessed`
4. Segment towers into individual pngs: run `select_towers.py` and these images are placed in `towers/media/thumbnails`

*here's where I'm stuck* - I'm not sure what to do next. Do I do a manual pass and try to clean up some of the images by erasing stuff via MS Paint?
That would be a fairly time consuming effort. Also, I'm wondering if the thumbnails serve as the starting point, the original image type.
Then I post-process those further into svgs and other stuff. I need a way to get metadata on all of these images, I think I'll need
to manually do that for a lot of the meta data in the original image type. There's 115 pages, and on average probably 3-4 per page.
My guess is that the book will have 500 towers. Then I should be able to generate svgs from close to 400 of them, and then create pngs
from those svgs from the best ones, maybe about 100 or so. These 100 would form the basis of the component that relies on the hashlips art engine
to generate a whole bunch of variations.

5. 