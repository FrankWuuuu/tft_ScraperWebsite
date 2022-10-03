# from Program.Scraper import bunnymuffins
# from Scraper import *
from calendar import c
import json

print()
print()
print()
print()
print()
print()

tftacticsDatabase = [
    [
        {
            "carry": ["Xayah", "Shyvana"],
            "units": [
                "Ashe",
                "Gnar",
                "Swain",
                "Hecarim",
                "Neeko",
                {"Xayah": ["Giant Slayer", "Guinsoo's Rageblade", "Infinity Edge"]},
                {"Shyvana": ["Archangel's Staff", "Ionic Spark", "Morellonomicon"]},
            ],
            "threeStars": [],
        },
        {
            "carry": ["Shi Oh Yu"],
            "units": [
                "Gnar",
                {"Anivia": ["Morellonomicon"]},
                "Lulu",
                {"Neeko": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                {"Shi Oh Yu": ["Bloodthirster", "Titan's Resolve"]},
                "Bard",
                "Yasuo",
            ],
            "threeStars": [],
        },
        {
            "carry": ["Daeja"],
            "units": [
                "Sejuani",
                "Lillia",
                "Yone",
                {"Nunu": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                "Hecarim",
                {"Daeja": ["Archangel's Staff", "Giant Slayer", "Guinsoo's Rageblade"]},
                "Yasuo",
            ],
            "threeStars": [],
        },
        {
            "carry": ["Ao Shin"],
            "units": [
                "Heimerdinger",
                "Lulu",
                {"Sylas": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                "Ornn",
                "Bard",
                "Zoe",
                {
                    "Ao Shin": [
                        "Archangel's Staff",
                        "Hextech Gunblade",
                        "Spear of Shojin",
                    ]
                },
            ],
            "threeStars": [],
        },
        {
            "carry": ["Sona", "Syfen"],
            "units": [
                "Heimerdinger",
                "Tristana",
                "Lulu",
                {"Sylas": ["Gargoyle Stoneplate", "Sunfire Cape"]},
                {"Sona": ["Morellonomicon", "Spear of Shojin"]},
                {"Syfen": ["Bloodthirster", "Titan's Resolve"]},
                "Zoe",
            ],
            "threeStars": [],
        },
    ],
    [
        {
            "carry": ["Olaf"],
            "units": [
                "Shen",
                "Qiyana",
                {"Diana": ["Frozen Heart", "Ionic Spark", "Sunfire Cape"]},
                "Sylas",
                {"Olaf": ["Assassin Emblem", "Infinity Edge", "Rapid Firecannon"]},
                "Ornn",
                "Pyke",
            ],
            "threeStars": ["Diana", "Olaf"],
        },
        {
            "carry": ["Aurelion Sol"],
            "units": [
                "Heimerdinger",
                "Lulu",
                {"Sylas": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                "Ornn",
                "Bard",
                "Zoe",
                {
                    "Aurelion Sol": [
                        "Archangel's Staff",
                        "Mage Emblem",
                        "Spear of Shojin",
                    ]
                },
            ],
            "threeStars": [],
        },
        {
            "carry": ["Varus"],
            "units": [
                "Nami",
                "Qiyana",
                "Twitch",
                {"Varus": ["Deathblade", "Guinsoo's Rageblade", "Runaan's Hurricane"]},
                {"Illaoi": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                "Ornn",
                "Talon",
                "Bard",
            ],
            "threeStars": ["Nami", "Varus", "Illaoi"],
        },
        {
            "carry": ["Aurelion Sol"],
            "units": [
                "Heimerdinger",
                "Vladimir",
                "Nami",
                {"Illaoi": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                "Lulu",
                "Sylas",
                {
                    "Aurelion Sol": [
                        "Archangel's Staff",
                        "Mage Emblem",
                        "Spear of Shojin",
                    ]
                },
            ],
            "threeStars": ["Vladimir", "Nami", "Illaoi"],
        },
        {
            "carry": ["Varus"],
            "units": [
                "Ezreal",
                "Skarner",
                "Shen",
                "Twitch",
                {"Varus": ["Deathblade", "Guinsoo's Rageblade", "Runaan's Hurricane"]},
                {"Illaoi": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                "Ornn",
                "Xayah",
            ],
            "threeStars": ["Skarner", "Varus", "Illaoi"],
        },
        {
            "carry": ["Yone", "Olaf"],
            "units": [
                "Qiyana",
                {"Yone": ["Bloodthirster", "Guinsoo's Rageblade", "Quicksilver"]},
                "Shen",
                "Diana",
                {"Olaf": ["Bloodthirster", "Guinsoo's Rageblade", "Quicksilver"]},
                "Sylas",
                "Ornn",
                "Yasuo",
            ],
            "threeStars": ["Yone", "Olaf"],
        },
        {
            "carry": ["Daeja"],
            "units": [
                {"Daeja": ["Archangel's Staff", "Giant Slayer", "Guinsoo's Rageblade"]},
                "Shi Oh Yu",
                {"Idas": ["Dragon's Claw", "Gargoyle Stoneplate", "Sunfire Cape"]},
                "Bard",
                "Yasuo",
            ],
            "threeStars": [],
        },
        {
            "carry": ["Anivia", "Volibear"],
            "units": [
                "Karma",
                "Ashe",
                {"Anivia": ["Archangel's Staff", "Morellonomicon", "Spear of Shojin"]},
                "Lee Sin",
                "Swain",
                {"Volibear": ["Bloodthirster", "Guinsoo's Rageblade", "Quicksilver"]},
                "Ornn",
                "Yasuo",
            ],
            "threeStars": ["Anivia", "Volibear"],
        },
        {
            "carry": ["Ryze"],
            "units": [
                "Sejuani",
                "Lillia",
                "Nami",
                {"Ryze": ["Archangel's Staff", "Hextech Gunblade", "Spear of Shojin"]},
                {"Sylas": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                "Hecarim",
                "Bard",
                "Zoe",
            ],
            "threeStars": ["Ryze", "Sylas"],
        },
        {
            "carry": ["Nidalee"],
            "units": [
                {"Nidalee": ["Deathblade", "Guinsoo's Rageblade", "Quicksilver"]},
                "Gnar",
                "Elise",
                "Swain",
                {"Neeko": ["Dragon's Claw", "Sunfire Cape", "Warmog's Armor"]},
                "Soraka",
                "Shyvana",
            ],
            "threeStars": ["Nidalee"],
        },
        {
            "carry": ["Ezreal"],
            "units": [
                {"Ezreal": ["Blue Buff", "Infinity Edge", "Jeweled Gauntlet"]},
                "Karma",
                {"Leona": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                "Taric",
                "Ashe",
                "Lee Sin",
                "Shi Oh Yu",
            ],
            "threeStars": ["Ezreal", "Karma", "Leona", "Taric"],
        },
        {
            "carry": ["Sett", "Shyvana"],
            "units": [
                "Senna",
                {"Sett": ["Deathblade", "Guinsoo's Rageblade", "Quicksilver"]},
                "Shen",
                "Swain",
                "Hecarim",
                "Xayah",
                {"Shyvana": ["Archangel's Staff", "Ionic Spark", "Morellonomicon"]},
            ],
            "threeStars": ["Senna", "Sett"],
        },
        {
            "carry": ["Talon", "Xayah"],
            "units": [
                "Sejuani",
                "Qiyana",
                "Shen",
                "Twitch",
                "Hecarim",
                "Ornn",
                {"Talon": ["Bloodthirster", "Giant Slayer", "Infinity Edge"]},
                {"Xayah": ["Giant Slayer", "Guinsoo's Rageblade", "Quicksilver"]},
            ],
            "threeStars": [],
        },
        {
            "carry": ["Swain", "Shyvana"],
            "units": [
                "Senna",
                "Sett",
                "Shen",
                {"Swain": ["Guinsoo's Rageblade", "Quicksilver", "Statikk Shiv"]},
                "Hecarim",
                "Xayah",
                "Yasuo",
                {"Shyvana": ["Archangel's Staff", "Ionic Spark", "Morellonomicon"]},
            ],
            "threeStars": [],
        },
        {
            "carry": ["Corki"],
            "units": [
                "Tristana",
                "Lulu",
                {"Corki": ["Giant Slayer", "Guinsoo's Rageblade", "Hand of Justice"]},
                {"Neeko": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                "Sona",
                "Bard",
                "Shyvana",
            ],
            "threeStars": [],
        },
        {
            "carry": ["Sona", "Daeja"],
            "units": [
                "Tahm Kench",
                "Jinx",
                "Corki",
                {"Ornn": ["Gargoyle Stoneplate"]},
                {"Sona": ["Morellonomicon", "Spear of Shojin"]},
                {"Daeja": ["Giant Slayer", "Guinsoo's Rageblade", "Revel Emblem"]},
                "Yasuo",
            ],
            "threeStars": [],
        },
        {
            "carry": ["Olaf"],
            "units": [
                "Braum",
                "Lillia",
                "Shen",
                {"Diana": ["Frozen Heart", "Ionic Spark", "Sunfire Cape"]},
                {"Olaf": ["Bloodthirster", "Guinsoo's Rageblade", "Quicksilver"]},
                "Sylas",
                "Ornn",
                "Pyke",
            ],
            "threeStars": ["Diana", "Olaf"],
        },
        {
            "carry": ["Syfen"],
            "units": [
                "Qiyana",
                "Shen",
                "Elise",
                "Sylas",
                {"Ornn": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                {"Syfen": ["Bloodthirster", "Quicksilver", "Titan's Resolve"]},
                "Pyke",
            ],
            "threeStars": [],
        },
    ],
    [
        {
            "carry": ["Yone"],
            "units": [
                "Shen",
                {"Yone": ["Bloodthirster", "Guinsoo's Rageblade", "Quicksilver"]},
                {"Nunu": ["Gargoyle Stoneplate", "Sunfire Cape", "Warmog's Armor"]},
                "Olaf",
                "Hecarim",
                "Daeja",
                "Yasuo",
            ],
            "threeStars": ["Yone", "Nunu"],
        }
    ],
    [],
    [],
]

f = open('tftactics.json')
tftacticsDatabase = json.load(f)

tftacticsLength = 0
for thing in tftacticsDatabase:
    tftacticsLength += len(thing)
tftacticsTierOfEachCarry= {}
for i in range (len(tftacticsDatabase)-1, -1, -1):
    for comp in tftacticsDatabase[i]:
        for carry in comp['carry']:
            
            tftacticsTierOfEachCarry[carry] = i



lolchessdatabase= [
    {
        "carry": ["Corki", "Sona", "Shyvana"],
        "units": [
            "Tristana",
            "Lulu",
            {"Corki": ["Giant Slayer", "Guinsoo's Rageblade", "Last Whisper"]},
            {"Neeko": ["Gargoyle Stoneplate", "Warmog's Armor", "Bramble Vest"]},
            {"Sona": ["Spear of Shojin", "Morellonomicon"]},
            "Bard",
            {"Shyvana": ["Infinity Edge", "Jeweled Gauntlet", "Hand of Justice"]},
        ],
    },
    {
        "carry": ["Yasuo", "Ao Shin"],
        "units": [
            "Heimerdinger",
            "Lulu",
            {"Sylas": ["Zz'Rot Portal"]},
            {"Ornn": ["Warmog's Armor", "Sunfire Cape", "Gargoyle Stoneplate"]},
            "Bard",
            {"Yasuo": ["Titan’s Resolve", "Bloodthirster", "Blue Buff"]},
            {"Zoe": ["Spear of Shojin"]},
            {"Ao Shin": ["Spear of Shojin", "Giant Slayer", "Archangel's Staff"]},
        ],
    },
    {
        "carry": ["Corki", "Sy'fen"],
        "units": [
            "Heimerdinger",
            "Tristana",
            {"Lulu": ["Chalice of Power", "Chalice of Power", "Zeke's Herald"]},
            {"Sylas": ["Gargoyle Stoneplate", "Warmog's Armor", "Sunfire Cape"]},
            {"Corki": ["Giant Slayer", "Guinsoo's Rageblade", "Spear of Shojin"]},
            "Sona",
            "Zoe",
            {"Sy'fen": ["Bloodthirster", "Titan’s Resolve", "Quicksilver"]},
        ],
    },
    {
        "carry": ["Anivia", "Yasuo", "Shi Oh Yu"],
        "units": [
            "Gnar",
            {"Anivia": ["Morellonomicon", "Archangel's Staff", "Spear of Shojin"]},
            "Lulu",
            {"Neeko": ["Warmog's Armor", "Gargoyle Stoneplate", "Bramble Vest"]},
            "Bard",
            {"Yasuo": ["Titan’s Resolve", "Hand of Justice", "Giant Slayer"]},
            {"Shi Oh Yu": ["Titan’s Resolve", "Bloodthirster", "Edge of Night"]},
        ],
    },
    {
        "carry": ["Xayah", "Shyvana"],
        "units": [
            "Ashe",
            "Gnar",
            "Swain",
            "Hecarim",
            {"Neeko": ["Gargoyle Stoneplate", "Warmog's Armor", "Sunfire Cape"]},
            {"Xayah": ["Giant Slayer", "Guinsoo's Rageblade", "Quicksilver"]},
            "Yasuo",
            {"Shyvana": ["Titan’s Resolve", "Bloodthirster", "Archangel's Staff"]},
        ],
    },
    {
        "carry": ["Yasuo", "Daeja"],
        "units": [
            "Sejuani",
            "Lillia",
            "Yone",
            {"Nunu": ["Sunfire Cape", "Warmog's Armor", "Ionic Spark"]},
            "Hecarim",
            {"Yasuo": ["Cavalier Emblem", "Titan’s Resolve", "Bloodthirster"]},
            {"Daeja": ["Giant Slayer", "Archangel's Staff", "Guinsoo's Rageblade"]},
        ],
    },
    {
        "carry": ["Olaf", "Talon"],
        "units": [
            "Qiyana",
            "Shen",
            {"Diana": ["Sunfire Cape", "Frozen Heart", "Ionic Spark"]},
            {"Olaf": ["Assassin Emblem", "Infinity Edge", "Rapid Firecannon"]},
            "Sylas",
            "Ornn",
            {"Talon": ["Infinity Edge", "Giant Slayer", "Hand of Justice"]},
            "Pyke",
        ],
    },
    {
        "carry": ["Talon", "Xayah"],
        "units": [
            "Sejuani",
            "Qiyana",
            "Shen",
            "Twitch",
            {"Hecarim": ["Bramble Vest", "Sunfire Cape", "Warmog's Armor"]},
            "Ornn",
            {"Talon": ["Infinity Edge", "Hand of Justice", "Giant Slayer"]},
            {"Xayah": ["Giant Slayer", "Guinsoo's Rageblade", "Quicksilver"]},
            "Bard",
        ],
    },
    {
        "carry": ["Corki", "Daeja"],
        "units": [
            "Tahm Kench",
            {"Jinx": ["Statikk Shiv"]},
            "Lee Sin",
            {"Corki": ["Giant Slayer", "Infinity Edge", "Last Whisper"]},
            {"Ornn": ["Sunfire Cape", "Gargoyle Stoneplate", "Warmog's Armor"]},
            "Sona",
            {"Yasuo": ["Thief's Gloves"]},
            {"Daeja": ["Guinsoo's Rageblade", "Revel Emblem", "Quicksilver"]},
        ],
    },
    {
        "carry": ["Corki", "Sona"],
        "units": [
            "Jinx",
            "Thresh",
            {"Tristana": ["Banshee’s Claw"]},
            "Lulu",
            {"Corki": ["Giant Slayer", "Last Whisper", "Guinsoo's Rageblade"]},
            {"Sona": ["Spear of Shojin", "Morellonomicon"]},
            "Bard",
            {"Idas": ["Gargoyle Stoneplate", "Dragon's Claw", "Warmog's Armor"]},
        ],
    },
    {
        "carry": ["Varus", "Talon"],
        "units": [
            "Nami",
            "Qiyana",
            "Twitch",
            {"Illaoi": ["Sunfire Cape", "Warmog's Armor", "Gargoyle Stoneplate"]},
            {"Varus": ["Guinsoo's Rageblade", "Giant Slayer", "Runaan's Hurricane"]},
            {"Ornn": ["Zz'Rot Portal"]},
            {"Talon": ["Infinity Edge", "Hand of Justice", "Edge of Night"]},
            "Bard",
        ],
    },
    {
        "carry": ["Aurelion Sol"],
        "units": [
            "Heimerdinger",
            {"Vladimir": ["Zz'Rot Portal"]},
            {"Nami": ["Spear of Shojin"]},
            {"Illaoi": ["Zz'Rot Portal"]},
            "Lulu",
            {"Sylas": ["Warmog's Armor", "Gargoyle Stoneplate", "Ionic Spark"]},
            {"Zoe": ["Spear of Shojin"]},
            {"Aurelion Sol": ["Giant Slayer", "Hextech Gunblade", "Archangel's Staff"]},
        ],
    },
    {
        "carry": ["Yasuo", "Sy'fen"],
        "units": [
            {"Qiyana": ["Frozen Heart"]},
            "Shen",
            "Thresh",
            {"Sylas": ["Zeke's Herald", "Zeke's Herald"]},
            {"Ornn": ["Sunfire Cape", "Redemption"]},
            "Pyke",
            {"Yasuo": ["Titan’s Resolve", "Infinity Edge", "Hand of Justice"]},
            {"Sy'fen": ["Titan’s Resolve", "Bloodthirster", "Quicksilver"]},
        ],
    },
    {
        "carry": ["Elise", "Sy'fen"],
        "units": [
            "Taric",
            "Thresh",
            {"Elise": ["Bloodthirster", "Guinsoo's Rageblade", "Quicksilver"]},
            "Sylas",
            {"Neeko": ["Bramble Vest", "Sunfire Cape", "Gargoyle Stoneplate"]},
            "Soraka",
            {"Sy'fen": ["Titan’s Resolve", "Bloodthirster", "Frozen Heart"]},
        ],
    },
    {
        "carry": ["Anivia", "Volibear"],
        "units": [
            "Karma",
            "Sett",
            "Ashe",
            {"Anivia": ["Morellonomicon", "Archangel's Staff", "Hextech Gunblade"]},
            "Lee Sin",
            "Swain",
            {"Volibear": ["Guinsoo's Rageblade", "Bloodthirster", "Quicksilver"]},
            {"Ornn": ["Warmog's Armor", "Bramble Vest", "Sunfire Cape"]},
        ],
    },
    {
        "carry": ["Sett", "Xayah"],
        "units": [
            {"Sett": ["Giant Slayer", "Guinsoo's Rageblade", "Quicksilver"]},
            "Kayn",
            "Shen",
            "Swain",
            "Hecarim",
            {"Xayah": ["Giant Slayer", "Last Whisper", "Guinsoo's Rageblade"]},
            {"Shyvana": ["Bramble Vest", "Warmog's Armor", "Dragon's Claw"]},
        ],
    },
    {
        "carry": ["Elise", "Talon", "Sy'fen"],
        "units": [
            "Nami",
            {"Elise": ["Bloodthirster", "Guinsoo's Rageblade", "Quicksilver"]},
            "Sylas",
            {"Neeko": ["Bramble Vest", "Sunfire Cape"]},
            {"Talon": ["Infinity Edge", "Hand of Justice", "Giant Slayer"]},
            "Pyke",
            "Zoe",
            {"Sy'fen": ["Titan’s Resolve", "Bloodthirster", "Quicksilver"]},
        ],
    },
    {
        "carry": ["Yasuo", "Aurelion Sol"],
        "units": [
            "Heimerdinger",
            "Lulu",
            {"Sylas": ["Warmog's Armor", "Gargoyle Stoneplate", "Ionic Spark"]},
            "Ornn",
            "Bard",
            {"Yasuo": ["Titan’s Resolve", "Warmog's Armor", "Hand of Justice"]},
            {"Zoe": ["Spear of Shojin"]},
            {"Aurelion Sol": ["Giant Slayer", "Archangel's Staff", "Hextech Gunblade"]},
        ],
    },
    {
        "carry": ["Tristana"],
        "units": [
            "Senna",
            {"Braum": ["Dragon's Claw", "Bramble Vest", "Warmog's Armor"]},
            {"Jinx": ["Banshee’s Claw", "Statikk Shiv"]},
            "Thresh",
            {"Tristana": ["Deathblade", "Guinsoo's Rageblade", "Giant Slayer"]},
            "Lulu",
            "Corki",
            {"Sona": ["Morellonomicon"]},
            "Bard",
        ],
    },
    {
        "carry": ["Xayah", "Yasuo"],
        "units": [
            "Aatrox",
            {"Kayn": ["Frozen Heart"]},
            "Swain",
            {"Volibear": ["Needlessly Big Gem"]},
            {"Xayah": ["Giant Slayer", "Guinsoo's Rageblade", "Draven's Axe"]},
            {"Yasuo": ["Diamond Hands", "Bloodthirster", "Titan’s Resolve"]},
            {"Zoe": ["Spear of Shojin"]},
            {"Idas": ["Sunfire Cape", "Gargoyle Stoneplate", "Mogul's Mail"]},
        ],
    },
]

f = open('lolchess.json')
lolchessdatabase = json.load(f)

lolchessLength = len(lolchessdatabase)
lolchessTierOfEachCarry= {}
for i in range (len(lolchessdatabase)-1, -1, -1):
    comp = lolchessdatabase[i]
    for carry in comp['carry']:
        lolchessTierOfEachCarry[carry] = i



bunnymuffinsdatabase=[
    [
        {
            "carry": ["Ao Shin"],
            "units": [
                {"Heimerdinger": []},
                {"Sylas": []},
                {"Lulu": []},
                {"Ornn": []},
                {"Bard": []},
                {"Zoe": []},
                {
                    "Ao Shin": [
                        "Spear of Shojin",
                        "Archangel's Staff",
                        "Hextech Gunblade",
                    ]
                },
            ],
        },
        {
            "carry": ["Daeja"],
            "units": [
                {"Yone": []},
                {"Nunu": ["Warmog's Armor", "Redemption"]},
                {"Lulu": []},
                {"Hecarim": []},
                {"Daeja": ["Hextech Gunblade", "Quicksilver", "Guinsoo's Rageblade"]},
                {"Yasuo": []},
                {"Bard": []},
            ],
        },
    ],
    [
        {
            "carry": ["Corki", "Sy'fen"],
            "units": [
                {"Tristana": []},
                {"Sylas": ["Warmog's Armor"]},
                {"Lulu": []},
                {"Sona": ["Morellonomicon"]},
                {"Corki": ["Guinsoo's Rageblade", "Giant Slayer", "Hand of Justice"]},
                {"Sy'fen": ["Bloodthirster", "Quicksilver"]},
                {"Bard": []},
            ],
        },
        {
            "carry": ["Corki"],
            "units": [
                {"Jinx": []},
                {"Tristana": []},
                {"Lulu": []},
                {"Sona": []},
                {"Corki": ["Infinity Edge", "Deathblade", "Last Whisper"]},
                {"Idas": ["Gargoyle Stoneplate", "Dragon's Claw", "Sunfire Cape"]},
                {"Bard": []},
            ],
        },
        {
            "carry": ["Anivia", "Shi Oh Yu"],
            "units": [
                {"Lulu": []},
                {"Anivia": ["Morellonomicon", "Spear of Shojin"]},
                {"Neeko": ["Warmog's Armor", "Gargoyle Stoneplate"]},
                {"Shi Oh Yu": ["Titan’s Resolve", "Bloodthirster", "Giant Slayer"]},
                {"Bard": []},
                {"Soraka": []},
            ],
        },
        {
            "carry": ["Shyvana"],
            "units": [
                {"Gnar": []},
                {"Ashe": []},
                {"Swain": []},
                {"Neeko": ["Warmog's Armor"]},
                {"Hecarim": []},
                {"Xayah": ["Guinsoo's Rageblade"]},
                {"Shyvana": ["Frozen Heart", "Ionic Spark", "Jeweled Gauntlet"]},
            ],
        },
        {
            "carry": ["Aurelion Sol"],
            "units": [
                {"Vladimir": []},
                {"Heimerdinger": []},
                {"Nami": []},
                {"Sylas": ["Ionic Spark", "Warmog's Armor"]},
                {"Illaoi": []},
                {"Lulu": []},
                {
                    "Aurelion Sol": [
                        "Mage Emblem",
                        "Archangel's Staff",
                        "Hextech Gunblade",
                    ]
                },
            ],
        },
    ],
    [
        {
            "carry": ["Varus"],
            "units": [
                {"Skarner": []},
                {"Ezreal": []},
                {"Shen": []},
                {"Twitch": []},
                {"Illaoi": ["Bramble Vest", "Dragon's Claw", "Warmog's Armor"]},
                {"Varus": ["Deathblade", "Guinsoo's Rageblade", "Runaan's Hurricane"]},
                {"Ornn": []},
                {"Xayah": []},
            ],
        },
        {
            "carry": ["Elise", "Sy'fen"],
            "units": [
                {"Shen": []},
                {"Thresh": []},
                {"Sylas": []},
                {"Elise": ["Bloodthirster", "Guinsoo's Rageblade", "Quicksilver"]},
                {"Ornn": ["Gargoyle Stoneplate", "Sunfire Cape"]},
                {"Sy'fen": ["Bloodthirster", "Titan’s Resolve", "Quicksilver"]},
            ],
        },
        {
            "carry": ["Olaf", "Diana"],
            "units": [
                {"Shen": []},
                {"Braum": []},
                {"Lillia": []},
                {"Sylas": []},
                {"Olaf": ["Guinsoo's Rageblade", "Quicksilver", "Titan’s Resolve"]},
                {"Diana": ["Infinity Edge", "Titan’s Resolve", "Frozen Heart"]},
                {"Ornn": []},
                {"Pyke": []},
            ],
        },
        {
            "carry": ["Sy'fen"],
            "units": [
                {"Heimerdinger": []},
                {"Sylas": ["Gargoyle Stoneplate", "Dragon's Claw"]},
                {"Lulu": []},
                {"Sona": ["Morellonomicon"]},
                {"Sy'fen": ["Bloodthirster", "Titan’s Resolve", "Quicksilver"]},
                {"Zoe": []},
                {"Bard": []},
            ],
        },
        {
            "carry": ["Xayah"],
            "units": [
                {"Sejuani": []},
                {"Qiyana": ["Frozen Heart"]},
                {"Shen": []},
                {"Twitch": []},
                {"Hecarim": ["Sunfire Cape", "Warmog's Armor"]},
                {"Ornn": []},
                {"Talon": ["Infinity Edge"]},
                {"Xayah": ["Guinsoo's Rageblade", "Quicksilver", "Giant Slayer"]},
            ],
        },
        {
            "carry": ["Xayah"],
            "units": [
                {"Shen": []},
                {"Ashe": []},
                {"Neeko": []},
                {"Hecarim": []},
                {"Xayah": ["Guinsoo's Rageblade", "Deathblade", "Giant Slayer"]},
                {"Soraka": []},
                {"Shyvana": ["Frozen Heart", "Warmog's Armor", "Titan’s Resolve"]},
            ],
        },
        {
            "carry": ["Volibear", "Yasuo"],
            "units": [
                {"Karma": ["Chalice of Power", "Zeke's Herald"]},
                {"Ashe": []},
                {"Volibear": ["Guinsoo's Rageblade", "Quicksilver", "Bloodthirster"]},
                {"Lee Sin": []},
                {"Swain": []},
                {"Anivia": []},
                {"Ornn": []},
                {"Yasuo": ["Titan’s Resolve", "Hand of Justice"]},
            ],
        },
        {
            "carry": ["Volibear", "Yasuo"],
            "units": [
                {"Sejuani": []},
                {"Nunu": []},
                {"Volibear": ["Guinsoo's Rageblade", "Quicksilver", "Bloodthirster"]},
                {"Lee Sin": []},
                {"Anivia": ["Morellonomicon"]},
                {"Ornn": ["Gargoyle Stoneplate"]},
                {"Hecarim": []},
                {"Yasuo": ["Titan’s Resolve", "Hand of Justice"]},
            ],
        },
        {
            "carry": ["Yone"],
            "units": [
                {"Leona": ["Warmog's Armor", "Redemption"]},
                {"Taric": []},
                {"Braum": []},
                {"Thresh": []},
                {"Yone": ["Guinsoo's Rageblade", "Quicksilver", "Hand of Justice"]},
                {"Daeja": []},
                {"Yasuo": ["Titan’s Resolve"]},
            ],
        },
        {
            "carry": ["Swain", "Yasuo"],
            "units": [
                {"Sett": []},
                {"Karma": []},
                {"Shen": []},
                {"Ashe": []},
                {"Lee Sin": []},
                {"Swain": ["Quicksilver", "Guinsoo's Rageblade", "Archangel's Staff"]},
                {"Neeko": ["Warmog's Armor"]},
                {"Yasuo": ["Titan’s Resolve", "Hand of Justice"]},
            ],
        },
    ],
    [
        {
            "carry": ["Tristana"],
            "units": [
                {
                    "Tahm Kench": [
                        "Dragon's Claw",
                        "Gargoyle Stoneplate",
                        "Gargoyle Stoneplate",
                    ]
                },
                {"Tristana": ["Hand of Justice", "Guinsoo's Rageblade"]},
                {"Jinx": ["Zeke's Herald", "Zeke's Herald"]},
                {"Lulu": []},
                {"Sona": []},
                {"Corki": []},
            ],
        },
        {
            "carry": ["Sett"],
            "units": [
                {"Sett": ["Quicksilver", "Guinsoo's Rageblade", "Titan’s Resolve"]},
                {"Senna": []},
                {"Shen": ["Redemption"]},
                {"Swain": []},
                {"Hecarim": []},
                {"Xayah": []},
                {"Shyvana": ["Frozen Heart", "Warmog's Armor"]},
            ],
        },
        {
            "carry": ["Nami"],
            "units": [
                {"Heimerdinger": []},
                {"Nami": ["Spear of Shojin", "Spear of Shojin", "Archangel's Staff"]},
                {"Sylas": ["Dragon's Claw", "Bramble Vest", "Ionic Spark"]},
                {"Illaoi": []},
                {"Lulu": []},
                {"Ryze": []},
                {"Zoe": []},
                {"Bard": []},
            ],
        },
        {
            "carry": ["Nidalee"],
            "units": [
                {"Nidalee": ["Guinsoo's Rageblade", "Titan’s Resolve", "Deathblade"]},
                {"Gnar": []},
                {"Elise": []},
                {"Swain": []},
                {"Neeko": ["Warmog's Armor"]},
                {"Soraka": []},
                {"Shyvana": ["Warmog's Armor", "Frozen Heart"]},
            ],
        },
        {
            "carry": ["Ezreal"],
            "units": [
                {"Taric": []},
                {"Leona": ["Bramble Vest", "Sunfire Cape", "Warmog's Armor"]},
                {"Karma": []},
                {"Ezreal": ["Hextech Gunblade", "Archangel's Staff", "Blue Buff"]},
                {"Braum": []},
                {"Thresh": []},
                {"Ashe": []},
                {"Ornn": []},
            ],
        },
        {
            "carry": ["Lee Sin", "Yasuo"],
            "units": [
                {"Karma": []},
                {"Ashe": []},
                {"Lee Sin": ["Jeweled Gauntlet", "Bloodthirster", "Infinity Edge"]},
                {"Swain": []},
                {"Volibear": []},
                {"Neeko": ["Warmog's Armor"]},
                {"Ornn": []},
                {"Yasuo": ["Titan’s Resolve", "Hand of Justice"]},
            ],
        },
        {
            "carry": ["Kayn"],
            "units": [
                {"Shen": ["Warmog's Armor"]},
                {"Kayn": ["Infinity Edge", "Deathblade", "Bloodthirster"]},
                {"Qiyana": ["Frozen Heart"]},
                {"Hecarim": []},
                {"Ornn": []},
                {"Talon": ["Infinity Edge"]},
                {"Pyke": ["Infinity Edge"]},
            ],
        },
        {
            "carry": ["Diana"],
            "units": [
                {"Braum": []},
                {"Lillia": []},
                {"Qiyana": ["Zeke's Herald"]},
                {"Olaf": []},
                {"Diana": ["Ionic Spark", "Infinity Edge", "Titan’s Resolve"]},
                {"Ornn": []},
                {"Talon": ["Infinity Edge"]},
                {"Pyke": []},
            ],
        },
    ],
]

f = open('bunnymuffins.json')
bunnymuffinsdatabase = json.load(f)

bunnymuffinsLength = 0
for thing in bunnymuffinsdatabase:
    bunnymuffinsLength += len(thing)
bunnymuffinsTierOfEachCarry= {}
for i in range (len(bunnymuffinsdatabase)-1, -1, -1):
    for comp in bunnymuffinsdatabase[i]:
        for carry in comp['carry']:
            
            bunnymuffinsTierOfEachCarry[carry] = i





def lolchessToBunnymuffins(n):
    n = n * bunnymuffinsLength / lolchessLength
    currentTier = 0
    while n >= 0:
        n -=  len(bunnymuffinsdatabase[currentTier])
        currentTier +=1
    
    return currentTier-1

def tftacticsToBunnymuffins(n):
    if n == 0:
        return .5
    elif n == 1 :
        return 2.5
    else:
        return 3

for carry in tftacticsTierOfEachCarry:
    tftacticsTierOfEachCarry[carry] = tftacticsToBunnymuffins(tftacticsTierOfEachCarry[carry])
for carry in lolchessTierOfEachCarry:
    lolchessTierOfEachCarry[carry] = lolchessToBunnymuffins(lolchessTierOfEachCarry[carry])

print(tftacticsTierOfEachCarry)
print()
print(lolchessTierOfEachCarry)
print()
print(bunnymuffinsTierOfEachCarry)
print()
print()
print()


arrCombinedTierOfEachCarry = {}
for carry in bunnymuffinsTierOfEachCarry:
    carryIsInDatabase  = 3
    print(carry, end=': ')
    try: 
        ThistftacticsTierOfCarry= tftacticsTierOfEachCarry[carry]
    except:
        # print( carry + " isnt in tftactics", end = '   ')
        ThistftacticsTierOfCarry = 0
        carryIsInDatabase-=1

    try: 
        ThislolchessTierOfCarry= lolchessTierOfEachCarry[carry]
    except:
        # print( carry + " isnt in lolchess", end = '   ')
        ThislolchessTierOfCarry = 0
        carryIsInDatabase-=1

    combine = bunnymuffinsTierOfEachCarry[carry] + ThistftacticsTierOfCarry + ThislolchessTierOfCarry
    combine/= carryIsInDatabase

    # print(ThistftacticsTierOfCarry, end = ' + ')
    # print(ThislolchessTierOfCarry, end = ' + ')
    # print(bunnymuffinsTierOfEachCarry[carry], end = ' = ')
    # print(combine)
    

    arrCombinedTierOfEachCarry[carry]= combine

print()

for carry in tftacticsTierOfEachCarry:
    carryIsInDatabase  = 3
    print(carry, end=': ')
    try: 
        ThisBunnyMuffinsTierOfCarry= bunnymuffinsTierOfEachCarry[carry]
    except:
        # print( carry + " isnt in tftactics", end = '   ')
        ThisBunnyMuffinsTierOfCarry = 0
        carryIsInDatabase-=1

    try: 
        ThislolchessTierOfCarry= lolchessTierOfEachCarry[carry]
    except:
        # print( carry + " isnt in lolchess", end = '   ')
        ThislolchessTierOfCarry = 0
        carryIsInDatabase-=1

    combine = ThisBunnyMuffinsTierOfCarry + tftacticsTierOfEachCarry[carry] + ThislolchessTierOfCarry
    combine/= carryIsInDatabase
    arrCombinedTierOfEachCarry[carry]= combine


    # print(ThisBunnyMuffinsTierOfCarry, end = ' + ')
    # print(ThislolchessTierOfCarry, end = ' + ')
    # print(tftacticsTierOfEachCarry[carry], end = ' = ')
    # print(combine)

for carry in lolchessTierOfEachCarry:
    carryIsInDatabase  = 3
    print(carry, end=': ')
    try: 
        ThistftacticsTierOfCarry= tftacticsTierOfEachCarry[carry]
    except:
        # print( carry + " isnt in tftactics", end = '   ')
        ThistftacticsTierOfCarry = 0
        carryIsInDatabase-=1

    try: 
        ThisBunnyMuffinsTierOfCarry= bunnymuffinsTierOfEachCarry[carry]
    except:
        # print( carry + " isnt in tftactics", end = '   ')
        ThisBunnyMuffinsTierOfCarry = 0
        carryIsInDatabase-=1

    combine = ThistftacticsTierOfCarry + lolchessTierOfEachCarry[carry] +  ThisBunnyMuffinsTierOfCarry
    combine/= carryIsInDatabase


    

    arrCombinedTierOfEachCarry[carry]= combine

    print(ThistftacticsTierOfCarry, end = ' + ')
    print(ThisBunnyMuffinsTierOfCarry, end = ' + ')
    print(lolchessTierOfEachCarry[carry], end = ' = ')
    print(combine, end = "  (")
    print(carryIsInDatabase, end = ")")
    print()

    




dict1 = arrCombinedTierOfEachCarry
sorted_values = sorted(dict1.values()) # Sort the values
sorted_dict = {}
for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]

print()
print()
print()

print(sorted_dict)




def fixnames (unitName):
    unitName =unitName.replace(" ", "")
    unitName = unitName.replace("'", "")
    unitName = unitName.replace("TyrantSwain", "Swain")
    return unitName



carryAndTheirComps = {}
for carry in sorted_dict:
    compsWithCarry = []
    for tier in tftacticsDatabase:
        for comp in tier:
            for carry2 in comp["carry"]:
                if carry == carry2:
                    compsWithCarry.append(comp)

    for comp in lolchessdatabase:
        for carry2 in comp["carry"]:
            if carry == carry2:
                compsWithCarry.append(comp)
    carryAndTheirComps[fixnames(carry)] = compsWithCarry

    for tier in bunnymuffinsdatabase:
        for comp in tier:
            for carry2 in comp["carry"]:
                if carry == carry2:
                    compsWithCarry.append(comp)




# carryAndTheirCompsString = json.dumps(carryAndTheirComps)
# print(fixnames(carryAndTheirCompsString))


print()
print()
print()
print()
print()
print()
print()
print()

json_object = json.dumps(carryAndTheirComps, indent=4)
with open("summary.json", "w") as outfile:
    outfile.write(json_object)

# print(carryAndTheirComps)
print()

print()
print()
print()
print()
print()

