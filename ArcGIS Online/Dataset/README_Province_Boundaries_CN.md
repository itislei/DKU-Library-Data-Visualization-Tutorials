# README

## Dataset:
"China Province Boundaries (Vector Data)"

### Description:
This dataset contains the administrative boundaries of Chinese provinces, autonomous regions, municipalities, and special administrative regions in ESRI shapefile format.

---

## Data Source:
CnOpenData

---

## Data Format:
Zipped shapefile bundle (`China_Province_Boundaries.zip`) containing:
- `.shp` (geometry)
- `.shx` (index)
- `.dbf` (attributes)
- `.prj` (coordinate system)
- `.cpg` (character encoding)

---

## Attribute Table Fields:
| Field Name      | Description                                      |
|-----------------|--------------------------------------------------|
| PROV_EN         | Province name in English                         |
| PROV_CN         | Province name in Chinese                         |
| PROV_CODE       | Administrative division code                     |
| CAPITAL_EN      | Capital city name in English                     |
| CAPITAL_CN      | Capital city name in Chinese                     |
| TYPE            | Type (Province, Municipality, Autonomous Region) |
| AREA_SQKM       | Approximate area in square kilometers            |

---

## Coordinate System:
- **Projection**: WGS 84 / Pseudo-Mercator (EPSG:3857) or Geographic (EPSG:4326)
- **Units**: Decimal degrees or meters depending on projection.

---

## Use Cases:
- Thematic mapping
- Administrative analysis
- Regional planning
- Cartographic visualization

---

## File:
`China_Province_Boundaries.zip`
