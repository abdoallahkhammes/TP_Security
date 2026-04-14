import secrets

# Diceware word list (shortened example – use full list in production)
DICEWARE_WORDLIST = [
    "apple", "moon", "cloud", "storm", "brave", "tiger", "forest", "light",
    "stone", "flame", "ocean", "thunder", "silver", "golden", "phoenix"
]

def generate_passphrase(num_words=6, separator="-"):
    if len(DICEWARE_WORDLIST) < num_words:
        raise ValueError("Not enough words in wordlist")
    # CSPRNG selection
    chosen = [secrets.choice(DICEWARE_WORDLIST) for _ in range(num_words)]
    return separator.join(chosen)

if __name__ == "__main__":
    print(generate_passphrase(5, " "))