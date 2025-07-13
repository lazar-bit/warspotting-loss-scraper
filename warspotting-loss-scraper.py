import requests
import datetime
import time
import openpyxl


START_DATE = datetime.date(2022, 2, 24)          # first day to pull
END_DATE   = datetime.date(2022, 2, 28)          # last day to pull or CHANGE to datetime.date.today()
BELLIGERENT = "russia"                           
BASE_URL   = "https://ukr.warspotting.net/api"   # domain
HEADERS    = {"User-Agent": "WarSpotClient/1.0 (contact@example.com)"}
SLEEP_BETWEEN_DATES = 0.5    # delay between days
OUTFILE    = "warspotting_losses.xlsx"

def fetch_day_one_page(date_str: str, belligerent: str):
    """Fetch just one page of losses for a given day."""
    url = f"{BASE_URL}/losses/{belligerent}/{date_str}"
    print(f"  ↳ {url}")
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        if r.status_code == 404:
            print(f"    No data for {date_str} (404).")
            return []
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"    Request error: {e}")
        return []

    losses = r.json().get("losses", [])
    return losses

def flatten(e: dict) -> dict:
    """Flatten the API record into a row-friendly dict."""
    return {
        "id"              : e.get("id"),
        "date"            : e.get("date"),
        "type"            : e.get("type"),
        "model"           : e.get("model"),
        "status"          : e.get("status"),
        "lost_by"         : e.get("lost_by"),
        "nearest_location": e.get("nearest_location"),
        "geo"             : e.get("geo"),
        "unit"            : e.get("unit"),
        "tags"            : e.get("tags"),
        "comment"         : e.get("comment"),
        "sources"         : ", ".join(e.get("sources", []))
                            if isinstance(e.get("sources"), list) else e.get("sources"),
        "photos"          : ", ".join(e.get("photos", []))
                            if isinstance(e.get("photos"), list) else e.get("photos"),
    }

def main():
    wb, ws = openpyxl.Workbook(), None
    current = START_DATE
    total_rows = 0

    while current <= END_DATE:
        ds = current.isoformat()
        print(f"Fetching {ds} …")
        day_records = fetch_day_one_page(ds, BELLIGERENT)
        if day_records:
            if ws is None:
                ws = wb.active
                ws.title = "Losses"
                ws.append(list(flatten(day_records[0]).keys()))
            for rec in day_records:
                ws.append(list(flatten(rec).values()))
            total_rows += len(day_records)
            print(f"    {len(day_records)} records.")
        else:
            print("    0 records.")
        current += datetime.timedelta(days=1)
        time.sleep(SLEEP_BETWEEN_DATES)

    if ws is None:
        print("No data fetched at all.")
    else:
        wb.save(OUTFILE)
        print(f"\nDONE – {total_rows} total records saved to {OUTFILE}")

if __name__ == "__main__":
    main()
