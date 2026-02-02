# README

## Dataset:
"China Airport Dataset with Geospatial Coordinates, 2024"

### Description:
This dataset contains 200+ airports, airstrips, and general aviation fields in China, with detailed geospatial, administrative, and operational information.

---

## Reference:
Compiled from public aviation sources and official records. Data includes airports in mainland China, Hong Kong, Macao, and Taiwan.

---

## Source:
CnOpenData
---

## Data Format:
CSV file with the following columns:

| Field Name        | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Name_EN           | English name of the airport                                                 |
| Name_CN           | Chinese name of the airport                                                 |
| LAT               | Latitude (decimal degrees, WGS84)                                           |
| LNG               | Longitude (decimal degrees, WGS84)                                          |
| Address_EN        | English address                                                             |
| Address_CN        | Chinese address                                                             |
| Province_EN       | Province/Municipality in English                                            |
| Province_CN       | Province/Municipality in Chinese                                            |
| City_EN           | City in English                                                             |
| City_CN           | City in Chinese                                                             |
| Area_EN           | District/County in English                                                  |
| Area_CN           | District/County in Chinese                                                  |
| Telephone         | Contact telephone number                                                    |
| BuiltYear         | Year of construction/opening                                                |
| BuiltMonth        | Month of construction/opening                                               |

---

## Data Dictionary:
- **Name_EN / Name_CN**: Official name of the airport in English and Chinese.
- **LAT / LNG**: Geographic coordinates suitable for mapping and GIS applications.
- **Address_EN / Address_CN**: Physical location of the airport.
- **Province/City/Area**: Hierarchical administrative divisions.
- **Telephone**: Contact number for airport information.
- **BuiltYear / BuiltMonth**: Historical data on airport establishment.

---

## Notes:
- Some fields may be empty where data is unavailable.
- Coordinates are approximate and intended for general mapping.
- Data includes civilian, military, and general aviation facilities.

---

## File:
`China Airport Dataset.csv`
