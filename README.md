# Tankini Sanskrit IME (टङ्किनी संस्कृतम्)

[![Keyman](https://img.shields.io/badge/Keyman-10.0%2B-blue.svg)](https://keyman.com/)
[![KeymanWeb](https://img.shields.io/badge/KeymanWeb-18.0%2B-informational.svg)](https://keymanweb.com/)
[![Tests](https://img.shields.io/badge/Tests-816%2F816%20Passing%20(100%25)-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)]()

**Tankini Sanskrit IME** is a high-performance, ergonomic phonetic Input Method Engine (IME) crafted for classical and Vedic Sanskrit. Built upon the Keyman Engine architecture, Tankini provides natural Latin-to-Devanagari typing across Desktop (macOS, Windows, Linux), Mobile (iOS, Android), and the Web.

---

## 🌟 Key Highlights

- **Smart Latin Buffer Engine**: Consonant keys are buffered dynamically with real-time Latin preview, committing into Devanagari halant (`्`), full consonants, or complex conjuncts seamlessly without requiring manual virama keystrokes.
- **Full Vedic Svara Support**: Dedicated, collision-free keystrokes for Vedic accents—Anudatta (`Z`), Svarita (`X`), and Deergha Svarita (`XX`).
- **Intuitive Dual Mappings**: Natural, mnemonic key sequences inspired by standard ITRANS and Harvard-Kyoto (e.g., `A` / `aa`, `I` / `ii` / `ee`, `U` / `uu` / `oo`, `K` / `kh`, `G` / `gh`).
- **Homorganic Nasal Intelligence**: Automatic phonetic assimilation for velar and palatal nasals (`ng` → `ङ्`, `nj` → `ञ्`), including compound conjunct handling (`ngx` → `ङ्क्ष`).
- **Compound Word & Punctuation Support**: Hyphenation (`-`), parentheses (`()`), danda (`.`), and double danda (`..`) cleanly commit active consonant buffers with halant preservation.
- **100% Test Verified**: Comprehensive 816-test suite covering edge cases, ligature formations, Vedic accents, and classical shloka corpora.

---

## 📖 Phonetic Mapping Reference

### 1. Independent Vowels (स्वर)

| Devanagari | Keystroke(s) | Description |
|:---:|:---|:---|
| **अ** | `a` | Hrasva A |
| **आ** | `aa`, `A` | Deergha A |
| **इ** | `i` | Hrasva I |
| **ई** | `ii`, `I`, `ee` | Deergha I |
| **उ** | `u` | Hrasva U |
| **ऊ** | `uu`, `U`, `oo` | Deergha U |
| **ऋ** | `R` | Vocalic R |
| **ॠ** | `RR` | Long Vocalic R |
| **ऌ** | `lR` | Vocalic L |
| **ॡ** | `lRR` | Long Vocalic L |
| **ए** | `e`, `E` | E |
| **ऐ** | `ai` | AI |
| **ओ** | `o`, `O` | O |
| **औ** | `au` | AU |

### 2. Modifiers (अयोगवाह)

| Devanagari | Keystroke(s) | Description |
|:---:|:---|:---|
| **ं** | `M` | Anusvara |
| **ः** | `H` | Visarga |
| **ँ** | `M.` | Candrabindu |

### 3. Consonants (व्यञ्जन)

#### कण्ठ्य (Gutturals / Velars)
| Devanagari | Keystroke(s) |
|:---:|:---|
| **क** | `k` + `a` |
| **ख** | `kh`, `K` + `a` |
| **ग** | `g` + `a` |
| **घ** | `gh`, `G` + `a` |
| **ङ** | `ng` + `a` |

#### तालव्य (Palatals)
| Devanagari | Keystroke(s) |
|:---:|:---|
| **च** | `c` + `a` |
| **छ** | `ch`, `C` + `a` |
| **ज** | `j` + `a` |
| **झ** | `jh`, `J` + `a` |
| **ञ** | `nj`, `Y` + `a` |

#### मूर्धन्य (Retroflex / Cerebrals)
| Devanagari | Keystroke(s) |
|:---:|:---|
| **ट** | `T` + `a` |
| **ठ** | `Th` + `a` |
| **ड** | `D` + `a` |
| **ढ** | `Dh` + `a` |
| **ण** | `N` + `a` |

#### दन्त्य (Dentals)
| Devanagari | Keystroke(s) |
|:---:|:---|
| **त** | `t` + `a` |
| **थ** | `th` + `a` |
| **द** | `d` + `a` |
| **ध** | `dh` + `a` |
| **न** | `n` + `a` |

#### ओष्ठ्य (Labials)
| Devanagari | Keystroke(s) |
|:---:|:---|
| **प** | `p` + `a` |
| **फ** | `ph`, `P` + `a` |
| **ब** | `b` + `a` |
| **भ** | `bh`, `B` + `a` |
| **म** | `m` + `a` |

#### अन्तःस्थ (Semi-vowels)
| Devanagari | Keystroke(s) |
|:---:|:---|
| **य** | `y` + `a` |
| **र** | `r` + `a` |
| **ल** | `l` + `a` |
| **ळ** | `L` + `a` |
| **व** | `v`, `w` + `a` |

#### ऊष्मन् (Sibilants & Aspirate)
| Devanagari | Keystroke(s) |
|:---:|:---|
| **श** | `sh`, `S` + `a` |
| **ष** | `Sh`, `shh` + `a` |
| **स** | `s` + `a` |
| **ह** | `h` + `a` |

### 4. Special Conjuncts (संयुक्त)

| Devanagari | Keystroke(s) | Example |
|:---:|:---|:---|
| **क्ष** | `x` + `a` | `kSa` or `xa` → **क्ष** |
| **ज्ञ** | `gY`, `jY` + `a` | `jYa` or `gYa` → **ज्ञ** |
| **ङ्क्ष** | `ngx` + `a` | `kAngxitArthadA` → **काङ्क्षितार्थदा** |

### 5. Vedic Accents (वैदिकस्वराः)

| Accent | Unicode | Keystroke | Description |
|:---:|:---:|:---:|:---|
| **॒** | `U+0952` | `Z` | Anudatta (अनुदात्तः - horizontal line below) |
| **॑** | `U+0951` | `X` | Svarita (स्वरितः - vertical line above) |
| **᳚** | `U+1CDA` | `XX` | Deergha Svarita (दीर्घस्वरितः - double vertical line) |

### 6. Special Symbols & Punctuation

| Symbol | Meaning | Keystroke(s) |
|:---:|:---|:---|
| **ॐ** | Pranava (Om) | `OM`, `AUM` |
| **।** | Danda (Single) | `.` |
| **॥** | Double Danda | `..` |
| **ऽ** | Avagraha | `.a` |
| **॰** | Abbreviation Sign | `q` |
| **-** | Compound Hyphen | `-` (commits preceding consonant with halant) |
| **()** | Parentheses | `()`, `)` (commits preceding consonant with halant) |
| **\\** | Explicit Virama | `\` |

### 7. Devanagari Numerals (संख्याः)

| ० | १ | २ | ३ | ४ | ५ | ६ | ७ | ८ | ९ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` |

---

## 🏗️ Repository Structure

```
Tankini-IME/
├── README.md                           # Comprehensive documentation and mapping reference
├── layout-paln.txt                     # Canonical keyboard specification and layout design
├── .gitignore                          # Git ignore definitions
├── keyman/
│   ├── source/
│   │   ├── tankini_sanskrit.kmn        # Primary Keyman source code (13 rule sections)
│   │   ├── tankini_sanskrit.kps        # Keyman package source specification
│   │   ├── tankini_sanskrit.kvks       # On-Screen Visual Keyboard specification
│   │   ├── tankini_sanskrit.keyman-touch-layout # Touch layout definitions for mobile/tablet
│   │   ├── readme.htm                  # Package documentation
│   │   └── welcome.htm                 # User onboarding guide
│   ├── build/
│   │   ├── tankini_sanskrit.kmx        # Compiled binary for Desktop (Windows, macOS, Linux)
│   │   ├── tankini_sanskrit.js         # Compiled engine for KeymanWeb
│   │   ├── tankini_sanskrit.kmp        # Distributable installer package
│   │   └── tankini_sanskrit.kvk        # Compiled visual keyboard data
│   └── tests/
│       ├── index.html                  # Interactive test suite UI & visual verification runner
│       ├── run_tests_headless.js       # Playwright-based headless Chrome automated runner
│       ├── generate_tests.py           # Corpus-driven test generator
│       ├── test_cases.json             # 816 compiled test assertions
│       └── test.txt                    # Raw classical Sanskrit corpus source text
└── Mudgala-IME/                        # Legacy standalone IME engine and script conversion tables
    ├── Mudgala By Neelakantha Shastri.exe # Legacy Windows binary
    ├── input_phonetic.txt              # Phonetic input tables
    ├── output_devanagari.txt           # Devanagari output mappings
    ├── output_grantha.txt              # Grantha script mappings
    ├── output_tamil.txt                # Tamil script mappings
    └── output_roman.txt                # Roman transliteration mappings
```

---

## 🛠️ Building & Compiling

### Prerequisites

- [Keyman Developer CLI (`kmc`)](https://keyman.com/developer/):
  ```bash
  # Installed via npm / Homebrew
  npm install -g @keymanapp/kmc
  # Or via Homebrew
  brew install keyman-developer
  ```

### Build Targets

```bash
# 1. Compile Desktop/Mobile binary (.kmx)
kmc build keyman/source/tankini_sanskrit.kmn -o keyman/build/tankini_sanskrit.kmx

# 2. Compile KeymanWeb binary (.js)
kmc build keyman/source/tankini_sanskrit.kmn -o keyman/build/tankini_sanskrit.js

# 3. Compile Keyman Package installer (.kmp)
kmc build keyman/source/tankini_sanskrit.kps -o keyman/build/tankini_sanskrit.kmp
```

---

## 🧪 Testing & Verification

Tankini includes an extensive automated test suite covering all 55 character groups and phonological combinations:

- **152 Manual Test Cases**: Granular validation of buffer states, deadkeys, aspirate deduplications, homorganic nasals, and Vedic accents.
- **664 Corpus Test Cases**: Real-world classical Sanskrit words and sentences extracted from canonical literature.
- **100% Pass Rate**: Verified via headless browser automation.

To run the test suite locally:

```bash
# 1. Start a local HTTP server
python3 -m http.server 8765 --directory keyman

# 2. Open tests in your browser
open http://localhost:8765/tests/index.html
```

---

## 👤 Author & Acknowledgements

- **Author**: Neelakantha Shastri ([@shastravid](https://github.com/shastravid))
- **Copyright**: © 2026 Neelakantha Shastri. All rights reserved.
