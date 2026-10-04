"""Build the optional Excel projection of Aura XLSL."""
from __future__ import annotations
from pathlib import Path
import win32com.client as win32

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "Aura.xlsm"
VBA_SOURCE = ROOT / "vba" / "AuraHub.bas"

def main() -> None:
    if not VBA_SOURCE.exists():
        raise FileNotFoundError(VBA_SOURCE)
    excel = wb = None
    try:
        excel = win32.gencache.EnsureDispatch("Excel.Application")
        excel.Visible = False
        excel.DisplayAlerts = False
        wb = excel.Workbooks.Add()
        wb.Sheets(1).Name = "Home"
        wb.SaveAs(str(OUTPUT), FileFormat=52)
        module = wb.VBProject.VBComponents.Add(1)
        module.Name = "AuraHub"
        module.CodeModule.AddFromString(VBA_SOURCE.read_text(encoding="utf-8"))
        wb.Save()
    finally:
        if wb is not None:
            try: wb.Close(SaveChanges=True)
            except Exception: pass
        if excel is not None:
            try: excel.Quit()
            except Exception: pass
    print(f"Created {OUTPUT}")

if __name__ == "__main__":
    main()
