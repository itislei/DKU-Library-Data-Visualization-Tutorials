# README

## Title
edges

### Description:
This dataset contains edge (relationship) data for a character network from the Sherlock Holmes series. It represents connections between characters with relationship types and strength weights.

---

## Data Sources
`edges.csv`

## Files Inventory
Comma-separated values (CSV) with the following columns:

| Column | Description |
|--------|-------------|
| Source | Source node ID (corresponds to ID in nodes.csv) |
| Target | Target node ID |
| Type | Edge type (all are "Undirected" in this dataset) |
| Id | Unique relationship identifier |
| Label | Relationship category (e.g., Family Member, Partner & Colleague) |
| Weight | Relationship strength (scale 1-5, higher = stronger connection) |

---

## Data Dictionary

### Edge Types
- **Family Member**: Blood or marital relationships
- **Partner & Colleague**: Professional partnerships and collaborations
- **Enemy**: Antagonistic relationships
- **Special Connection**: Unique, significant relationships
- **Landlady & Tenant**: Residential arrangements
- **Mastermind & Henchman**: Criminal hierarchy relationships

### Weight Scale
- **1**: Very weak connection
- **2**: Weak connection
- **3**: Moderate connection
- **4**: Strong connection
- **5**: Very strong connection

## Notes on Use
This sample dataset is intended solely for instructional use in the Gephi Tutorial.

## Archive Format
The file is provided in a CSV format: edges.csv
