import random

words = [
    "about", "above", "abuse", "actor", "acute",
    "admit", "adopt", "adult", "after", "again",
    "agent", "agree", "ahead", "alarm", "album",
    "alert", "alien", "alive", "allow", "alone",
    "along", "alter", "among", "anger", "angle",
    "angry", "apart", "apple", "apply", "arena",
    "argue", "arise", "armed", "armor", "arrow",
    "aside", "asset", "audio", "avoid", "award",
    "aware", "awful", "bacon", "badge", "basic",
    "beach", "begin", "being", "below", "bench",
    "birth", "black", "blade", "blame", "blank",
    "blast", "blend", "blind", "block", "blood",
    "board", "boost", "booth", "bound", "brain",
    "brand", "brave", "bread", "break", "brick", 
    "brief", "bring", "broad", "broke",
    "brown", "brush", "build", "built", "cable",
    "carry", "catch", "cause", "chain", "chair",
    "chaos", "charm", "chase", "cheap", "check",
    "chest", "chief", "child", "china", "claim",
    "class", "clean", "clear", "climb", "clock",
    "close", "cloud", "coach", "coast", "color",
    "comic", "common", "coral", "count", "court",
    "cover", "craft", "crash", "crazy", "cream",
    "crime", "cross", "crowd", "crown", "crush",
    "curve", "cycle", "daily", "dance", "death",
    "debug", "delay", "depth", "devil", "dirty",
    "doubt", "dozen", "draft", "dream", "dress",
    "drink", "drive", "early", "earth", "eight",
    "elite", "empty", "enemy", "enjoy", "enter",
    "entry", "equal", "error", "event", "every",
    "exact", "extra", "faith", "false", "fancy",
    "fault", "feast", "field", "fight", "final",
    "first", "flame", "flash", "fleet", "floor",
    "focus", "force", "frame", "fresh",
    "front", "frost", "fruit", "fully", "funny",
    "giant", "given", "glass", "globe", "glory",
    "going", "grace", "grade", "grand", "grant",
    "grass", "great", "green", "group", "guard",
    "guess", "guest", "guide", "happy", "heart",
    "heavy", "hello", "horse", "hotel", "house",
    "human", "ideal", "image", "imply", "index",
    "inner", "input", "issue", "jelly", "joint",
    "judge", "juice", "knife", "known", "label",
    "large", "laser", "later", "laugh", "layer",
    "learn", "least", "leave", "legal", "level",
    "light", "limit", "local", "logic", "lucky",
    "magic", "major", "maker", "march", "match",
    "maybe", "media", "metal", "might", "minor",
    "model", "money", "month", "moral", "motor",
    "mount", "mouse", "mouth", "movie", "music",
    "never", "night", "noise", "north", "novel",
    "nurse", "occur", "ocean", "offer", "often",
    "order", "other", "outer", "owner", "paint",
    "panel", "paper", "party", "peace", "phone",
    "photo", "piano", "piece", "pilot", "place",
    "plain", "plane", "plant", "plate", "point",
    "power", "press", "price", "pride", "prime",
    "print", "prize", "proof", "proud", "quick",
    "quiet", "radio", "raise", "range", "rapid",
    "reach", "ready", "realm", "reason", "reply",
    "right", "rival", "river", "robot", "rough",
    "round", "royal", "rural", "scale", "scene",
    "score", "sense", "serve", "seven", "shade",
    "shake", "shape", "share", "sharp", "sheep",
    "sheet", "shelf", "shell", "shift", "shine",
    "shirt", "shock", "shoot", "short", "sight",
    "since", "skill", "sleep", "slice", "small",
    "smart", "smile", "smoke", "snake", "solid",
    "sound", "south", "space", "spare", "speak",
    "speed", "spend", "sport", "staff", "stage",
    "stand", "start", "state", "steam", "steel",
    "stick", "still", "stock", "stone", "store",
    "storm", "story", "style", "sugar", "super",
    "sweet", "table", "taste", "teach", "team",
    "teeth", "theme", "thing", "think", "third",
    "three", "throw", "tiger", "title", "today",
    "topic", "total", "touch", "tower", "track",
    "trade", "train", "treat", "trend", "trial",
    "trust", "truth", "uncle", "under", "union",
    "unity", "until", "upper", "upset", "usual",
    "value", "video", "visit", "voice", "waste",
    "watch", "water", "wheel", "where", "which",
    "while", "white", "whole", "whose", "woman",
    "world", "worry", "worth", "would", "write",
    "wrong", "young", "youth"
]

word = random.choice(words)

print("\n\nWelcome to Python Wordle!")
print("Guess the 5 letter word. You have 6 attempts.\n\n")

for attempt in range(6):
    guess = input(f"\nGuess {attempt + 1}/6: ").lower()

    if len(guess) != 5:
        print("Please enter exactly 5 letters.\n")
        continue

    result = ""

    for i in range(5):
        if guess[i] == word[i]:
            result += guess[i].upper()  
        elif guess[i] in word:
            result += guess[i]         
        else:
            result += "_"               

    print(result)

    if guess == word:
        print("\nYou got it!")
        break
else:
    print(f"\nYou lost! The word was: {word}")