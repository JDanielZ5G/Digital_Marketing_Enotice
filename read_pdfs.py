import fitz

files = {
    'UVP': r'C:\Users\Dell\Desktop\Digital-Marketing\UVP_group_2 (1).pdf',
    'Wireframe': r'C:\Users\Dell\Desktop\Digital-Marketing\wireframe_group_2.pdf',
    'Brand Kit': r'C:\Users\Dell\Desktop\Digital-Marketing\Group_2_Brand_kit (1).pdf',
}

for name, path in files.items():
    print(f'\n{"="*80}')
    print(f'=== {name} ===')
    doc = fitz.open(path)
    for pn, page in enumerate(doc):
        # Use raw text (not blocks) for most complete extraction
        print(f'\n--- Page {pn+1} ---')
        # Method 1: raw text
        raw = page.get_text("text")
        print("RAW:", raw[:4000])
        # Method 2: word list for exact ordering
        words = page.get_text("words")
        sentence = ' '.join([w[4] for w in words])
        print("WORDS:", sentence[:2000])
