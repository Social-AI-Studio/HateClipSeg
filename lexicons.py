hateful_lexicons = {
    "gender": {
        "female": [
            "cunt", "femnazi", "whore", "mudshark", "chicks", "pussy",
            "bitch", "hoe", "raped", "slut", "thot", "gold digger",
            "bimbo", "skank", "breeder"
        ],
        "male": [
            "cuck", "ass", "asshole", "dick", "rent boy", "incel",
            "simp", "mangina", "manlet", "deadbeat"
        ]
    },

    "race": {
        "asians": [
            "ching chong", "gookboy", "gook", "chink", "chinaman", "zipperhead"
        ],
        "latinos": [
            "wetback", "spic", "latina"
        ],
        "arab": [
            "raghead", "camel jockey"
        ],
        "black": [
            "nigger", "spearchucker", "niglet", "coon", "jungle bunny",
            "jungle monkey", "nigga", "ghetto"
        ],
        "jews": [
            "zionist", "kike", "goy", "goyim", "kikescum"
        ],
        "white": [
            "white trash", "whites", "redneck"
        ],
        "indigenous": [
            "redskin"
        ],
        "mixed_race": [
            "mutt", "mongrel"
        ],
        "general": [
            "shitskin", "obozo"
        ]
    },

    "sexual_orientation": {
        "general": [
            "faggot", "queer", "lgbt", "foot fetish", "alphabet people"
        ],
        "gay": [
            "sissy", "bar of soap", "pansy", "anal", "twink", "fruitcake", "poof"
        ],
        "transphobic": [
            "tranny", "trans", "femboy", "trap", "shemale"
        ],
        "lesbian": [
            "dyke", "homo", "girlfags", "butch", "carpet muncher",
            "lezzies", "stud", "bull dyke", "diesel dyke"
        ]
    },

    "religion": {
        "muslim": [
            "goatfucker", "moslem", "allah akbar", "muzrat", "kuffar",
            "muslimes", "muzzies", "mussie", "infidel", "al Qaeda", "ISIS"
        ],
        "christian": [
            "christians", "mormon", "fundie", "cherrypicking"
        ],
        "hindu": [
            "hindu", "sikh", "jain", "dothead", "towelhead", "paki", "turban"
        ],
        "buddhist": [
            "buddhist"
        ],
        "communist": [
            "communist", "marxist", "kommies", "commie", "pinko",
            "socialist", "leftist"
        ],
        "jew": [
            "jews", "yid", "sheeny", "jewboy", "jewess", "moneylender"
        ],
        "political": [
            "liberals", "libscum", "miscellaneous"
        ],
        "disability": [
            "retard", "crippled", "fucktard"
        ],
        "other": [
            "cross-breed", "inbred", "troll",  # “?” category mapped to “other”
        ],
        "general_insult": [
            "fuck", "shit", "crap", "damn", "jerk", "motherfucker"
        ],
        "self_harm": [
            "suicide", "kill yourself", "kill all"
        ],
        "sexual": [
            "pervert"
        ],
        "refugee": [
            "leeches", "freeloader", "cockroaches",
            "boat people", "terrorists", "benefits seeker"
        ]
    }
}

# If you need a single flat list of all lexicons, you can do:
all_hateful_terms = []
def collect_terms(node):
    if isinstance(node, list):
        all_hateful_terms.extend(node)
    elif isinstance(node, dict):
        for sub in node.values():
            collect_terms(sub)

collect_terms(hateful_lexicons)
# `all_hateful_terms` now contains every string in a single list.

# Example printout:
print(hateful_lexicons["gender"]["female"])
print(all_hateful_terms)
# → ['cunt', 'femnazi', 'whore', ...]
# print(len(all_hateful_terms))  # total count of unique entries
