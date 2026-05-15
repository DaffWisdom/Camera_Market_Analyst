import pandas as pd

# ==========================================
# 1. LOAD RAW DATA
# ==========================================
try:
    df = pd.read_csv('used_camera_canon_r50_raw.csv')
    print("--- FIRST 5 ROWS OF RAW DATA ---")
    print(df.head())
except FileNotFoundError:
    print("Error: The raw CSV file was not found. Please run test_scraper.py first.")
    exit()

# ==========================================
# 2. DATA CLEANING (Price Column)
# ==========================================
# Remove currency symbols (" đ") and thousand separators (".")
df['Price'] = df['Price'].str.replace(' đ', '', regex=False)
df['Price'] = df['Price'].str.replace('.', '', regex=False)

# Convert the cleaned string into a numeric format, coercing errors to NaN
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Drop rows where Price could not be parsed (e.g., "Liên hệ")
df = df.dropna(subset=['Price'])
df['Price'] = df['Price'].astype(int)

# ==========================================
# 3. FEATURE ENGINEERING
# ==========================================

# Define a more robust Regex pattern for Vietnamese camera accessories
# Catches: kit, 18-45, lens, ống kính (lens in VN), kèm (includes), ...
kit_pattern = r'kit|lens|ống\s*kính|18[- ]?45|15[- ]?45|kèm\s*theo|rfs'

# Apply the pattern. 
df['Includes_Kit'] = df['Product_Name'].str.lower().str.contains(kit_pattern, regex=True, na=False)

# Optional: You can create a quick verification to see the result directly in the terminal
print("\n--- VERIFYING 'Includes_Kit' LOGIC ---")
# Filter and show only the rows where Includes_Kit is False to check if we missed any
missing_kits = df[df['Includes_Kit'] == False][['Product_Name', 'Includes_Kit']]
print("Products marked as NO KIT (Body only):")
print(missing_kits.head(10))

# ==========================================
# 3. FEATURE ENGINEERING (Continued)
# ==========================================

# Feature 2: Camera Condition (e.g., 99%, 95%, Like New)
# Pattern logic:
# \d{2}%      -> Matches exactly two digits followed by a percent sign (e.g., 99%, 98%)
# like\s*new  -> Matches "like new" or "likenew"
# mới|lướt    -> Matches "mới" (new) or "lướt" (gently used)
condition_pattern = r'(\d{2}%|like\s*new|mới|lướt|chính\s*hãng)'

# Extract the pattern.
df['Condition'] = df['Product_Name'].str.lower().str.extract(condition_pattern)[0]

# Standardize the extracted text
df['Condition'] = df['Condition'].str.replace(r'like\s*new', 'Like New', regex=True)
df['Condition'] = df['Condition'].str.replace('mới', 'New/Like New', regex=False)
df['Condition'] = df['Condition'].str.replace('lướt', 'Gently Used', regex=False)
df['Condition'] = df['Condition'].str.replace('chính hãng', 'Official VN', regex=False)

# For products that don't mention condition in the title, fill the empty values (NaN) with 'Unknown'
df['Condition'] = df['Condition'].fillna('Unknown')

print("\n--- VERIFYING 'Condition' EXTRACTION ---")
# Count how many of each condition we found
print(df['Condition'].value_counts())

# ==========================================
# 3. FEATURE ENGINEERING (Refined)
# ==========================================

# Feature 3: Is it Fullbox?
# Check if the title mentions 'fullbox' or 'full box'
fullbox_pattern = r'fullbox|full\s*box'
df['Is_Fullbox'] = df['Product_Name'].str.lower().str.contains(fullbox_pattern, regex=True, na=False)

# Optional: Print to check the overlap between Kit and Fullbox
print("\n--- CHECKING FULLBOX vs KIT ---")
# Count how many products are Fullbox but were previously marked as No Kit
hidden_kits = df[(df['Is_Fullbox'] == True) & (df['Includes_Kit'] == False)]
print(f"Found {len(hidden_kits)} 'Fullbox' cameras that might be hiding a Kit lens!")

# ==========================================
# 4. EXPORT CLEANED DATA
# ==========================================
df.to_csv('used_camera_canon_r50_cleaned.csv', index=False, encoding='utf-8-sig')
print("\n✅ Data cleaning completed! Saved to 'used_camera_canon_r50_cleaned.csv'.")