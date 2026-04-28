# Climate Challenge Week0

A data analysis project for climate challenge competitions.

## Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd climate-challenge-week0
```

### Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Folder Structure

```
climate-challenge-week0/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI workflow
├── data/                   # Data files (ignored by git)
├── venv/                   # Virtual environment (ignored by git)
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- scipy
- jupyter