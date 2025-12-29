# Co-op Salary Analysis

End-to-end analysis and interactive dashboard of self-reported co-op salary data using Python and modern data tools.

## Overview

This project provides a production-ready data application for analyzing co-op salary data. It includes modular code for data loading, analysis, and an interactive dashboard service to visualize insights.

## Project Structure

```
Co-op-Salary-Analysis/
├── data/
│   ├── raw/                    # Raw data files (CSV, JSON, etc.)
│   └── processed/              # Processed/cleaned data files
├── src/
│   ├── __init__.py
│   ├── data_loader.py          # Data loading utilities
│   ├── analysis.py             # Analysis functions
│   └── utils.py                # Utility functions
├── dashboard/
│   ├── __init__.py
│   └── app.py                  # Dashboard/API entry point
├── tests/
│   ├── __init__.py
│   ├── test_data_loader.py     # Tests for data loader
│   └── test_analysis.py        # Tests for analysis module
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Features

- **Modular Architecture**: Organized code structure with separation of concerns
- **Data Management**: Separate directories for raw and processed data
- **Analysis Tools**: Placeholder functions for statistical analysis and insights
- **Dashboard Service**: Entry point for interactive visualization and API
- **Testing**: Basic test structure using unittest
- **Production-Ready**: Includes configuration, documentation, and best practices

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Bowen-Zeng/Co-op-Salary-Analysis.git
   cd Co-op-Salary-Analysis
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Dashboard

The dashboard application can be started using:

```bash
python dashboard/app.py
```

**Note**: The current implementation includes placeholder functions. You'll need to choose and configure a web framework (Flask, FastAPI, Streamlit, etc.) to make it functional.

### Data Loading

```python
from src.data_loader import load_csv_data, get_data_path

# Get path to a data file
data_path = get_data_path("salary_data.csv", "raw")

# Load data (placeholder - needs implementation)
data = load_csv_data(data_path)
```

### Analysis

```python
from src.analysis import calculate_summary_statistics, analyze_by_category

# Calculate statistics (placeholder - needs implementation)
stats = calculate_summary_statistics(data)

# Analyze by category (placeholder - needs implementation)
results = analyze_by_category(data, "company")
```

## Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=src --cov=dashboard

# Run specific test file
python -m pytest tests/test_data_loader.py
```

Or using unittest:

```bash
python -m unittest discover tests/
```

## Development

### Code Style

This project follows Python best practices:

- PEP 8 style guide
- Type hints for function signatures
- Comprehensive docstrings
- Modular, testable code

### Linting and Formatting

```bash
# Format code with black
black src/ dashboard/ tests/

# Lint with flake8
flake8 src/ dashboard/ tests/

# Type check with mypy
mypy src/ dashboard/
```

## Data

### Raw Data

Place raw data files in the `data/raw/` directory. Supported formats:
- CSV files
- JSON files
- Excel files (with appropriate library)

### Processed Data

Processed/cleaned data should be saved to `data/processed/` directory.

## Dashboard Frameworks

Choose one of the following frameworks for the dashboard (update `requirements.txt` accordingly):

- **Flask**: Lightweight web framework for custom APIs and dashboards
- **FastAPI**: Modern, fast API framework with automatic documentation
- **Streamlit**: Quick interactive dashboards with minimal code
- **Dash**: Python framework for building analytical web applications

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Future Enhancements

- [ ] Implement data cleaning and transformation pipelines
- [ ] Add advanced statistical analysis functions
- [ ] Create interactive visualizations
- [ ] Implement API endpoints
- [ ] Add database integration
- [ ] Create comprehensive documentation
- [ ] Add CI/CD pipeline
- [ ] Deploy to cloud platform

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or feedback, please open an issue on GitHub.

## Acknowledgments

- Thanks to all co-op students who contributed salary data
- Built with Python and modern data tools
