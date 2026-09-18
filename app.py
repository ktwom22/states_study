from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Complete dataset with concrete visual memory clues for learning differences
STATES = [
    {"name": "Alabama", "hint": "A flat-top building with a tiny heel at the bottom left.", "capital": "Montgomery"},
    {"name": "Alaska", "hint": "The Giant Whale swimming with a tail of island dots!", "capital": "Juneau"},
    {"name": "Arizona", "hint": "A box with a steep playground slide on the bottom-left.", "capital": "Phoenix"},
    {"name": "Arkansas", "hint": "A pair of shorts or pants right above the boot!", "capital": "Little Rock"},
    {"name": "California", "hint": "A long, curved banana hugging the ocean edge.", "capital": "Sacramento"},
    {"name": "Colorado", "hint": "A clean, smooth building brick (flat on all 4 sides).", "capital": "Denver"},
    {"name": "Connecticut", "hint": "A small puzzle block with a tiny square notch in the roof.",
     "capital": "Hartford"},
    {"name": "Delaware", "hint": "A skinny number 1 or vertical pencil with a rounded top.", "capital": "Dover"},
    {"name": "Florida", "hint": "A water pistol or a diving board splashing down.", "capital": "Tallahassee"},
    {"name": "Georgia", "hint": "A round, fuzzy peach with a jagged beach on the right.", "capital": "Atlanta"},
    {"name": "Hawaii", "hint": "A necklace of separate bead-islands floating in a line.", "capital": "Honolulu"},
    {"name": "Idaho", "hint": "A tall winter snow-boot or ice skate facing left.", "capital": "Boise"},
    {"name": "Illinois", "hint": "A tall yellow ear of corn pointing down to a round point.", "capital": "Springfield"},
    {"name": "Indiana", "hint": "A tall block with a scoop missing from its left shoulder.", "capital": "Indianapolis"},
    {"name": "Iowa", "hint": "A round face/cookie with a human nose sticking out the side!", "capital": "Des Moines"},
    {"name": "Kansas", "hint": "A flat box with a mouse bite chewed out of the top-right corner.", "capital": "Topeka"},
    {"name": "Kentucky", "hint": "A crispy fried chicken drumstick (bone points right!).", "capital": "Frankfort"},
    {"name": "Louisiana", "hint": "The capital letter 'L' or a fancy high-heeled boot.", "capital": "Baton Rouge"},
    {"name": "Maine", "hint": "A heavy mitten pointing straight up toward Canada.", "capital": "Augusta"},
    {"name": "Maryland", "hint": "A squiggly crab with two claws cut by water in the middle.", "capital": "Annapolis"},
    {"name": "Massachusetts", "hint": "A strong arm flexing a muscle (Cape Cod is the fist!).", "capital": "Boston"},
    {"name": "Michigan", "hint": "The Winter Mitten with a bunny jumping over the top.", "capital": "Lansing"},
    {"name": "Minnesota", "hint": "A puffy white Chef's Hat with a little pom-pom at the top.", "capital": "St. Paul"},
    {"name": "Mississippi", "hint": "A guitar neck standing tall with a wavy river on the left.", "capital": "Jackson"},
    {"name": "Missouri", "hint": "A block shirt with a little square button sticking out the bottom.",
     "capital": "Jefferson City"},
    {"name": "Montana", "hint": "Look at the left edge: it's a person's face (forehead, nose, and chin) looking east.",
     "capital": "Helena"},
    {"name": "Nebraska", "hint": "A wide box with a shelf or handle sticking out of the top left.",
     "capital": "Lincoln"},
    {"name": "Nevada", "hint": "An upside-down pyramid with a sharp, slanted slide on the left.",
     "capital": "Carson City"},
    {"name": "New Hampshire", "hint": "An upside-down party hat (wide bottom, pointy top).", "capital": "Concord"},
    {"name": "New Jersey", "hint": "A curvy peanut or wiggly caterpillar standing up.", "capital": "Trenton"},
    {"name": "New Mexico", "hint": "A square block with a tiny Lego step cut out on the bottom.",
     "capital": "Santa Fe"},
    {"name": "New York", "hint": "A triangle bird with a long fish-tail (Long Island) on the right.",
     "capital": "Albany"},
    {"name": "North Carolina", "hint": "A long, flat surfboard pointing out into the ocean.", "capital": "Raleigh"},
    {"name": "North Dakota", "hint": "A smooth flat roof along Canada with a wiggly river on the right.",
     "capital": "Bismarck"},
    {"name": "Ohio", "hint": "A round superhero shield or police officer badge.", "capital": "Columbus"},
    {"name": "Oklahoma", "hint": "A cooking frying pan with a long handle pointing left.", "capital": "Oklahoma City"},
    {"name": "Oregon", "hint": "A sturdy treasure chest with a wavy river lid.", "capital": "Salem"},
    {"name": "Pennsylvania", "hint": "A flat stone brick with a tiny chimney touching the lake.",
     "capital": "Harrisburg"},
    {"name": "Rhode Island", "hint": "The baby state! The tiny piece with a bite out of the center.",
     "capital": "Providence"},
    {"name": "South Carolina", "hint": "A folding paper fan or slice of pie pointing down.", "capital": "Columbia"},
    {"name": "South Dakota", "hint": "A flat box with a wavy river line drawn down the middle.", "capital": "Pierre"},
    {"name": "Tennessee", "hint": "A long, skinny picnic bench or skateboard.", "capital": "Nashville"},
    {"name": "Texas", "hint": "The big giant! A giant cowboy shape with arms spreading wide.", "capital": "Austin"},
    {"name": "Utah", "hint": "A square with a giant bite/step missing from the top-right corner.",
     "capital": "Salt Lake City"},
    {"name": "Vermont", "hint": "Shaped like the letter 'V' for Vermont! (Wide top, pointy bottom).",
     "capital": "Montpelier"},
    {"name": "Virginia", "hint": "A flying bird or arrowhead pointing to the left.", "capital": "Richmond"},
    {"name": "Washington", "hint": "A postage stamp with a ripped-off top-left corner.", "capital": "Olympia"},
    {"name": "West Virginia", "hint": "A crushed letter 'W' or a flying tree frog.", "capital": "Charleston"},
    {"name": "Wisconsin", "hint": "A big mitt or badger head surrounded by water.", "capital": "Madison"},
    {"name": "Wyoming", "hint": "The simplest box on the map (sits on top of Colorado).", "capital": "Cheyenne"}
]


@app.route('/')
def single_mode():
    return render_template('index.html')


@app.route('/map')
def map_mode():
    return render_template('map_mode.html')


@app.route('/api/question')
def get_question():
    correct = random.choice(STATES)
    distractors = random.sample([s for s in STATES if s['name'] != correct['name']], 3)
    options = [correct['name']] + [d['name'] for d in distractors]
    random.shuffle(options)

    return jsonify({
        "name": correct['name'],
        "hint": correct['hint'],
        "capital": correct['capital'],
        "options": options
    })


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port)