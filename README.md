# Medical QA Prompt Evaluation

## Project Overview
This project evaluates the effectiveness and safety of large language models (LLMs) in answering medical questions using various prompt engineering strategies. The goal is to identify prompt styles that maximize factuality, helpfulness, and safety while minimizing hallucinations and misinformation.

## Features
- Multiple prompt templates: zero-shot, few-shot, chain-of-thought, and meta-prompt
- Automated and manual evaluation of model responses
- Hallucination detection using pattern-based methods
- Logging and analysis of failure cases

## Folder Structure
```
├── README.md                  # Project overview, setup, findings
├── domain_analysis.md         # Understanding of domain tasks
├── prompts/                   # Prompt templates
│   ├── zero_shot.txt
│   ├── few_shot.txt
│   ├── cot_prompt.txt
│   └── meta_prompt.txt
├── evaluation/                # Evaluation data and reports
│   ├── input_queries.json
│   ├── output_logs.json
│   └── analysis_report.md
├── src/                       # Source code
│   └── utils.py
├── hallucination_log.md       # Examples of failure cases
```

## Setup Instructions
1. Clone the repository and install Python 3.8+.
2. Install dependencies (if any are added in the future).
3. Place your LLM API keys or model weights as needed (not included in this repo).

## Usage
- Edit or add prompt templates in the `prompts/` directory.
- Add test queries to `evaluation/input_queries.json`.
- Run the evaluation pipeline (to be implemented in `src/main.py`).
- Review results in `evaluation/output_logs.json` and `analysis_report.md`.
- Log failure cases in `hallucination_log.md` for continuous improvement.

## Contributing
Contributions are welcome! Please:
- Propose new prompts or evaluation queries
- Suggest improvements to hallucination detection
- Report or log new failure cases

## License
This project is for research and educational purposes only. Not for clinical use. 