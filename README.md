\# Password Policy Auditor



A Python-based cybersecurity project that evaluates password compliance against configurable security policies and identifies common weak password patterns.



\## Project Overview



The Password Policy Auditor is a locally operated security tool developed to demonstrate password security principles, Python programming, regular expressions, input validation, and automated software testing.



The application evaluates synthetic test passwords against configurable requirements and generates a compliance report.



\*\*No external services or third-party Python packages are required.\*\*



\## Features



\- Minimum password length validation.

\- Uppercase and lowercase character checks.

\- Numeric character validation.

\- Special character validation.

\- Detection of excessive repeated characters.

\- Detection of common weak password patterns.

\- Detection of basic sequential and keyboard patterns.

\- Configurable password policies.

\- Validation of policy configuration settings.

\- Automated unit testing.

\- Text-based compliance report generation.

\- Password values excluded from generated reports.



\## Technologies



| Technology | Purpose |

|---|---|

| Python 3 | Application development |

| Regular Expressions | Password pattern detection |

| unittest | Automated testing |

| dataclasses | Configurable policy management |

| pathlib | Report file management |



\## Project Structure



```text

Password-Policy-Auditor/

â”‚

â”œâ”€â”€ src/

â”‚   â”œâ”€â”€ password\_auditor.py

â”‚   â”œâ”€â”€ report\_generator.py

â”‚   â””â”€â”€ main.py

â”‚

â”œâ”€â”€ tests/

â”‚   â”œâ”€â”€ test\_password\_auditor.py

â”‚   â””â”€â”€ test\_report\_generator.py

â”‚

â”œâ”€â”€ reports/

â”œâ”€â”€ evidence/

â”œâ”€â”€ .gitignore

â””â”€â”€ README.md

```



\## Installation



Clone the repository:



```bash

git clone https://github.com/t-phiri-cyber/Password-Policy-Auditor.git

```



Navigate into the project directory:



```bash

cd Password-Policy-Auditor

```



Python 3 is required. No additional package installation is necessary.



\## Running the Application



Run the application from the project root:



```bash

py -m src.main

```



Enter a synthetic test password when prompted.



The application displays:

\- Individual policy check results.

\- Detected weak password patterns.

\- Overall compliance status.

\- Location of the generated audit report.



\## Running the Tests



Execute the complete automated test suite:



```bash

py -m unittest discover -s tests -v

```



The current test suite contains \*\*21 tests\*\* covering password validation, weak-pattern detection, custom policies, invalid configuration settings, and report generation.



Latest verified result: 21 tests passed.



\## Security Considerations



\- Use synthetic test passwords only.

\- Password values are not included in generated reports.

\- The application operates locally.

\- Passwords are not transmitted to external services.

\- The tool does not connect to breached-password databases.



\## Limitations



This project is a password policy compliance checker, not a complete password-strength assessment platform.



It does not:

\- Calculate password entropy.

\- Check passwords against known breach databases.

\- Guarantee resistance to every password attack.

\- Replace multi-factor authentication or secure authentication architecture.



Its weak-pattern detection is based on a defined set of common words and character sequences.



\## Learning Outcomes



This project demonstrates practical knowledge of:



\- Authentication security.

\- Password policy enforcement.

\- Python application development.

\- Regular expressions.

\- Input validation and error handling.

\- Unit testing and software quality assurance.

\- Security reporting and documentation.



\## Project Cost



Â£0 â€” Developed using Python and its standard library.



\---



\*\*Project:\*\* Password Policy Auditor  

\*\*Category:\*\* Cybersecurity / Authentication Security  

\*\*Language:\*\* Python 3




