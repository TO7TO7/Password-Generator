import random
import re

def leet_convert(word):
    word = re.sub(r'gh', '8', word, flags=re.IGNORECASE)
    word = re.sub(r'a', '@', word, flags=re.IGNORECASE)
    word = re.sub(r'[il]', '!', word, flags=re.IGNORECASE)
    word = re.sub(r's', '$', word, flags=re.IGNORECASE)
    word = re.sub(r'o', '0', word, flags=re.IGNORECASE)
    word = re.sub(r'e', '3', word, flags=re.IGNORECASE)
    return word

specials = ['@', '#', '!', '$', '%', '&', '*', '-', '_']

def get_user_inputs():
    nickname = input("victem name: ").strip()
    number = input("numbers: ").strip()
    word = input("second name: ").strip()

    extra_inputs = []
    more = input("any info (y/n): ").strip().lower()
    if more == 'y':
        print("write info (for stop press Enter):")
        while True:
            item = input("more info: ").strip()
            if item == "":
                break
            extra_inputs.append(item)

    return nickname, number, word, extra_inputs

def generate_passwords(nickname, number, word='', extras=[], count=1000000, max_length=16):
    passwords = set()
    nickname = nickname.strip()
    number = number.strip()

    inputs = [nickname, word] + extras
    inputs = [i.capitalize() for i in inputs if i]

    full_parts = []
    for part in inputs:
        full_parts.append(part)
        full_parts.append(leet_convert(part))

    full_parts.append(number)

    print(f"[*] input number leet: {len(full_parts)}")

    while len(passwords) < count - 4:
        parts = random.sample(full_parts, k=random.randint(2, min(4, len(full_parts))))
        random.shuffle(parts)
        base = ''.join(parts)

        sp1 = random.choice(specials)
        sp2 = random.choice(specials)

        formats = [
            f"{base}{sp1}{sp2}",
            f"{sp1}{base}{sp2}",
            f"{base}{sp1}_{sp2}",
            f"{base}_{sp1}{sp2}",
            f"{base[:len(base)//2]}{sp1}{base[len(base)//2:]}{sp2}",
            f"{base}{random.randint(0, 9999)}{sp1}{sp2}",
            f"{sp1}{base[:3]}{sp2}{random.choice(full_parts)}",
            f"{base.lower()}{sp1}{random.choice(specials)}{random.randint(100, 999)}",
            f"{base.upper()}{sp2}{sp1}{random.choice(['2024', '123', '000'])}"
        ]

        for pwd in formats:
            if len(pwd) <= max_length:
                passwords.add(pwd)

        if len(passwords) % 100000 == 0:
            print(f"[+] generate {len(passwords)} password...")

    cap = nickname.capitalize()
    passwords.update([
        f"{cap}_{number}@@",
        f"{leet_convert(cap)}_{number}@@",
        f"{cap}_{number}!!",
        f"{cap}{number}@!",
    ])

    return passwords

nickname, number, word, extras = get_user_inputs()
if not nickname or not number:
    print("Error in victim name or number.")
else:
    passwords = generate_passwords(nickname, number, word, extras)
    with open("leet_passwords.txt", "w", encoding="utf-8") as f:
        for pwd in passwords:
            f.write(pwd + "\n")
    print(f"Successful file: leet_passwords.txt ✅")
