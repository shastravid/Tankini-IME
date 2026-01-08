import json
import os

base_dir = "/Users/shastravid/Antigravity/Tankini-IME/keyman/tests"
json_path = os.path.join(base_dir, "test_cases.json")
txt_path = os.path.join(base_dir, "test.txt")

print(f"Reading from {json_path}")
try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    lines = []
    seen = set()
    for item in data:
        if "Line (Canon)" in item.get('desc', ''):
            expect = item['expect']
            if expect not in seen:
                lines.append(expect)
                seen.add(expect)
    
    if not lines:
        print("No lines found in JSON to extract!")
    else:
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"Successfully extracted {len(lines)} lines to {txt_path}")

except Exception as e:
    print(f"Error: {e}")
