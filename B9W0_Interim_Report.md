# B9W0: African Climate Trend Analysis - Interim Report

---

## Section 1: Task 1 — Git & Environment Setup (300-500 words)

### Repository Structure

The climate-challenge-week0 repository was initialized with the following structure:

```
climate-challenge-week0/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI workflow
├── data/                       # Data files (ignored by git)
├── venv/                       # Virtual environment (ignored by git)
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── src/                        # Source code directory
├── notebooks/                  # Jupyter notebooks
├── tests/                      # Test files
└── scripts/                    # Utility scripts
```

### Branching Strategy

The project used a feature branch workflow:
- **Base branch**: `main` (created from initial commit)
- **Feature branch**: `setup-task` → used for initial setup
- **PR workflow**: Branch pushed to remote, then merged via GitHub Pull Request

The branching strategy followed conventional Git flow:
1. Create feature branch from main
2. Make commits with descriptive messages
3. Push branch to remote
4. Create PR on GitHub for review and merge

### CI Workflow

The GitHub Actions workflow (`.github/workflows/ci.yml`) was configured to:
- Trigger on push to main branch
- Run on ubuntu-latest
- Use Python 3.10
- Install dependencies from requirements.txt
- Verify Python version

### Conventional Commits

Three conventional commits were made:

| Commit | Message | Description |
|--------|---------|-------------|
| 1 | `init: add .gitignore` | Added .gitignore with data/, *.csv, .ipynb_checkpoints/, venv/ |
| 2 | `chore: venv setup` | Added requirements.txt with pandas, numpy, matplotlib, seaborn, scipy, jupyter |
| 3 | `ci: add GitHub Actions workflow` | Created .github/workflows/ci.yml and README.md |

### Virtual Environment Setup

The virtual environment was created using Python's built-in venv module:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

The venv directory is ignored by git (via .gitignore) to avoid committing virtual environment files.

---

## Section 2: Task 2 — Data Profiling & Cleaning Approach (500-700 words)

### Data Cleaning Pipeline for 5 Countries

The data cleaning pipeline for the African climate dataset includes the following steps:

#### 1. Handling -999 Sentinel Values

The dataset uses -999 as a sentinel value to indicate missing data. This is a common practice in climate datasets where -999 represents no data or sensor failure. The cleaning approach:

- **Detection**: Scan all columns for -999 values
- **Replacement**: Replace -999 with NumPy's NaN (Not a Number) for proper missing value handling
- **Verification**: Confirm replacement with isnull().sum()

#### 2. Date Parsing Logic

The Ethiopia dataset contains YEAR and DOY (Day of Year) columns:
- **YEAR**: 4-digit year (e.g., 2015)
- **DOY**: Day of year (1-366)

The date parsing logic:
```python
df['DATE'] = pd.to_datetime(
    df['YEAR'].astype(str) + df['DOY'].astype(str).str.zfill(3), 
    format='%Y%j'
)
```
This converts YEAR + DOY into a proper datetime object, enabling time series analysis.

#### 3. Missing Value Strategy

For handling missing values after -999 replacement:
- **Forward-fill**: Use previous valid observation to fill gaps (useful for temperature data)
- **Threshold-based dropping**: Drop columns/rows with >50% missing values
- **Interpolation**: Linear interpolation for time series continuity

#### 4. Outlier Detection Method

Outliers are detected using Z-score analysis:
- Calculate Z-score for each numeric column
- Flag values where |Z| > 3 (beyond 3 standard deviations)
- Review flagged values for potential data quality issues

### Initial Findings for Ethiopia

| Metric | Value |
|--------|-------|
| Total Rows | ~3,650 (10 years of daily data) |
| Columns | 11 (YEAR, DOY, T2M, T2M_MAX, T2M_MIN, T2M_RANGE, PRECTOTCORR, RH2M, WS2M, WS2M_MAX, PS, QV2M) |
| Missing % (after -999 replacement) | ~0% (initial check) |
| Duplicate Count | 0 (no duplicate rows detected) |

**Key Variables:**
- **T2M**: Temperature at 2 meters (°C)
- **T2M_MAX/T2M_MIN**: Daily max/min temperature
- **PRECTOTCORR**: Precipitation (corrected)
- **RH2M**: Relative humidity at 2 meters
- **WS2M**: Wind speed at 2 meters
- **PS**: Surface pressure
- **QV2M**: Specific humidity

### Planned Analysis

1. **Time Series Trends**: Analyze temperature and precipitation changes over the 10-year period
2. **Correlations**: Examine relationships between variables (e.g., temperature vs. precipitation)
3. **Distributions**: Visualize distribution of key climate variables
4. **Seasonal Patterns**: Identify seasonal patterns in temperature and rainfall
5. **Climate Indices**: Calculate climate indices for the region

### Challenges Encountered

- **Date Format**: Converting YEAR + DOY format required string manipulation and specific datetime format
- **Sentinel Values**: Identifying and replacing -999 values across all columns
- **Initial Setup**: Setting up the repository structure and Git workflow from scratch
- **Branch Management**: Managing multiple branches (setup-task, eda-ethiopia) and ensuring clean commit history

---

*Report generated on April 28, 2026*
*Project: B9W0 African Climate Trend Analysis*