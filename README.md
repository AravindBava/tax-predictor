# Deal Risk Analyzer

Estimates the returns and risks of buying a rental property in metro Atlanta, starting with Fulton County.

## What it can do so far
- Property tax estimate, using Fulton County's 40% assessment ratio and sourced millage rates
- Mortgage payment and remaining loan balance
- One-year deal numbers: NOI, cash flow, DSCR, cap rate, and cash-on-cash return
- Five-year cash flows including the sale, total profit, and IRR

## How to run the tests
    cd deal-risk-analyzer
    source .venv/bin/activate
    python -m pytest -v

## Data sources
Millage rates are for the 2025 tax year, from the Georgia Department of Revenue:
https://dor.georgia.gov/local-government-services/digest-compliance-section/property-tax-millage-rates

| Area | Total mills |
| --- | --- |
| Unincorporated Fulton County | 26.989 |
| City of Atlanta (Fulton County) | 40.709 |

## Disclaimer
These are estimates, not real tax bills, appraisals, or investment advice.
