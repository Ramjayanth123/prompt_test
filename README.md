# 🩺 Medical QA Prompt Evaluation

Welcome to the **Medical QA Prompt Evaluation** project! 🚀

## 🌟 Project Overview
This project explores how different prompt engineering strategies affect the quality and safety of large language model (LLM) answers to medical questions. Our mission: maximize factuality, helpfulness, and safety, while minimizing hallucinations and misinformation. 🧑‍⚕️💬

## ✨ Features
- 📝 Multiple prompt templates: zero-shot, few-shot, chain-of-thought, and meta-prompt
- 🤖 Automated & manual evaluation of LLM responses
- 🚨 Hallucination detection with pattern-based methods
- 📊 Logging & analysis of failure cases
- 📈 Visualizations and summary reports

## 📁 Folder Structure
```
├── README.md                  # 👋 Project overview, setup, findings
├── domain_analysis.md         # 🧠 Understanding of domain tasks
├── prompts/                   # 💡 Prompt templates
│   ├── zero_shot.txt
│   ├── few_shot.txt
│   ├── cot_prompt.txt
│   └── meta_prompt.txt
├── evaluation/                # 🧪 Evaluation data and reports
│   ├── input_queries.json
│   ├── output_logs.json
│   └── analysis_report.md
├── src/                       # 🛠️ Source code & notebook
│   ├── main.ipynb
│   └── utils.py
├── hallucination_log.md       # 🚩 Examples of failure cases
```

## ⚡ Quickstart
1. **Clone** this repo & install Python 3.8+ 🐍
2. **Install dependencies** (see the first cell in `src/main.ipynb`)
3. **Run** the notebook: `src/main.ipynb` in Jupyter/Colab
4. **Review** results in `evaluation/` and logs in `hallucination_log.md`

## 🛠️ Usage
- Edit or add prompt templates in `prompts/`
- Add test queries to `evaluation/input_queries.json`
- Run the notebook to generate and evaluate responses
- Check `evaluation/output_logs.json` and `analysis_report.md` for results
- Log new failure cases in `hallucination_log.md`

## 🤝 Contributing
We love contributions! 💙
- Suggest new prompts or queries
- Improve hallucination detection
- Share new failure cases

## 📜 License
**For research & educational use only. Not for clinical application.**

---

Made with ❤️ by the Medical QA Prompt Evaluation team 