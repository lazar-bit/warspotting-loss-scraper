# Russian Equipment Losses (WarSpotting API Data Extractor)

This Python script downloads and saves documented Russian equipment losses from the open-source [WarSpotting.net](https://ukr.warspotting.net) API into an Excel file for further analysis and research.

---

## Features

* Fetches equipment loss data for each day from February 24, 2022 onward
* Based on **WarSpotting.net's official API**
* Outputs data into a structured `.xlsx` (Excel) file
* Includes type, model, location, unit (if known), etc...

---

## ⚠️ Limitations & Disclaimers

* ⚠️ Due to API limitations, the script retrieves a maximum of 100 records per day
  → This does not significantly affect analytical value but should be noted.
* Only Russian losses** are accessible through the API; Ukrainian data is not available
* The script includes polite delays between each request to prevent overloading the API
* Built entirely on WarSpotting.net’s public API – credit to them for maintaining this invaluable source
* 🧪 This project is for **research and educational purposes only**

---

## How It Works

1. You set a date range
2. The script queries the WarSpotting API one day at a time
3. For each day, it downloads up to 100 loss records
4. Adds a delay between each request to respect the API's limits
5. Saves the result to `warspotting_losses.xlsx` with all relevant data

---

## Example Output Columns

* `id`
* `date`
* `type`
* `model`
* `status`
* `lost_by`
* `nearest_location`
* `geo`
* `unit`
* `tags`
* `comment`
* `sources`
* `photos`

---

## Requirements

* Python 3.x
* `requests`
* `openpyxl`

Install them via:

```bash
pip install requests openpyxl
```

---

## License

This project is licensed under the **MIT License** — see the `LICENSE` file for details.

---

## Acknowledgments

* API and data provided by [WarSpotting.net](https://ukr.warspotting.net)
* Built by Zsolt Lazar for academic and open-source research
