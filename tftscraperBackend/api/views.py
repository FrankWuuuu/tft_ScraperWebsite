from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
  # return JsonResponse('cumcum', safe=False)
  person = {'name': 'joey'}
  lolchess = {
    "Yasuo": [
        {
            "carry": [
                "Yasuo",
                "Daeja"
            ],
            "units": [
                "Leona",
                "Sejuani",
                "Nunu",
                "Rakan",
                "Hecarim",
                "Bard",
                "Yasuo",
                "Daeja"
            ],
            "items": [
                {
                    "Leona": [
                        "Sunfire Cape"
                    ]
                },
                {
                    "Nunu": [
                        "Warmog's Armor",
                        "Ionic Spark",
                        "Redemption"
                    ]
                },
                {
                    "Yasuo": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Blue Buff"
                    ]
                },
                {
                    "Daeja": [
                        "Giant Slayer",
                        "Archangel's Staff",
                        "Guinsoo's Rageblade"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Kai'sa",
                "Lee Sin",
                "Yasuo"
            ],
            "units": [
                "Karma",
                "Sejuani",
                "Sett",
                "Kai'sa",
                "Qiyana",
                "Lee Sin",
                "Volibear",
                "Hecarim",
                "Yasuo"
            ],
            "items": [
                {
                    "Kai'sa": [
                        "Morellonomicon",
                        "Statikk Shiv"
                    ]
                },
                {
                    "Lee Sin": [
                        "Infinity Edge",
                        "Jeweled Gauntlet",
                        "Bloodthirster"
                    ]
                },
                {
                    "Hecarim": [
                        "Protector's Vow"
                    ]
                },
                {
                    "Yasuo": [
                        "Titan\u2019s Resolve",
                        "Infinity Edge",
                        "Bloodthirster"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Yasuo",
                "Shi Oh Yu"
            ],
            "units": [
                "Karma",
                "Rakan",
                "Seraphine",
                "Soraka",
                "Yasuo",
                "Idas",
                "Shi Oh Yu"
            ],
            "items": [
                {
                    "Yasuo": [
                        "Titan\u2019s Resolve",
                        "Blue Buff",
                        "Bloodthirster"
                    ]
                },
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Redemption"
                    ]
                },
                {
                    "Shi Oh Yu": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Guinsoo's Rageblade"
                    ]
                }
            ]
        }
    ],
    "Aphelios": [
        {
            "carry": [
                "Aphelios"
            ],
            "units": [
                "Senna",
                "Aphelios",
                "Rell",
                "Rell",
                "Tristana",
                "Zeri",
                "Nomsy",
                "Graves"
            ],
            "threeStars": [],
            "items": [
                {
                    "Senna": [
                        "Zeke's Herald"
                    ]
                },
                {
                    "Aphelios": [
                        "Infinity Edge",
                        "Last Whisper"
                    ]
                },
                {
                    "Rell": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Aphelios",
                "Graves"
            ],
            "units": [
                "Sejuani",
                "Senna",
                "Aphelios",
                "Qiyana",
                "Rell",
                "Rengar",
                "Zeri",
                "Graves",
                "Hecarim"
            ],
            "items": [
                {
                    "Senna": [
                        "Zeke's Herald"
                    ]
                },
                {
                    "Aphelios": [
                        "Last Whisper",
                        "Infinity Edge"
                    ]
                },
                {
                    "Rell": [
                        "Protector's Vow",
                        "Sunfire Cape"
                    ]
                },
                {
                    "Zeri": [
                        "Darkflight Emblem"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Giant Slayer"
                    ]
                },
                {
                    "Hecarim": [
                        "Gargoyle Stoneplate"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Aphelios",
                "Graves"
            ],
            "units": [
                "Sejuani",
                "Rell",
                "Aphelios",
                "Aphelios",
                "Rell",
                "Zeri",
                "Graves",
                "Hecarim"
            ],
            "items": [
                {
                    "Sejuani": [
                        "Zeke's Herald"
                    ]
                },
                {
                    "Aphelios": [
                        "Runaan's Hurricane",
                        "Last Whisper"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster",
                        "Infinity Edge",
                        "Titan\u2019s Resolve"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Aphelios",
                "Graves"
            ],
            "units": [
                "Sejuani",
                "Senna",
                "Rell",
                "Aphelios",
                "Nunu",
                "Zeri",
                "Hecarim",
                "Graves"
            ],
            "items": [
                {
                    "Sejuani": [
                        "Zz'Rot Portal"
                    ]
                },
                {
                    "Rell": [
                        "Protector's Vow",
                        "Sunfire Cape"
                    ]
                },
                {
                    "Aphelios": [
                        "Guinsoo's Rageblade",
                        "Runaan's Hurricane",
                        "Deathblade"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster",
                        "Guinsoo's Rageblade",
                        "Titan\u2019s Resolve"
                    ]
                }
            ]
        }
    ],
    "Xayah": [
        {
            "carry": [
                "Xayah",
                "Shyvana"
            ],
            "units": [
                "Sejuani",
                "Twitch",
                "Rakan",
                "Jayce",
                "Xayah",
                "Hecarim",
                "Shyvana"
            ],
            "threeStars": [],
            "items": [
                {
                    "Xayah": [
                        "Giant Slayer",
                        "Guinsoo's Rageblade",
                        "Infinity Edge"
                    ]
                },
                {
                    "Shyvana": [
                        "Archangel's Staff",
                        "Ionic Spark",
                        "Morellonomicon"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Xayah",
                "Shyvana"
            ],
            "units": [
                "Sejuani",
                "Twitch",
                "Rakan",
                "Hecarim",
                "Jayce",
                "Xayah",
                "Bard",
                "Shyvana"
            ],
            "items": [
                {
                    "Hecarim": [
                        "Sunfire Cape"
                    ]
                },
                {
                    "Jayce": [
                        "Gargoyle Stoneplate",
                        "Titan\u2019s Resolve",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Xayah": [
                        "Giant Slayer",
                        "Guinsoo's Rageblade",
                        "Infinity Edge"
                    ]
                },
                {
                    "Shyvana": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Archangel's Staff"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Xayah",
                "Shyvana"
            ],
            "units": [
                "Sejuani",
                "Twitch",
                "Rakan",
                "Jayce",
                "Xayah",
                "Hecarim",
                "Bard",
                "Shyvana"
            ],
            "items": [
                {
                    "Jayce": [
                        "Warmog's Armor",
                        "Titan\u2019s Resolve",
                        "Bramble Vest"
                    ]
                },
                {
                    "Xayah": [
                        "Infinity Edge",
                        "Giant Slayer",
                        "Quicksilver"
                    ]
                },
                {
                    "Shyvana": [
                        "Ionic Spark",
                        "Morellonomicon",
                        "Archangel's Staff"
                    ]
                }
            ]
        }
    ],
    "Shyvana": [
        {
            "carry": [
                "Ao Shin",
                "Shyvana"
            ],
            "units": [
                "Rakan",
                "Idas",
                "Ao Shin",
                "Shyvana",
                "Terra"
            ],
            "threeStars": [],
            "items": [
                {
                    "Ao Shin": [
                        "Hextech Gunblade",
                        "Spear of Shojin"
                    ]
                },
                {
                    "Shyvana": [
                        "Ionic Spark",
                        "Morellonomicon"
                    ]
                },
                {
                    "Terra": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Xayah",
                "Shyvana"
            ],
            "units": [
                "Sejuani",
                "Twitch",
                "Rakan",
                "Jayce",
                "Xayah",
                "Hecarim",
                "Shyvana"
            ],
            "threeStars": [],
            "items": [
                {
                    "Xayah": [
                        "Giant Slayer",
                        "Guinsoo's Rageblade",
                        "Infinity Edge"
                    ]
                },
                {
                    "Shyvana": [
                        "Archangel's Staff",
                        "Ionic Spark",
                        "Morellonomicon"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Xayah",
                "Shyvana"
            ],
            "units": [
                "Sejuani",
                "Twitch",
                "Rakan",
                "Hecarim",
                "Jayce",
                "Xayah",
                "Bard",
                "Shyvana"
            ],
            "items": [
                {
                    "Hecarim": [
                        "Sunfire Cape"
                    ]
                },
                {
                    "Jayce": [
                        "Gargoyle Stoneplate",
                        "Titan\u2019s Resolve",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Xayah": [
                        "Giant Slayer",
                        "Guinsoo's Rageblade",
                        "Infinity Edge"
                    ]
                },
                {
                    "Shyvana": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Archangel's Staff"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Ao Shin",
                "Shyvana"
            ],
            "units": [
                "Rakan",
                "Graves",
                "Idas",
                "Ao Shin",
                "Shyvana",
                "Terra"
            ],
            "items": [
                {
                    "Idas": [
                        "Mogul's Mail"
                    ]
                },
                {
                    "Ao Shin": [
                        "Spear of Shojin",
                        "Archangel's Staff",
                        "Hextech Gunblade"
                    ]
                },
                {
                    "Shyvana": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Archangel's Staff"
                    ]
                },
                {
                    "Terra": [
                        "Gargoyle Stoneplate",
                        "Protector's Vow",
                        "Dragon's Claw"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Jayce",
                "Shi Oh Yu",
                "Shyvana"
            ],
            "units": [
                "Kai'sa",
                "Zac",
                "Rakan",
                "Seraphine",
                "Jayce",
                "Shi Oh Yu",
                "Shyvana"
            ],
            "items": [
                {
                    "Jayce": [
                        "Infinity Edge",
                        "Jeweled Gauntlet",
                        "Hand of Justice"
                    ]
                },
                {
                    "Shi Oh Yu": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Guinsoo's Rageblade"
                    ]
                },
                {
                    "Shyvana": [
                        "Titan\u2019s Resolve",
                        "Archangel's Staff",
                        "Morellonomicon"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Xayah",
                "Shyvana"
            ],
            "units": [
                "Sejuani",
                "Twitch",
                "Rakan",
                "Jayce",
                "Xayah",
                "Hecarim",
                "Bard",
                "Shyvana"
            ],
            "items": [
                {
                    "Jayce": [
                        "Warmog's Armor",
                        "Titan\u2019s Resolve",
                        "Bramble Vest"
                    ]
                },
                {
                    "Xayah": [
                        "Infinity Edge",
                        "Giant Slayer",
                        "Quicksilver"
                    ]
                },
                {
                    "Shyvana": [
                        "Ionic Spark",
                        "Morellonomicon",
                        "Archangel's Staff"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Ao Shin",
                "Shyvana"
            ],
            "units": [
                "Rakan",
                "Idas",
                "Terra",
                "Ao Shin",
                "Shyvana"
            ],
            "items": [
                {
                    "Rakan": [
                        "Zeke's Herald"
                    ]
                },
                {
                    "Idas": [
                        "Redemption",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Terra": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Dragon's Claw"
                    ]
                },
                {
                    "Ao Shin": [
                        "Hextech Gunblade",
                        "Spear of Shojin",
                        "Archangel's Staff"
                    ]
                },
                {
                    "Shyvana": [
                        "Morellonomicon",
                        "Ionic Spark"
                    ]
                }
            ]
        }
    ],
    "Diana": [
        {
            "carry": [
                "Diana",
                "Olaf"
            ],
            "units": [
                "Braum",
                "Lillia",
                "Diana",
                "Olaf",
                "Sylas",
                "Hecarim",
                "Nilah",
                "Pantheon"
            ],
            "threeStars": [
                "Diana",
                "Olaf"
            ],
            "items": [
                {
                    "Diana": [
                        "Hand of Justice",
                        "Ionic Spark",
                        "Sunfire Cape"
                    ]
                },
                {
                    "Olaf": [
                        "Bloodthirster",
                        "Giant Slayer",
                        "Runaan's Hurricane"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Diana",
                "Olaf",
                "Nilah",
                "Pantheon"
            ],
            "units": [
                "Braum",
                "Lillia",
                "Diana",
                "Olaf",
                "Rakan",
                "Sylas",
                "Nilah",
                "Pantheon",
                "Bard"
            ],
            "items": [
                {
                    "Diana": [
                        "Sunfire Cape",
                        "Ionic Spark",
                        "Hand of Justice"
                    ]
                },
                {
                    "Olaf": [
                        "Infinity Edge",
                        "Runaan's Hurricane",
                        "Bloodthirster"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Giant Slayer"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Warmog's Armor"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Diana",
                "Olaf",
                "Nilah"
            ],
            "units": [
                "Braum",
                "Lillia",
                "Qiyana",
                "Diana",
                "Olaf",
                "Sylas",
                "Nilah",
                "Pantheon"
            ],
            "items": [
                {
                    "Qiyana": [
                        "Zeke's Herald",
                        "Zeke's Herald"
                    ]
                },
                {
                    "Diana": [
                        "Sunfire Cape",
                        "Ionic Spark",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Olaf": [
                        "Infinity Edge",
                        "Runaan's Hurricane",
                        "Assassin Emblem"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Giant Slayer"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Diana",
                "Rengar",
                "Nilah"
            ],
            "units": [
                "Aphelios",
                "Qiyana",
                "Rell",
                "Diana",
                "Rengar",
                "Nilah",
                "Tyrant Swain"
            ],
            "items": [
                {
                    "Qiyana": [
                        "Zeke's Herald"
                    ]
                },
                {
                    "Diana": [
                        "Ionic Spark",
                        "Hand of Justice",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Rengar": [
                        "Infinity Edge",
                        "Bloodthirster"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Giant Slayer",
                        "Hand of Justice"
                    ]
                },
                {
                    "Tyrant Swain": [
                        "Gargoyle Stoneplate",
                        "Morellonomicon"
                    ]
                }
            ]
        }
    ],
    "Olaf": [
        {
            "carry": [
                "Diana",
                "Olaf"
            ],
            "units": [
                "Braum",
                "Lillia",
                "Diana",
                "Olaf",
                "Sylas",
                "Hecarim",
                "Nilah",
                "Pantheon"
            ],
            "threeStars": [
                "Diana",
                "Olaf"
            ],
            "items": [
                {
                    "Diana": [
                        "Hand of Justice",
                        "Ionic Spark",
                        "Sunfire Cape"
                    ]
                },
                {
                    "Olaf": [
                        "Bloodthirster",
                        "Giant Slayer",
                        "Runaan's Hurricane"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Olaf",
                "Pantheon"
            ],
            "units": [
                "Lillia",
                "Yone",
                "Olaf",
                "Sylas",
                "Hecarim",
                "Pantheon",
                "Yasuo",
                "Zoe"
            ],
            "threeStars": [
                "Olaf"
            ],
            "items": [
                {
                    "Olaf": [
                        "Bloodthirster",
                        "Giant Slayer",
                        "Runaan's Hurricane"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Giant Slayer",
                        "Titan's Resolve"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Diana",
                "Olaf",
                "Nilah",
                "Pantheon"
            ],
            "units": [
                "Braum",
                "Lillia",
                "Diana",
                "Olaf",
                "Rakan",
                "Sylas",
                "Nilah",
                "Pantheon",
                "Bard"
            ],
            "items": [
                {
                    "Diana": [
                        "Sunfire Cape",
                        "Ionic Spark",
                        "Hand of Justice"
                    ]
                },
                {
                    "Olaf": [
                        "Infinity Edge",
                        "Runaan's Hurricane",
                        "Bloodthirster"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Giant Slayer"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Warmog's Armor"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Diana",
                "Olaf",
                "Nilah"
            ],
            "units": [
                "Braum",
                "Lillia",
                "Qiyana",
                "Diana",
                "Olaf",
                "Sylas",
                "Nilah",
                "Pantheon"
            ],
            "items": [
                {
                    "Qiyana": [
                        "Zeke's Herald",
                        "Zeke's Herald"
                    ]
                },
                {
                    "Diana": [
                        "Sunfire Cape",
                        "Ionic Spark",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Olaf": [
                        "Infinity Edge",
                        "Runaan's Hurricane",
                        "Assassin Emblem"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Giant Slayer"
                    ]
                }
            ]
        }
    ],
    "Daeja": [
        {
            "carry": [
                "Daeja"
            ],
            "units": [
                "Sejuani",
                "Rell",
                "Yone",
                "Nunu",
                "Hecarim",
                "Daeja",
                "Yasuo"
            ],
            "threeStars": [],
            "items": [
                {
                    "Nunu": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Daeja": [
                        "Giant Slayer",
                        "Guinsoo's Rageblade",
                        "Hextech Gunblade"
                    ]
                },
                {
                    "Yasuo": [
                        "Cavalier Emblem"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Yasuo",
                "Daeja"
            ],
            "units": [
                "Leona",
                "Sejuani",
                "Nunu",
                "Rakan",
                "Hecarim",
                "Bard",
                "Yasuo",
                "Daeja"
            ],
            "items": [
                {
                    "Leona": [
                        "Sunfire Cape"
                    ]
                },
                {
                    "Nunu": [
                        "Warmog's Armor",
                        "Ionic Spark",
                        "Redemption"
                    ]
                },
                {
                    "Yasuo": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Blue Buff"
                    ]
                },
                {
                    "Daeja": [
                        "Giant Slayer",
                        "Archangel's Staff",
                        "Guinsoo's Rageblade"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Daeja"
            ],
            "units": [
                "Sejuani",
                "Rell",
                "Yone",
                "Nunu",
                "Hecarim",
                "Daeja",
                "Yasuo"
            ],
            "items": [
                {
                    "Nunu": [
                        "Warmog's Armor",
                        "Redemption",
                        "Ionic Spark"
                    ]
                },
                {
                    "Daeja": [
                        "Guinsoo's Rageblade",
                        "Archangel's Staff",
                        "Hextech Gunblade"
                    ]
                }
            ]
        }
    ],
    "Pantheon": [
        {
            "carry": [
                "Olaf",
                "Pantheon"
            ],
            "units": [
                "Lillia",
                "Yone",
                "Olaf",
                "Sylas",
                "Hecarim",
                "Pantheon",
                "Yasuo",
                "Zoe"
            ],
            "threeStars": [
                "Olaf"
            ],
            "items": [
                {
                    "Olaf": [
                        "Bloodthirster",
                        "Giant Slayer",
                        "Runaan's Hurricane"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Giant Slayer",
                        "Titan's Resolve"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Pantheon",
                "Syfen"
            ],
            "units": [
                "Zyra",
                "Seraphine",
                "Sylas",
                "Pantheon",
                "Syfen",
                "Bard",
                "Yasuo"
            ],
            "threeStars": [],
            "items": [
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Giant Slayer",
                        "Titan's Resolve"
                    ]
                },
                {
                    "Syfen": [
                        "Bloodthirster",
                        "Quicksilver",
                        "Titan's Resolve"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Pantheon",
                "Shi Oh Yu"
            ],
            "units": [
                "Karma",
                "Zyra",
                "Seraphine",
                "Pantheon",
                "Shi Oh Yu",
                "Yasuo",
                "Soraka"
            ],
            "threeStars": [],
            "items": [
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Giant Slayer",
                        "Titan's Resolve"
                    ]
                },
                {
                    "Shi Oh Yu": [
                        "Bloodthirster",
                        "Edge of Night",
                        "Titan's Resolve"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Wukong",
                "Pantheon"
            ],
            "units": [
                "Wukong",
                "Olaf",
                "Sylas",
                "Pantheon",
                "Shi Oh Yu",
                "Yasuo",
                "Soraka"
            ],
            "threeStars": [
                "Wukong"
            ],
            "items": [
                {
                    "Wukong": [
                        "Infinity Edge",
                        "Rapid Firecannon",
                        "Runaan's Hurricane"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Giant Slayer",
                        "Titan's Resolve"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Diana",
                "Olaf",
                "Nilah",
                "Pantheon"
            ],
            "units": [
                "Braum",
                "Lillia",
                "Diana",
                "Olaf",
                "Rakan",
                "Sylas",
                "Nilah",
                "Pantheon",
                "Bard"
            ],
            "items": [
                {
                    "Diana": [
                        "Sunfire Cape",
                        "Ionic Spark",
                        "Hand of Justice"
                    ]
                },
                {
                    "Olaf": [
                        "Infinity Edge",
                        "Runaan's Hurricane",
                        "Bloodthirster"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Giant Slayer"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Warmog's Armor"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Pantheon",
                "Sy'fen"
            ],
            "units": [
                "Lillia",
                "Zyra",
                "Seraphine",
                "Sylas",
                "Pantheon",
                "Bard",
                "Zoe",
                "Sy'fen"
            ],
            "items": [
                {
                    "Zyra": [
                        "Spear of Shojin"
                    ]
                },
                {
                    "Sylas": [
                        "Zeke's Herald",
                        "Zeke's Herald",
                        "Protector's Vow"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Giant Slayer"
                    ]
                },
                {
                    "Zoe": [
                        "Spear of Shojin"
                    ]
                },
                {
                    "Sy'fen": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Quicksilver"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Pantheon",
                "Sy'fen"
            ],
            "units": [
                "Jax",
                "Yone",
                "Zyra",
                "Olaf",
                "Sylas",
                "Pantheon",
                "Yasuo",
                "Sy'fen"
            ],
            "items": [
                {
                    "Jax": [
                        "Sunfire Cape"
                    ]
                },
                {
                    "Sylas": [
                        "Zeke's Herald",
                        "Zeke's Herald",
                        "Locket of the Iron Solari"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Yasuo": [
                        "Blue Buff"
                    ]
                },
                {
                    "Sy'fen": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Quicksilver"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Pantheon",
                "Shi Oh Yu",
                "Sy'fen"
            ],
            "units": [
                "Gnar",
                "Pantheon",
                "Jayce",
                "Shi Oh Yu",
                "Sy'fen",
                "Soraka"
            ],
            "items": [
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Gargoyle Stoneplate"
                    ]
                },
                {
                    "Shi Oh Yu": [
                        "Bloodthirster",
                        "Edge of Night",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Sy'fen": [
                        "Giant Slayer",
                        "Titan\u2019s Resolve",
                        "Bloodthirster"
                    ]
                }
            ]
        }
    ],
    "AoShin": [
        {
            "carry": [
                "Ao Shin",
                "Shyvana"
            ],
            "units": [
                "Rakan",
                "Idas",
                "Ao Shin",
                "Shyvana",
                "Terra"
            ],
            "threeStars": [],
            "items": [
                {
                    "Ao Shin": [
                        "Hextech Gunblade",
                        "Spear of Shojin"
                    ]
                },
                {
                    "Shyvana": [
                        "Ionic Spark",
                        "Morellonomicon"
                    ]
                },
                {
                    "Terra": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Lee Sin",
                "Ao Shin"
            ],
            "units": [
                "Sett",
                "Qiyana",
                "Lee Sin",
                "Volibear",
                "Graves",
                "Yasuo",
                "Ao Shin"
            ],
            "threeStars": [
                "Lee Sin"
            ],
            "items": [
                {
                    "Lee Sin": [
                        "Hand of Justice",
                        "Infinity Edge",
                        "Jeweled Gauntlet"
                    ]
                },
                {
                    "Ao Shin": [
                        "Archangel's Staff",
                        "Hextech Gunblade",
                        "Spear of Shojin"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Ao Shin"
            ],
            "units": [
                "Lee Sin",
                "Rakan",
                "Bard",
                "Idas",
                "Ao Shin",
                "Terra"
            ],
            "items": [
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Ionic Spark"
                    ]
                },
                {
                    "Ao Shin": [
                        "Spear of Shojin",
                        "Archangel's Staff",
                        "Bloodthirster"
                    ]
                },
                {
                    "Terra": [
                        "Gargoyle Stoneplate",
                        "Protector's Vow",
                        "Dragon's Claw"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Ao Shin",
                "Shyvana"
            ],
            "units": [
                "Rakan",
                "Graves",
                "Idas",
                "Ao Shin",
                "Shyvana",
                "Terra"
            ],
            "items": [
                {
                    "Idas": [
                        "Mogul's Mail"
                    ]
                },
                {
                    "Ao Shin": [
                        "Spear of Shojin",
                        "Archangel's Staff",
                        "Hextech Gunblade"
                    ]
                },
                {
                    "Shyvana": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Archangel's Staff"
                    ]
                },
                {
                    "Terra": [
                        "Gargoyle Stoneplate",
                        "Protector's Vow",
                        "Dragon's Claw"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Ao Shin",
                "Shyvana"
            ],
            "units": [
                "Rakan",
                "Idas",
                "Terra",
                "Ao Shin",
                "Shyvana"
            ],
            "items": [
                {
                    "Rakan": [
                        "Zeke's Herald"
                    ]
                },
                {
                    "Idas": [
                        "Redemption",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Terra": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Dragon's Claw"
                    ]
                },
                {
                    "Ao Shin": [
                        "Hextech Gunblade",
                        "Spear of Shojin",
                        "Archangel's Staff"
                    ]
                },
                {
                    "Shyvana": [
                        "Morellonomicon",
                        "Ionic Spark"
                    ]
                }
            ]
        }
    ],
    "Syfen": [
        {
            "carry": [
                "Pantheon",
                "Sy'fen"
            ],
            "units": [
                "Lillia",
                "Zyra",
                "Seraphine",
                "Sylas",
                "Pantheon",
                "Bard",
                "Zoe",
                "Sy'fen"
            ],
            "items": [
                {
                    "Zyra": [
                        "Spear of Shojin"
                    ]
                },
                {
                    "Sylas": [
                        "Zeke's Herald",
                        "Zeke's Herald",
                        "Protector's Vow"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Giant Slayer"
                    ]
                },
                {
                    "Zoe": [
                        "Spear of Shojin"
                    ]
                },
                {
                    "Sy'fen": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Quicksilver"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Pantheon",
                "Sy'fen"
            ],
            "units": [
                "Jax",
                "Yone",
                "Zyra",
                "Olaf",
                "Sylas",
                "Pantheon",
                "Yasuo",
                "Sy'fen"
            ],
            "items": [
                {
                    "Jax": [
                        "Sunfire Cape"
                    ]
                },
                {
                    "Sylas": [
                        "Zeke's Herald",
                        "Zeke's Herald",
                        "Locket of the Iron Solari"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Yasuo": [
                        "Blue Buff"
                    ]
                },
                {
                    "Sy'fen": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Quicksilver"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Pantheon",
                "Shi Oh Yu",
                "Sy'fen"
            ],
            "units": [
                "Gnar",
                "Pantheon",
                "Jayce",
                "Shi Oh Yu",
                "Sy'fen",
                "Soraka"
            ],
            "items": [
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Gargoyle Stoneplate"
                    ]
                },
                {
                    "Shi Oh Yu": [
                        "Bloodthirster",
                        "Edge of Night",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Sy'fen": [
                        "Giant Slayer",
                        "Titan\u2019s Resolve",
                        "Bloodthirster"
                    ]
                }
            ]
        }
    ],
    "Graves": [
        {
            "carry": [
                "Graves",
                "Nilah"
            ],
            "units": [
                "Qiyana",
                "Rakan",
                "Seraphine",
                "Zeri",
                "Graves",
                "Nilah",
                "Idas"
            ],
            "threeStars": [],
            "items": [
                {
                    "Graves": [
                        "Bloodthirster",
                        "Titan's Resolve"
                    ]
                },
                {
                    "Nilah": [
                        "Hand of Justice",
                        "Infinity Edge"
                    ]
                },
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Warmog's Armor"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Aphelios",
                "Graves"
            ],
            "units": [
                "Sejuani",
                "Senna",
                "Aphelios",
                "Qiyana",
                "Rell",
                "Rengar",
                "Zeri",
                "Graves",
                "Hecarim"
            ],
            "items": [
                {
                    "Senna": [
                        "Zeke's Herald"
                    ]
                },
                {
                    "Aphelios": [
                        "Last Whisper",
                        "Infinity Edge"
                    ]
                },
                {
                    "Rell": [
                        "Protector's Vow",
                        "Sunfire Cape"
                    ]
                },
                {
                    "Zeri": [
                        "Darkflight Emblem"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Giant Slayer"
                    ]
                },
                {
                    "Hecarim": [
                        "Gargoyle Stoneplate"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Zeri",
                "Graves",
                "Nilah"
            ],
            "units": [
                "Tristana",
                "Qiyana",
                "Zac",
                "Zeri",
                "Graves",
                "Nilah",
                "Nomsy (Cannoneer)",
                "Idas"
            ],
            "items": [
                {
                    "Zeri": [
                        "Giant Slayer",
                        "Last Whisper",
                        "Guinsoo's Rageblade"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Infinity Edge"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Giant Slayer"
                    ]
                },
                {
                    "Nomsy (Cannoneer)": [
                        "Needlessly Big Gem",
                        "Statikk Shiv"
                    ]
                },
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Mogul's Mail"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Aphelios",
                "Graves"
            ],
            "units": [
                "Sejuani",
                "Rell",
                "Aphelios",
                "Aphelios",
                "Rell",
                "Zeri",
                "Graves",
                "Hecarim"
            ],
            "items": [
                {
                    "Sejuani": [
                        "Zeke's Herald"
                    ]
                },
                {
                    "Aphelios": [
                        "Runaan's Hurricane",
                        "Last Whisper"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster",
                        "Infinity Edge",
                        "Titan\u2019s Resolve"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Nilah",
                "Graves"
            ],
            "units": [
                "Jax",
                "Braum",
                "Zyra",
                "Nilah",
                "Hecarim",
                "Graves",
                "Yasuo",
                "Bard"
            ],
            "items": [
                {
                    "Nilah": [
                        "Giant Slayer",
                        "Edge of Night",
                        "Hand of Justice"
                    ]
                },
                {
                    "Hecarim": [
                        "Morellonomicon",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Graves": [
                        "Infinity Edge",
                        "Titan\u2019s Resolve",
                        "Last Whisper"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Nilah",
                "Graves"
            ],
            "units": [
                "Qiyana",
                "Seraphine",
                "Rakan",
                "Zeri",
                "Nilah",
                "Graves",
                "Idas"
            ],
            "items": [
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Edge of Night"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Idas": [
                        "Sunfire Cape",
                        "Redemption",
                        "Bramble Vest"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Aphelios",
                "Graves"
            ],
            "units": [
                "Sejuani",
                "Senna",
                "Rell",
                "Aphelios",
                "Nunu",
                "Zeri",
                "Hecarim",
                "Graves"
            ],
            "items": [
                {
                    "Sejuani": [
                        "Zz'Rot Portal"
                    ]
                },
                {
                    "Rell": [
                        "Protector's Vow",
                        "Sunfire Cape"
                    ]
                },
                {
                    "Aphelios": [
                        "Guinsoo's Rageblade",
                        "Runaan's Hurricane",
                        "Deathblade"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster",
                        "Guinsoo's Rageblade",
                        "Titan\u2019s Resolve"
                    ]
                }
            ]
        }
    ],
    "LeeSin": [
        {
            "carry": [
                "Lee Sin",
                "Ao Shin"
            ],
            "units": [
                "Sett",
                "Qiyana",
                "Lee Sin",
                "Volibear",
                "Graves",
                "Yasuo",
                "Ao Shin"
            ],
            "threeStars": [
                "Lee Sin"
            ],
            "items": [
                {
                    "Lee Sin": [
                        "Hand of Justice",
                        "Infinity Edge",
                        "Jeweled Gauntlet"
                    ]
                },
                {
                    "Ao Shin": [
                        "Archangel's Staff",
                        "Hextech Gunblade",
                        "Spear of Shojin"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Kai'sa",
                "Lee Sin",
                "Yasuo"
            ],
            "units": [
                "Karma",
                "Sejuani",
                "Sett",
                "Kai'sa",
                "Qiyana",
                "Lee Sin",
                "Volibear",
                "Hecarim",
                "Yasuo"
            ],
            "items": [
                {
                    "Kai'sa": [
                        "Morellonomicon",
                        "Statikk Shiv"
                    ]
                },
                {
                    "Lee Sin": [
                        "Infinity Edge",
                        "Jeweled Gauntlet",
                        "Bloodthirster"
                    ]
                },
                {
                    "Hecarim": [
                        "Protector's Vow"
                    ]
                },
                {
                    "Yasuo": [
                        "Titan\u2019s Resolve",
                        "Infinity Edge",
                        "Bloodthirster"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Lee Sin"
            ],
            "units": [
                "Sett",
                "Karma",
                "Qiyana",
                "Kai'sa",
                "Lee Sin",
                "Volibear",
                "Hecarim",
                "Yasuo"
            ],
            "items": [
                {
                    "Lee Sin": [
                        "Hextech Gunblade",
                        "Jeweled Gauntlet",
                        "Infinity Edge"
                    ]
                }
            ]
        }
    ],
    "Kaisa": [
        {
            "carry": [
                "Kai'sa",
                "Lee Sin",
                "Yasuo"
            ],
            "units": [
                "Karma",
                "Sejuani",
                "Sett",
                "Kai'sa",
                "Qiyana",
                "Lee Sin",
                "Volibear",
                "Hecarim",
                "Yasuo"
            ],
            "items": [
                {
                    "Kai'sa": [
                        "Morellonomicon",
                        "Statikk Shiv"
                    ]
                },
                {
                    "Lee Sin": [
                        "Infinity Edge",
                        "Jeweled Gauntlet",
                        "Bloodthirster"
                    ]
                },
                {
                    "Hecarim": [
                        "Protector's Vow"
                    ]
                },
                {
                    "Yasuo": [
                        "Titan\u2019s Resolve",
                        "Infinity Edge",
                        "Bloodthirster"
                    ]
                }
            ]
        }
    ],
    "Nilah": [
        {
            "carry": [
                "Graves",
                "Nilah"
            ],
            "units": [
                "Qiyana",
                "Rakan",
                "Seraphine",
                "Zeri",
                "Graves",
                "Nilah",
                "Idas"
            ],
            "threeStars": [],
            "items": [
                {
                    "Graves": [
                        "Bloodthirster",
                        "Titan's Resolve"
                    ]
                },
                {
                    "Nilah": [
                        "Hand of Justice",
                        "Infinity Edge"
                    ]
                },
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Warmog's Armor"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Diana",
                "Olaf",
                "Nilah",
                "Pantheon"
            ],
            "units": [
                "Braum",
                "Lillia",
                "Diana",
                "Olaf",
                "Rakan",
                "Sylas",
                "Nilah",
                "Pantheon",
                "Bard"
            ],
            "items": [
                {
                    "Diana": [
                        "Sunfire Cape",
                        "Ionic Spark",
                        "Hand of Justice"
                    ]
                },
                {
                    "Olaf": [
                        "Infinity Edge",
                        "Runaan's Hurricane",
                        "Bloodthirster"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Giant Slayer"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Warmog's Armor"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Diana",
                "Olaf",
                "Nilah"
            ],
            "units": [
                "Braum",
                "Lillia",
                "Qiyana",
                "Diana",
                "Olaf",
                "Sylas",
                "Nilah",
                "Pantheon"
            ],
            "items": [
                {
                    "Qiyana": [
                        "Zeke's Herald",
                        "Zeke's Herald"
                    ]
                },
                {
                    "Diana": [
                        "Sunfire Cape",
                        "Ionic Spark",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Olaf": [
                        "Infinity Edge",
                        "Runaan's Hurricane",
                        "Assassin Emblem"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Giant Slayer"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Diana",
                "Rengar",
                "Nilah"
            ],
            "units": [
                "Aphelios",
                "Qiyana",
                "Rell",
                "Diana",
                "Rengar",
                "Nilah",
                "Tyrant Swain"
            ],
            "items": [
                {
                    "Qiyana": [
                        "Zeke's Herald"
                    ]
                },
                {
                    "Diana": [
                        "Ionic Spark",
                        "Hand of Justice",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Rengar": [
                        "Infinity Edge",
                        "Bloodthirster"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Giant Slayer",
                        "Hand of Justice"
                    ]
                },
                {
                    "Tyrant Swain": [
                        "Gargoyle Stoneplate",
                        "Morellonomicon"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Zeri",
                "Graves",
                "Nilah"
            ],
            "units": [
                "Tristana",
                "Qiyana",
                "Zac",
                "Zeri",
                "Graves",
                "Nilah",
                "Nomsy (Cannoneer)",
                "Idas"
            ],
            "items": [
                {
                    "Zeri": [
                        "Giant Slayer",
                        "Last Whisper",
                        "Guinsoo's Rageblade"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Infinity Edge"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Giant Slayer"
                    ]
                },
                {
                    "Nomsy (Cannoneer)": [
                        "Needlessly Big Gem",
                        "Statikk Shiv"
                    ]
                },
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Mogul's Mail"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Nilah",
                "Graves"
            ],
            "units": [
                "Jax",
                "Braum",
                "Zyra",
                "Nilah",
                "Hecarim",
                "Graves",
                "Yasuo",
                "Bard"
            ],
            "items": [
                {
                    "Nilah": [
                        "Giant Slayer",
                        "Edge of Night",
                        "Hand of Justice"
                    ]
                },
                {
                    "Hecarim": [
                        "Morellonomicon",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Graves": [
                        "Infinity Edge",
                        "Titan\u2019s Resolve",
                        "Last Whisper"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Nilah",
                "Graves"
            ],
            "units": [
                "Qiyana",
                "Seraphine",
                "Rakan",
                "Zeri",
                "Nilah",
                "Graves",
                "Idas"
            ],
            "items": [
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Edge of Night"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Idas": [
                        "Sunfire Cape",
                        "Redemption",
                        "Bramble Vest"
                    ]
                }
            ]
        }
    ],
    "Rengar": [
        {
            "carry": [
                "Rengar",
                "Swain"
            ],
            "units": [
                "Sejuani",
                "Aphelios",
                "Qiyana",
                "Rell",
                "Rengar",
                "Graves",
                "Swain"
            ],
            "threeStars": [],
            "items": [
                {
                    "Sejuani": [
                        "Protector's Vow"
                    ]
                },
                {
                    "Rengar": [
                        "Bloodthirster",
                        "Infinity Edge"
                    ]
                },
                {
                    "Swain": [
                        "Archangel's Staff",
                        "Morellonomicon",
                        "Titan's Resolve"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Diana",
                "Rengar",
                "Nilah"
            ],
            "units": [
                "Aphelios",
                "Qiyana",
                "Rell",
                "Diana",
                "Rengar",
                "Nilah",
                "Tyrant Swain"
            ],
            "items": [
                {
                    "Qiyana": [
                        "Zeke's Herald"
                    ]
                },
                {
                    "Diana": [
                        "Ionic Spark",
                        "Hand of Justice",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Rengar": [
                        "Infinity Edge",
                        "Bloodthirster"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Giant Slayer",
                        "Hand of Justice"
                    ]
                },
                {
                    "Tyrant Swain": [
                        "Gargoyle Stoneplate",
                        "Morellonomicon"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Rengar",
                "Tyrant Swain"
            ],
            "units": [
                "Sejuani",
                "Rell",
                "Aphelios",
                "Qiyana",
                "Rengar",
                "Graves",
                "Tyrant Swain"
            ],
            "items": [
                {
                    "Sejuani": [
                        "Protector's Vow"
                    ]
                },
                {
                    "Rengar": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Tyrant Swain": [
                        "Morellonomicon",
                        "Gargoyle Stoneplate",
                        "Archangel's Staff"
                    ]
                }
            ]
        }
    ],
    "Sohm": [
        {
            "carry": [
                "Sohm"
            ],
            "units": [
                "Malphite",
                "Seraphine",
                "Sylas",
                "Nilah",
                "Sohm",
                "Bard",
                "Zoe"
            ],
            "threeStars": [],
            "items": [
                {
                    "Sylas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Sohm": [
                        "Blue Buff",
                        "Infinity Edge",
                        "Jeweled Gauntlet"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Sohm"
            ],
            "units": [
                "Malphite",
                "Taliyah",
                "Lux",
                "Zyra",
                "Seraphine",
                "Sylas",
                "Zoe",
                "Sohm"
            ],
            "items": [
                {
                    "Malphite": [
                        "Zz'Rot Portal"
                    ]
                },
                {
                    "Zyra": [
                        "Chalice of Power",
                        "Chalice of Power",
                        "Statikk Shiv"
                    ]
                },
                {
                    "Seraphine": [
                        "Spear of Shojin"
                    ]
                },
                {
                    "Sylas": [
                        "Gargoyle Stoneplate",
                        "Warmog's Armor",
                        "Sunfire Cape"
                    ]
                },
                {
                    "Zoe": [
                        "Spear of Shojin"
                    ]
                },
                {
                    "Sohm": [
                        "Archangel's Staff",
                        "Blue Buff",
                        "Jeweled Gauntlet"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Sohm"
            ],
            "units": [
                "Malphite",
                "Taliyah",
                "Lillia",
                "Sylas",
                "Seraphine",
                "Sohm",
                "Zoe"
            ],
            "items": [
                {
                    "Malphite": [
                        "Zz'Rot Portal"
                    ]
                },
                {
                    "Sylas": [
                        "Gargoyle Stoneplate",
                        "Warmog's Armor",
                        "Dragon's Claw"
                    ]
                },
                {
                    "Sohm": [
                        "Blue Buff",
                        "Hextech Gunblade",
                        "Jeweled Gauntlet"
                    ]
                }
            ]
        }
    ],
    "ShiOhYu": [
        {
            "carry": [
                "Pantheon",
                "Shi Oh Yu"
            ],
            "units": [
                "Karma",
                "Zyra",
                "Seraphine",
                "Pantheon",
                "Shi Oh Yu",
                "Yasuo",
                "Soraka"
            ],
            "threeStars": [],
            "items": [
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Giant Slayer",
                        "Titan's Resolve"
                    ]
                },
                {
                    "Shi Oh Yu": [
                        "Bloodthirster",
                        "Edge of Night",
                        "Titan's Resolve"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Yasuo",
                "Shi Oh Yu"
            ],
            "units": [
                "Karma",
                "Rakan",
                "Seraphine",
                "Soraka",
                "Yasuo",
                "Idas",
                "Shi Oh Yu"
            ],
            "items": [
                {
                    "Yasuo": [
                        "Titan\u2019s Resolve",
                        "Blue Buff",
                        "Bloodthirster"
                    ]
                },
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Redemption"
                    ]
                },
                {
                    "Shi Oh Yu": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Guinsoo's Rageblade"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Jayce",
                "Shi Oh Yu",
                "Shyvana"
            ],
            "units": [
                "Kai'sa",
                "Zac",
                "Rakan",
                "Seraphine",
                "Jayce",
                "Shi Oh Yu",
                "Shyvana"
            ],
            "items": [
                {
                    "Jayce": [
                        "Infinity Edge",
                        "Jeweled Gauntlet",
                        "Hand of Justice"
                    ]
                },
                {
                    "Shi Oh Yu": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Guinsoo's Rageblade"
                    ]
                },
                {
                    "Shyvana": [
                        "Titan\u2019s Resolve",
                        "Archangel's Staff",
                        "Morellonomicon"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Shi Oh Yu"
            ],
            "units": [
                "Karma",
                "Zyra",
                "Seraphine",
                "Pantheon",
                "Shi Oh Yu",
                "Yasuo",
                "Soraka"
            ],
            "items": [
                {
                    "Pantheon": [
                        "Gargoyle Stoneplate",
                        "Bloodthirster",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Shi Oh Yu": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Edge of Night"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Pantheon",
                "Shi Oh Yu",
                "Sy'fen"
            ],
            "units": [
                "Gnar",
                "Pantheon",
                "Jayce",
                "Shi Oh Yu",
                "Sy'fen",
                "Soraka"
            ],
            "items": [
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Gargoyle Stoneplate"
                    ]
                },
                {
                    "Shi Oh Yu": [
                        "Bloodthirster",
                        "Edge of Night",
                        "Titan\u2019s Resolve"
                    ]
                },
                {
                    "Sy'fen": [
                        "Giant Slayer",
                        "Titan\u2019s Resolve",
                        "Bloodthirster"
                    ]
                }
            ]
        }
    ],
    "Zippy": [
        {
            "carry": [
                "Zippy",
                "Jayce"
            ],
            "units": [
                "Sejuani",
                "Twitch",
                "Zippy",
                "Jayce",
                "Bard",
                "Shyvana"
            ],
            "items": [
                {
                    "Zippy": [
                        "Titan\u2019s Resolve",
                        "Sunfire Cape",
                        "Bloodthirster"
                    ]
                },
                {
                    "Jayce": [
                        "Titan\u2019s Resolve",
                        "Protector's Vow",
                        "Ionic Spark"
                    ]
                }
            ]
        }
    ],
    "Jayce": [
        {
            "carry": [
                "Jayce",
                "Shi Oh Yu",
                "Shyvana"
            ],
            "units": [
                "Kai'sa",
                "Zac",
                "Rakan",
                "Seraphine",
                "Jayce",
                "Shi Oh Yu",
                "Shyvana"
            ],
            "items": [
                {
                    "Jayce": [
                        "Infinity Edge",
                        "Jeweled Gauntlet",
                        "Hand of Justice"
                    ]
                },
                {
                    "Shi Oh Yu": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Guinsoo's Rageblade"
                    ]
                },
                {
                    "Shyvana": [
                        "Titan\u2019s Resolve",
                        "Archangel's Staff",
                        "Morellonomicon"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Zippy",
                "Jayce"
            ],
            "units": [
                "Sejuani",
                "Twitch",
                "Zippy",
                "Jayce",
                "Bard",
                "Shyvana"
            ],
            "items": [
                {
                    "Zippy": [
                        "Titan\u2019s Resolve",
                        "Sunfire Cape",
                        "Bloodthirster"
                    ]
                },
                {
                    "Jayce": [
                        "Titan\u2019s Resolve",
                        "Protector's Vow",
                        "Ionic Spark"
                    ]
                }
            ]
        }
    ],
    "Swain": [
        {
            "carry": [
                "Rengar",
                "Swain"
            ],
            "units": [
                "Sejuani",
                "Aphelios",
                "Qiyana",
                "Rell",
                "Rengar",
                "Graves",
                "Swain"
            ],
            "threeStars": [],
            "items": [
                {
                    "Sejuani": [
                        "Protector's Vow"
                    ]
                },
                {
                    "Rengar": [
                        "Bloodthirster",
                        "Infinity Edge"
                    ]
                },
                {
                    "Swain": [
                        "Archangel's Staff",
                        "Morellonomicon",
                        "Titan's Resolve"
                    ]
                }
            ]
        }
    ],
    "Zoe": [
        {
            "carry": [
                "Zoe",
                "Aurelion Sol"
            ],
            "units": [
                "Vladimir",
                "Lux",
                "Rakan",
                "Seraphine",
                "Zoe",
                "Idas",
                "Aurelion Sol"
            ],
            "items": [
                {
                    "Zoe": [
                        "Spear of Shojin",
                        "Guinsoo's Rageblade",
                        "Statikk Shiv"
                    ]
                },
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Ionic Spark",
                        "Sunfire Cape"
                    ]
                },
                {
                    "Aurelion Sol": [
                        "Spear of Shojin",
                        "Archangel's Staff",
                        "Jeweled Gauntlet"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Zoe",
                "Aurelion Sol"
            ],
            "units": [
                "Skarner",
                "Lux",
                "Zyra",
                "Seraphine",
                "Sylas",
                "Bard",
                "Zoe",
                "Aurelion Sol"
            ],
            "items": [
                {
                    "Skarner": [
                        "Zz'Rot Portal"
                    ]
                },
                {
                    "Sylas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Zoe": [
                        "Spear of Shojin",
                        "Statikk Shiv",
                        "Evoker Emblem"
                    ]
                },
                {
                    "Aurelion Sol": [
                        "Giant Slayer",
                        "Spear of Shojin",
                        "Archangel's Staff"
                    ]
                }
            ]
        }
    ],
    "AurelionSol": [
        {
            "carry": [
                "Zoe",
                "Aurelion Sol"
            ],
            "units": [
                "Vladimir",
                "Lux",
                "Rakan",
                "Seraphine",
                "Zoe",
                "Idas",
                "Aurelion Sol"
            ],
            "items": [
                {
                    "Zoe": [
                        "Spear of Shojin",
                        "Guinsoo's Rageblade",
                        "Statikk Shiv"
                    ]
                },
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Ionic Spark",
                        "Sunfire Cape"
                    ]
                },
                {
                    "Aurelion Sol": [
                        "Spear of Shojin",
                        "Archangel's Staff",
                        "Jeweled Gauntlet"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Zoe",
                "Aurelion Sol"
            ],
            "units": [
                "Skarner",
                "Lux",
                "Zyra",
                "Seraphine",
                "Sylas",
                "Bard",
                "Zoe",
                "Aurelion Sol"
            ],
            "items": [
                {
                    "Skarner": [
                        "Zz'Rot Portal"
                    ]
                },
                {
                    "Sylas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Zoe": [
                        "Spear of Shojin",
                        "Statikk Shiv",
                        "Evoker Emblem"
                    ]
                },
                {
                    "Aurelion Sol": [
                        "Giant Slayer",
                        "Spear of Shojin",
                        "Archangel's Staff"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Nomsy (Evoker)",
                "Aurelion Sol"
            ],
            "units": [
                "Lulu",
                "Taliyah",
                "Zac",
                "Seraphine",
                "Sylas",
                "Zoe",
                "Nomsy (Evoker)",
                "Aurelion Sol"
            ],
            "items": [
                {
                    "Sylas": [
                        "Gargoyle Stoneplate",
                        "Warmog's Armor",
                        "Ionic Spark"
                    ]
                },
                {
                    "Nomsy (Evoker)": [
                        "Spear of Shojin",
                        "Statikk Shiv"
                    ]
                },
                {
                    "Aurelion Sol": [
                        "Spear of Shojin",
                        "Archangel's Staff",
                        "Jeweled Gauntlet"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Lux",
                "Aurelion Sol"
            ],
            "units": [
                "Vladimir",
                "Skarner",
                "Nidalee",
                "Lux",
                "Sylas",
                "Varus",
                "Aurelion Sol"
            ],
            "items": [
                {
                    "Lux": [
                        "Spear of Shojin",
                        "Archangel's Staff",
                        "Jeweled Gauntlet"
                    ]
                },
                {
                    "Sylas": [
                        "Protector's Vow",
                        "Sunfire Cape",
                        "Gargoyle Stoneplate"
                    ]
                },
                {
                    "Varus": [
                        "Statikk Shiv"
                    ]
                },
                {
                    "Aurelion Sol": [
                        "Hextech Gunblade",
                        "Archangel's Staff",
                        "Giant Slayer"
                    ]
                }
            ]
        }
    ],
    "Zeri": [
        {
            "carry": [
                "Zeri"
            ],
            "units": [
                "Aphelios",
                "Tristana",
                "Rakan",
                "Seraphine",
                "Zeri",
                "Nomsy",
                "Idas"
            ],
            "threeStars": [
                "Rakan",
                "Zeri",
                "Nomsy"
            ],
            "items": [
                {
                    "Zeri": [
                        "Guinsoo's Rageblade",
                        "Hand of Justice",
                        "Infinity Edge"
                    ]
                },
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Warmog's Armor"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Zeri",
                "Graves",
                "Nilah"
            ],
            "units": [
                "Tristana",
                "Qiyana",
                "Zac",
                "Zeri",
                "Graves",
                "Nilah",
                "Nomsy (Cannoneer)",
                "Idas"
            ],
            "items": [
                {
                    "Zeri": [
                        "Giant Slayer",
                        "Last Whisper",
                        "Guinsoo's Rageblade"
                    ]
                },
                {
                    "Graves": [
                        "Bloodthirster",
                        "Titan\u2019s Resolve",
                        "Infinity Edge"
                    ]
                },
                {
                    "Nilah": [
                        "Infinity Edge",
                        "Hand of Justice",
                        "Giant Slayer"
                    ]
                },
                {
                    "Nomsy (Cannoneer)": [
                        "Needlessly Big Gem",
                        "Statikk Shiv"
                    ]
                },
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Mogul's Mail"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Zeri"
            ],
            "units": [
                "Aphelios",
                "Zeri",
                "Rakan",
                "Nomsy (Cannoneer)",
                "Idas"
            ],
            "items": [
                {
                    "Zeri": [
                        "Infinity Edge",
                        "Last Whisper",
                        "Guinsoo's Rageblade"
                    ]
                },
                {
                    "Idas": [
                        "Warmog's Armor",
                        "Gargoyle Stoneplate",
                        "Sunfire Cape"
                    ]
                }
            ]
        }
    ],
    "Lux": [
        {
            "carry": [
                "Lux"
            ],
            "units": [
                "Nidalee",
                "Skarner",
                "Vladimir",
                "Lux",
                "Sylas",
                "Varus",
                "Aurelion Sol"
            ],
            "threeStars": [
                "Nidalee",
                "Skarner",
                "Vladimir",
                "Lux",
                "Sylas"
            ],
            "items": [
                {
                    "Lux": [
                        "Archangel's Staff",
                        "Hextech Gunblade",
                        "Spear of Shojin"
                    ]
                },
                {
                    "Sylas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Warmog's Armor"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Lux",
                "Aurelion Sol"
            ],
            "units": [
                "Vladimir",
                "Skarner",
                "Nidalee",
                "Lux",
                "Sylas",
                "Varus",
                "Aurelion Sol"
            ],
            "items": [
                {
                    "Lux": [
                        "Spear of Shojin",
                        "Archangel's Staff",
                        "Jeweled Gauntlet"
                    ]
                },
                {
                    "Sylas": [
                        "Protector's Vow",
                        "Sunfire Cape",
                        "Gargoyle Stoneplate"
                    ]
                },
                {
                    "Varus": [
                        "Statikk Shiv"
                    ]
                },
                {
                    "Aurelion Sol": [
                        "Hextech Gunblade",
                        "Archangel's Staff",
                        "Giant Slayer"
                    ]
                }
            ]
        }
    ],
    "Varus": [
        {
            "carry": [
                "Varus"
            ],
            "units": [
                "Nidalee",
                "Skarner",
                "Vladimir",
                "Lux",
                "Twitch",
                "Sylas",
                "Varus",
                "Xayah"
            ],
            "threeStars": [
                "Sylas",
                "Varus"
            ],
            "items": [
                {
                    "Sylas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Varus": [
                        "Deathblade",
                        "Guinsoo's Rageblade",
                        "Runaan's Hurricane"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Varus"
            ],
            "units": [
                "Nidalee",
                "Skarner",
                "Vladimir",
                "Lux",
                "Twitch",
                "Zyra",
                "Sylas",
                "Varus"
            ],
            "items": [
                {
                    "Skarner": [
                        "Zz'Rot Portal"
                    ]
                },
                {
                    "Vladimir": [
                        "Zz'Rot Portal"
                    ]
                },
                {
                    "Sylas": [
                        "Gargoyle Stoneplate",
                        "Warmog's Armor",
                        "Sunfire Cape"
                    ]
                },
                {
                    "Varus": [
                        "Giant Slayer",
                        "Guinsoo's Rageblade",
                        "Runaan's Hurricane"
                    ]
                }
            ]
        }
    ],
    "Wukong": [
        {
            "carry": [
                "Wukong",
                "Pantheon"
            ],
            "units": [
                "Wukong",
                "Olaf",
                "Sylas",
                "Pantheon",
                "Shi Oh Yu",
                "Yasuo",
                "Soraka"
            ],
            "threeStars": [
                "Wukong"
            ],
            "items": [
                {
                    "Wukong": [
                        "Infinity Edge",
                        "Rapid Firecannon",
                        "Runaan's Hurricane"
                    ]
                },
                {
                    "Pantheon": [
                        "Bloodthirster",
                        "Giant Slayer",
                        "Titan's Resolve"
                    ]
                }
            ]
        }
    ],
    "Nomsy": [
        {
            "carry": [
                "Nomsy"
            ],
            "units": [
                "Zyra",
                "Lulu",
                "Rakan",
                "Seraphine",
                "Nomsy",
                "Idas",
                "Bard"
            ],
            "threeStars": [
                "Rakan",
                "Nomsy"
            ],
            "items": [
                {
                    "Nomsy": [
                        "Archangel's Staff",
                        "Hextech Gunblade",
                        "Spear of Shojin"
                    ]
                },
                {
                    "Idas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Warmog's Armor"
                    ]
                }
            ]
        },
        {
            "carry": [
                "Nomsy"
            ],
            "units": [
                "Heimerdinger",
                "Lux",
                "Sylas",
                "Nomsy",
                "Syfen",
                "Bard",
                "Zoe"
            ],
            "threeStars": [
                "Sylas",
                "Nomsy"
            ],
            "items": [
                {
                    "Sylas": [
                        "Gargoyle Stoneplate",
                        "Sunfire Cape",
                        "Warmog's Armor"
                    ]
                },
                {
                    "Nomsy": [
                        "Archangel's Staff",
                        "Hextech Gunblade",
                        "Spear of Shojin"
                    ]
                }
            ]
        }
    ],
    "Nomsy(Evoker)": [
        {
            "carry": [
                "Nomsy (Evoker)",
                "Aurelion Sol"
            ],
            "units": [
                "Lulu",
                "Taliyah",
                "Zac",
                "Seraphine",
                "Sylas",
                "Zoe",
                "Nomsy (Evoker)",
                "Aurelion Sol"
            ],
            "items": [
                {
                    "Sylas": [
                        "Gargoyle Stoneplate",
                        "Warmog's Armor",
                        "Ionic Spark"
                    ]
                },
                {
                    "Nomsy (Evoker)": [
                        "Spear of Shojin",
                        "Statikk Shiv"
                    ]
                },
                {
                    "Aurelion Sol": [
                        "Spear of Shojin",
                        "Archangel's Staff",
                        "Jeweled Gauntlet"
                    ]
                }
            ]
        }
    ]
}
  return Response(lolchess)
# Create your views here.
