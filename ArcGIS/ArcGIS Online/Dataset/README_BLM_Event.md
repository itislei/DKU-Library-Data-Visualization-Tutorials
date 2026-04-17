# README

## Title
Black Lives Matter (BLM) Event Dataset

---

## Description
This dataset contains information on major events and protests associated with the Black Lives Matter movement in North America. It includes event details such as titles, dates, geographic coordinates, locations, event types, estimated population exposure, and references. The dataset spans from 2013 to 2021 and covers events primarily in the United States, with one event in Canada.

---

## Data Source
This dataset was compiled from publicly available sources, including news articles (NBC News, CNN, BBC News, AP News, The Guardian, Chicago Tribune, NYTimes), Wikipedia, and other public documentation (Physicians for Human Rights, WNYC Project). Each record includes a reference link to the original source.

---

## Files

| File | Description |
|------|-------------|
| `BLM_Event.xlsx` | Excel workbook containing two sheets: `Example` (event data) and `Codebook` (attribute definitions) |

---

## Attributes (Sheet: Example)

| Attribute | Description |
|-----------|-------------|
| EVENT_TITLE | Full name or title of the event |
| EVENT_RELATED | The broader topic or movement linked to this event (all records = "Black Lives Matter") |
| DAY_START | Start date of the event (YYYY-MM-DD HH:MM:SS format) |
| DAY_END | End date of the event (YYYY-MM-DD HH:MM:SS format) |
| COUNTRY | Country where the event occurred |
| REGION | Sub-national administrative area (state/province/city) |
| LATITUDE | Geographic coordinate representing north–south position (decimal degrees, WGS84). North latitudes are positive |
| LONGITUDE | Geographic coordinate representing east–west position (decimal degrees, WGS84). West longitudes are negative |
| EVENT_TYPE | Category describing the nature of the event (e.g., Demonstration, Political violence, Digital social movement) |
| POPULATION_EXPOSURE | Estimated number of people who directly participated in or were exposed to the event |
| REFERENCE | Citation or URL link to the information source |

---

## Attributes (Sheet: Codebook)

| Item | Explanation |
|------|-------------|
| EVENT_TITLE | Full name or title of the event. |
| EVENT_RELATED | The broader topic or movement links to this event. |
| DAY_START | Exact date the event began, formatted as MM/DD/YY. |
| COUNTRY | Country where the event occurred. |
| REGION | Sub-national administrative area such as state, province, or city. |
| LATITUDE | Geographic coordinate representing the north–south position. North latitudes are positive (+), south latitudes are negative (–). |
| LONGITUDE | Geographic coordinate representing the east–west position. East longitudes are positive (+), west longitudes start with a negative sign (–). |
| EVENT_TYPE | Category describing the nature of the event. |
| POPULATION_EXPOSURE | Estimated number of people who directly participated in or were exposed to the event. |
| REFERENCE | Citation or link to the information source. |
| NOTE | Note or additional information about the data in the template. |

---

## Summary Statistics

- **Total events**: 18
- **Date range**: July 13, 2013 – March 13, 2021
- **Countries covered**: United States (17 events), Canada (1 event)
- **Event types**: Demonstration (14), Political violence (2), Digital social movement (1)

---

## Notes
- Population exposure values are estimates based on available reporting and may vary by source.
- Some events span multiple days; `DAY_START` and `DAY_END` reflect the reported duration.
- The dataset is not exhaustive and represents a curated selection of major BLM-related events.

---

## Notes on Use
This dataset is intended for research, educational, and visualization purposes. Users should verify event details with original sources when precise accuracy is required.

---

## Citation Request
If using this dataset, please cite the original sources listed in the `REFERENCE` column for each event. For the compiled dataset, cite as: "BLM Event Dataset, compiled from public news sources and documentation (2013–2021)."

---

## Archive Format
The file is provided in Excel (.xlsx) format with two sheets.
