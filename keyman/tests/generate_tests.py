import json
import re

# Mapping based on layout-paln.txt and kmn implementation

vowels = {
    'अ': 'a', 'आ': 'A', 'इ': 'i', 'ई': 'I', 'उ': 'u', 'ऊ': 'U',
    'ऋ': 'R', 'ॠ': 'RR', 'ऌ': 'lR', 'ॡ': 'lRR',
    'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
    'ं': 'M', 'ः': 'H', 'ँ': 'M.', 'ऽ': '.a'
}

consonants = {
    'क': 'k', 'ख': 'K', 'ग': 'g', 'घ': 'G', 'ङ': 'ng',
    'च': 'c', 'छ': 'C', 'ज': 'j', 'झ': 'J', 'ञ': 'Y',
    'ट': 'T', 'ठ': 'Th', 'ड': 'D', 'ढ': 'Dh', 'ण': 'N',
    'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
    'प': 'p', 'फ': 'P', 'ब': 'b', 'भ': 'B', 'म': 'm',
    'य': 'y', 'र': 'r', 'ल': 'l', 'ळ': 'L', 'व': 'v',
    'श': 'S', 'ष': 'Sh', 'स': 's', 'ह': 'h',
    'क्ष': 'x', 'ज्ञ': 'jY'
}

matras = {
    'ा': 'A', 'ि': 'i', 'ी': 'I', 'ु': 'u', 'ू': 'U',
    'ृ': 'R', 'ॄ': 'RR', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au'
}

special = {
    '०': '0', '१': '1', '२': '2', '३': '3', '४': '4',
    '५': '5', '६': '6', '७': '7', '८': '8', '९': '9',
    '।': '.', '॥': '..', 'ॐ': 'OM',
    '॰': 'q', '॒': '_', '॑': 'X', '᳚': 'XX',
    '\u200d': '', '\u200c': ''
}

# Consonant Map - Updated for Tankini Sanskrit
# Specific mappings that match our KMN explicit rules
consonants = {
    'क': 'k', 'ख': 'K', 'ग': 'g', 'घ': 'G', 'ङ': 'ng',
    'च': 'c', 'छ': 'C', 'ज': 'j', 'झ': 'J', 'ञ': 'Y',
    'ट': 'T', 'ठ': 'Th', 'ड': 'D', 'ढ': 'Dh', 'ण': 'N',
    'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
    'प': 'p', 'फ': 'P', 'ब': 'b', 'भ': 'B', 'म': 'm',
    'य': 'y', 'र': 'r', 'ल': 'l', 'ळ': 'L', 'व': 'v',
    'श': 'S', 'ष': 'Sh', 'स': 's', 'ह': 'h',
    'क्ष': 'x', 'ज्ञ': 'jY', 'ऌ': 'lR'
}

def convert_line(line):
    # Strip ZWJ/ZWNJ
    line = line.replace('\u200d', '').replace('\u200c', '')
    
    res = ""
    i = 0
    k_chars = list(line)
    
    while i < len(k_chars):
        char = k_chars[i]
        
        # Check Special / Numbers / Punctuation
        if char in special:
            res += special[char]
            i += 1
            continue
            
        # Check Vowels (Independent)
        if char in vowels:
            res += vowels[char]
            i += 1
            continue
            
        # Check Consonants
        if char in consonants:
            res += consonants[char]
            
            # Look ahead
            if i + 1 < len(k_chars):
                next_char = k_chars[i+1]
                
                if next_char in matras:
                    # Consonant (Halant) + Matra -> Consonant + Matra Key
                    # Keyboard Rule: Halant + Matra -> Matra (replacing halant)
                    res += matras[next_char]
                    i += 2
                    continue
                elif next_char == '्':
                    # Consonant + Halant
                    # Keyboard produces Halant by default.
                    # So 'k' -> 'क्'. Matches 'k' + '्' visually.
                    # We just skip the halant char in input processing.
                    i += 2 
                    continue
                else:
                    # Consonant + Something Else (Space, Consonant, Punctuation)
                    # Means Inherent Vowel "a" or just the next Consonant.
                    
                    # Wait, if next is Consonant?
                    # 'k' 't' -> 'क्' 't' -> 'kt' -> 'क्त'. 
                    # So we DON'T add 'a' if next is consonant?
                    # NO. If text is 'क' 'ta', then 'k' 'a' 't' 'a'.
                    # If text is 'क्' 'ta', then 'k' 't' 'a'.
                    
                    # My logic here is processing DEVANAGARI source.
                    # source 'क' means we MUST type 'k' + 'a' to get 'क' (remove default halant).
                    # source 'क्' (handled by elif == '्') means we type 'k' and leave it.
                    
                    res += 'a'
                    i += 1
                    continue
            else:
                # End of string Consonant 'क' -> Needs 'a'
                res += 'a'
                i += 1
                continue
        
        # Fallback for whitespace or unknown
        res += char
        i += 1
        
    return res

def generate_variants(canonical_seq):
    # Determine variants based on known patterns
    # A -> aa
    # I -> ii | ee
    # U -> uu | oo
    # This is a simple permuter that generates ONE alt sequence if possible
    
    alt = ""
    changed = False
    i = 0
    k_chars = canonical_seq # String input
    
    # We navigate strings, but A, I, U might be part of other things?
    # Our map outputs are single or double chars 'A', 'ai', 'U'.
    # We iterate and substitute.
    
    while i < len(k_chars):
        char = k_chars[i]
        nxt = k_chars[i+1] if i+1 < len(k_chars) else None
        
        # Check specific mapped output characters from convert_line
        if char == 'A':
            alt += 'aa'
            changed = True
        elif char == 'I':
            alt += 'ee' # Variant 1
            changed = True
        elif char == 'U':
            alt += 'oo' # Variant 1
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
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, 'test.txt')
    output_path = os.path.join(base_dir, 'test_cases.json')
    
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    test_cases = []
    
    # Pre-clean expected ZWJ/ZWNJ globally
    cleaned_lines = []
    for line in lines:
        l = line.strip().replace('\u200d', '').replace('\u200c', '')
        if l:
            cleaned_lines.append(l)

    for line in cleaned_lines:
        # Canonical Input
        canonical = convert_line(line)
        
        if canonical:
            test_cases.append({
                "seq": canonical,
                "expect": line,
                "desc": f"Line (Canon): {line[:10]}..."
            })
            
            # Alternative Input (One variant strategy: aa/ee/oo)
            alt = generate_variants(canonical)
            if alt:
                 test_cases.append({
                    "seq": alt,
                    "expect": line,
                    "desc": f"Line (Alt): {line[:10]}..."
                })
            
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(test_cases, f, indent=2, ensure_ascii=False)
        
    print(f"Generated {len(test_cases)} test cases.")

if __name__ == "__main__":
    main()
