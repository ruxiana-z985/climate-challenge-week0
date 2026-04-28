# African Climate Analysis Notebooks

This directory contains comprehensive exploratory data analysis notebooks for five African countries: Ethiopia, Kenya, Sudan, Tanzania, and Nigeria.

## Notebooks Overview

### Individual Country Analysis

Each country notebook follows a standardized analysis framework covering:

#### 📊 **Data Loading & Preprocessing**
- Load raw CSV data with `pd.read_csv()`
- Add Country column for identification
- Create DATE column from YEAR + DOY (Day of Year)
- Extract Month for seasonal analysis
- Handle missing values (-999 → NaN)
- Remove duplicate records
- Forward-fill missing data
- Export cleaned data to `data/<country>_clean.csv`

#### 🔍 **Missing Values Analysis**
- Comprehensive missing value assessment
- Flag columns with >5% missing data
- Statistical summary with `describe()`
- Missing value count and percentage analysis

#### ⚠️ **Outliers Detection**
- Z-score analysis for 7 key variables:
  - T2M (Temperature at 2 meters)
  - T2M_MAX (Maximum temperature)
  - T2M_MIN (Minimum temperature)
  - PRECTOTCORR (Precipitation)
  - RH2M (Relative humidity at 2 meters)
  - WS2M (Wind speed at 2 meters)
  - PS (Surface pressure)
- Outlier flagging with >3 Z-score threshold
- Documentation of outlier treatment decisions

#### 🧹 **Data Cleaning**
- Forward-fill imputation for missing values
- Row removal for >30% missing data
- Export cleaned datasets for reproducibility

#### 📈 **Time Series Analysis**
- **Temperature**: Monthly average line charts with warmest/coolest month annotations
- **Precipitation**: Monthly total bar charts with peak rainfall annotations
- Markdown interpretations of climate patterns

#### 🔗 **Correlation Analysis**
- Heatmap of all climate variables
- Scatter plots: T2M vs RH2M, T2M_RANGE vs WS2M
- Top 3 strongest correlations with interpretations

#### 📊 **Distribution Analysis**
- Precipitation histogram (log scale for skewed data)
- Bubble chart: Temperature vs Precipitation (wind speed as bubble size, humidity as color)
- Statistical interpretation of distributions

### Country-Specific Notebooks

| Notebook | Country | Climate Zone | Key Characteristics |
|----------|---------|--------------|-------------------|
| `ethiopia_eda.ipynb` | Ethiopia | East African Highland | Moderate temperatures, distinct rainy season |
| `kenya_eda.ipynb` | Kenya | Equatorial East Africa | Consistent temperatures, bimodal rainfall |
| `sudan_eda.ipynb` | Sudan | Sahelian/Saharan | High temperatures, distinct wet/dry seasons |
| `tanzania_eda.ipynb` | Tanzania | Equatorial | Stable temperatures, coastal influences |
| `nigeria_eda.ipynb` | Nigeria | West African Tropical | High humidity, distinct seasonal patterns |

### Comparative Analysis

#### `compare_countries.ipynb`

This notebook provides comprehensive cross-country analysis:

##### 📊 **Data Loading**
- Concatenation of all 5 cleaned datasets
- Unified timeframe (2015-2026)
- Country identification maintained

##### 🌡️ **Temperature Comparison**
- Multi-line chart of annual average temperatures (2015-2026)
- Summary statistics table by country
- Trend analysis and interpretation

##### 🌧️ **Precipitation Comparison**
- Side-by-side boxplots showing distribution differences
- Summary statistics including total precipitation
- Seasonal pattern comparisons

##### 🔥 **Extreme Heat Analysis**
- Bar chart: Average days/year with T2M_MAX > 35°C
- Country vulnerability ranking
- Heat stress implications

##### 🏜️ **Dry Days Analysis**
- Bar chart: Average maximum consecutive dry days/year
- Drought vulnerability assessment
- Water security implications

##### 📊 **Statistical Testing**
- Kruskal-Wallis test for temperature differences
- P-value interpretation and significance testing
- Effect size calculation (η²)
- Post-hoc pairwise comparisons

##### 🎯 **Vulnerability Ranking**
- Multi-criteria vulnerability scoring:
  - Temperature averages and extremes
  - Heat frequency and intensity
  - Drought duration and frequency
  - Precipitation variability
- Ranked table with justifications
- Visual vulnerability assessment

##### 🏛️ **COP32 Policy Recommendations**
- 5 framed observations answering key climate questions:
  1. Urgent heat adaptation needs
  2. Drought resilience investment priorities
  3. Temperature increase trend identification
  4. Food security precipitation threats
  5. Climate finance allocation recommendations
- Actionable policy bullet points

## Data Structure

### Input Variables
- **YEAR**: Calendar year (2015-2026)
- **DOY**: Day of year (1-366)
- **T2M**: Temperature at 2 meters (°C)
- **T2M_MAX**: Maximum daily temperature (°C)
- **T2M_MIN**: Minimum daily temperature (°C)
- **PRECTOTCORR**: Corrected precipitation (mm)
- **RH2M**: Relative humidity at 2 meters (%)
- **WS2M**: Wind speed at 2 meters (m/s)
- **PS**: Surface pressure (kPa)

### Derived Variables
- **DATE**: Pandas datetime (YEAR + DOY)
- **Country**: Country identifier
- **Month**: Month number (1-12)
- **T2M_RANGE**: Daily temperature range (T2M_MAX - T2M_MIN)

## Usage Instructions

### Prerequisites
```bash
pip install -r requirements.txt
```

### Running Individual Analysis
```bash
jupyter notebook ethiopia_eda.ipynb
```

### Running Comparative Analysis
```bash
jupyter notebook compare_countries.ipynb
```

### Data Dependencies
- Raw CSV files must be in project root
- Cleaned data will be generated in `data/` directory
- Ensure all country datasets are present before running comparative analysis

## Key Findings Summary

### Temperature Patterns
- **Hottest**: Sudan with extreme summer temperatures
- **Most Stable**: Tanzania with equatorial consistency
- **Highest Variability**: Ethiopia with highland influences

### Precipitation Patterns
- **Wettest**: Tanzania with consistent rainfall
- **Most Variable**: Sudan with distinct wet/dry seasons
- **Bimodal**: Kenya with two rainy seasons

### Vulnerability Assessment
- **Highest Risk**: Sudan (extreme heat + drought)
- **Moderate Risk**: Ethiopia (temperature variability)
- **Lower Risk**: Tanzania (stable equatorial climate)

## Methodology Notes

### Statistical Approach
- Non-parametric tests (Kruskal-Wallis) for non-normal data
- Z-score threshold of ±3 for outlier detection
- Forward-fill imputation preserving temporal structure
- Effect size interpretation using Cohen's conventions

### Quality Assurance
- Missing value threshold of 30% for row exclusion
- Automated data validation checks
- Reproducible random states for sampling
- Comprehensive documentation of assumptions

## Future Enhancements

### Potential Extensions
- Machine learning for climate prediction
- Downscaled regional analysis
- Climate change trend detection
- Economic impact assessment
- Agricultural vulnerability modeling

### Data Sources
- NASA POWER climate data
- Local meteorological stations
- Satellite observations
- Climate reanalysis products

---

**Analysis Period**: 2015-2026  
**Geographic Coverage**: 5 African countries  
**Data Points**: ~40,000 daily observations per country  
**Analysis Framework**: Standardized EDA with comparative assessment
