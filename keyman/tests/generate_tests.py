import json
import os

# ============================================================================
# Tankini Sanskrit Test Case Generator
# Converts Devanagari text → Tankini phonetic input sequences
# ============================================================================

# Vowels (Independent)
vowels = {
    'अ': 'a', 'आ': 'A', 'इ': 'i', 'ई': 'I', 'उ': 'u', 'ऊ': 'U',
    'ऋ': 'R', 'ॠ': 'RR', 'ऌ': 'lR', 'ॡ': 'lRR',
    'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
    'ं': 'M', 'ः': 'H', 'ँ': 'M.', 'ऽ': '.a'
}

# Consonants (multi-char checked first via ordered iteration)
consonants_ordered = [
    ('क्ष', 'x'), ('ज्ञ', 'jY'),
    ('क', 'k'), ('ख', 'K'), ('ग', 'g'), ('घ', 'G'), ('ङ', 'ng'),
    ('च', 'c'), ('छ', 'C'), ('ज', 'j'), ('झ', 'J'), ('ञ', 'Y'),
    ('ट', 'T'), ('ठ', 'Th'), ('ड', 'D'), ('ढ', 'Dh'), ('ण', 'N'),
    ('त', 't'), ('थ', 'th'), ('द', 'd'), ('ध', 'dh'), ('न', 'n'),
    ('प', 'p'), ('फ', 'P'), ('ब', 'b'), ('भ', 'B'), ('म', 'm'),
    ('य', 'y'), ('र', 'r'), ('ल', 'l'), ('ळ', 'L'), ('व', 'v'),
    ('श', 'S'), ('ष', 'Sh'), ('स', 's'), ('ह', 'h'),
]
consonants = dict(consonants_ordered)

# Matras (vowel signs on consonants)
matras = {
    'ा': 'A', 'ि': 'i', 'ी': 'I', 'ु': 'u', 'ू': 'U',
    'ृ': 'R', 'ॄ': 'RR', 'ॢ': 'lR', 'ॣ': 'lRR',
    'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au'
}

# Special characters
special = {
    '०': '0', '१': '1', '२': '2', '३': '3', '४': '4',
    '५': '5', '६': '6', '७': '7', '८': '8', '९': '9',
    '।': '.', '॥': '..', 'ॐ': 'OM',
    '॰': 'q', '॒': 'Z', '॑': 'X', '᳚': 'XX',
}


def convert_line(line):
    """Convert a Devanagari string to Tankini phonetic input sequence."""
    # Strip ZWJ/ZWNJ
    line = line.replace('\u200d', '').replace('\u200c', '')

    res = ""
    i = 0
    chars = list(line)

    while i < len(chars):
        char = chars[i]

        # Check Special / Numbers / Punctuation
        if char in special:
            res += special[char]
            i += 1
            continue

        # Check two-char vowels first (ऐ, औ are single chars so this is fine)
        if char in vowels:
            res += vowels[char]
            i += 1
            continue

        # Check multi-char consonants (क्ष, ज्ञ)
        found = False
        for deva, latin in consonants_ordered:
            if len(deva) > 1 and ''.join(chars[i:i+len(deva)]) == deva:
                res += latin
                i += len(deva)
                # Look ahead for matra or halant
                if i < len(chars):
                    next_char = chars[i]
                    if next_char in matras:
                        res += matras[next_char]
                        i += 1
                    elif next_char == '्':
                        # Halant — skip it (consonant cluster continues)
                        i += 1
                    else:
                        # Inherent vowel 'a'
                        res += 'a'
                else:
                    res += 'a'
                found = True
                break

        if found:
            continue

        # Check single-char consonants
        if char in consonants:
            res += consonants[char]

            # Look ahead
            if i + 1 < len(chars):
                next_char = chars[i + 1]
                if next_char in matras:
                    res += matras[next_char]
                    i += 2
                    continue
                elif next_char == '्':
                    # Halant — consonant cluster
                    i += 2
                    continue
                else:
                    # Inherent vowel 'a'
                    res += 'a'
                    i += 1
                    continue
            else:
                # End of string — inherent 'a'
                res += 'a'
                i += 1
                continue

        # Fallback for whitespace or unknown
        res += char
        i += 1

    return res


def generate_variants(canonical_seq):
    """Generate alternative input sequences (aa/ee/oo variants)."""
    alt = ""
    changed = False
    i = 0

    while i < len(canonical_seq):
        char = canonical_seq[i]
        nxt = canonical_seq[i + 1] if i + 1 < len(canonical_seq) else None

        if char == 'A' and nxt != 'U' and nxt != 'a':
            # A -> aa (but not AU which is a different thing)
            alt += 'aa'
            changed = True
        elif char == 'I':
            alt += 'ee'
            changed = True
        elif char == 'U':
            alt += 'oo'
            changed = True
        elif char == 'j' and nxt == 'Y':
            alt += 'gY'
            changed = True
            i += 2
            continue
        else:
            alt += char
        i += 1

    return alt if changed else None


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, 'test.txt')
    output_path = os.path.join(base_dir, 'test_cases.json')

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    test_cases = []

    # Pre-clean ZWJ/ZWNJ
    cleaned_lines = []
    for line in lines:
        l = line.strip().replace('\u200d', '').replace('\u200c', '')
        if l:
            cleaned_lines.append(l)

    for line in cleaned_lines:
        canonical = convert_line(line)

        if canonical:
            test_cases.append({
                "seq": canonical,
                "expect": line,
                "desc": f"Line (Canon): {line[:15]}..."
            })

            # Alternative Input
            alt = generate_variants(canonical)
            if alt:
                test_cases.append({
                    "seq": alt,
                    "expect": line,
                    "desc": f"Line (Alt): {line[:15]}..."
                })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(test_cases, f, indent=2, ensure_ascii=False)

    print(f"Generated {len(test_cases)} test cases.")


if __name__ == "__main__":
    main()
