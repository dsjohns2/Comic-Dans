import fontforge
scale = .6

# create empty font
font = fontforge.font()

# set font names
font.fontname = "ComicDans"
font.fullname = "ComicDans"
font.familyname = "ComicDans"

# import svgs
for i in range(1, 97):
    # create a new glyph with the code point i
    glyph = font.createChar(i)

    # import svg file into it
    glyph.importOutlines("svg/%s.svg" %i)

    # make the glyph rest on the baseline
    ymin = glyph.boundingBox()[1]
    if(i in [34, 39, 42, 96]):
        glyph.transform([scale, 0, 0, scale, 0, ymin])
    else:
        glyph.transform([1, 0, 0, 1, 0, -ymin])

    # set glyph side bearings, can be any value or even 0
    glyph.left_side_bearing = glyph.right_side_bearing = 10

# import svgs
for i in range(97, 123):
    # create a new glyph with the code point i
    glyph = font.createChar(i)

    # import svg file into it
    glyph.importOutlines("svg/%s.svg" %i)

    # make the glyph rest on the baseline
    ymin = glyph.boundingBox()[1]
    if(i in [103, 112, 113, 121]):
        glyph.transform([scale, 0, 0, scale, 0, ymin])
    elif(i == 106):
        glyph.transform([scale*1.3, 0, 0, scale*1.3, 0, -1])
    elif(i == 109):
        glyph.transform([scale*1.5, 0, 0, scale*1.5, 0, -ymin+.2])
    elif(i in [98, 100, 104, 102, 116, 107, 108]):
        glyph.transform([scale*1.5, 0, 0, scale*1.5, 0, -ymin])
    elif(i in [117, 114]):
        glyph.transform([scale*.8, 0, 0, scale*.8, 0, -ymin])
    elif(i == 122):
        glyph.transform([scale, 0, 0, scale, 0, 0])
    else:
        glyph.transform([scale, 0, 0, scale, 0, -ymin])

    # set glyph side bearings, can be any value or even 0
    glyph.left_side_bearing = glyph.right_side_bearing = 10


# import svgs
for i in range(123, 256):
    # create a new glyph with the code point i
    glyph = font.createChar(i)

    # import svg file into it
    glyph.importOutlines("svg/%s.svg" %i)

    # make the glyph rest on the baseline
    ymin = glyph.boundingBox()[1]
    glyph.transform([1, 0, 0, 1, 0, -ymin])

    # set glyph side bearings, can be any value or even 0
    glyph.left_side_bearing = glyph.right_side_bearing = 10


font.generate("comicdans.pfb", flags=["tfm", "afm"]) # type1 with tfm/afm
font.generate("comicdans.otf") # opentype
font.generate("comicdans.ttf") # truetype
