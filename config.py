from pathlib import Path

#To create a clear folder/file structure for the future, we use the pathlib library and anchor all path to fixed point
ROOT = Path(__file__).parent

DATA_FILE = ROOT / "data" / "findata-m5KLx91yPatZlJqV.xlsx"
DB_FILE   = ROOT / "db" / "financial.db"

print("Done!")
