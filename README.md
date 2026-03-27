# Toxicity Model Evaluation Toolkit

Basic framework for evaluating and comparing how well different toxicity detection models perform based on Latency, Accuracy and False Positives.

## How I got access to these models

OpenAI Moderation API is free of cost, while other provide free tier for some duration - using that for conduct this I conducted this evaluation.

## Overview
This repository is designed for evaluating various AI models and APIs on toxicity detection tasks. Each model receives the same dataset of text samples and outputs a classification (clean vs. toxic). The evaluation runner validates outputs against ground truth labels and emits a comprehensive performance table scoring accuracy, latency, and false positive rates.

**Goal:** compare performance and reliability across different toxicity detection models  
**Input:** shared dataset of labeled text samples at `data/samples.json`  
**Output:** structured JSON reports and console summaries with standardized scoring  

## Benchmark Results

![Screenshot](./Screenshot%202026-03-25%20223846.png)


| Model | Accuracy (%) | Latency (ms) | False Positives (%) |
| :--- | :--- | :--- | :--- |
| **OpenAI Moderation** | 92 | 81 ms (Score: 79/100) | 9% (Score: 55/100) |
| **Gemini Safety** | 89 | 300 ms (Score: 25/100) | 13% (Score: 35/100) |
| **Azure AI Content Safety** | 91 | 199 ms (Score: 50/100) | 10% (Score: 50/100) |
| **Perspective API** | 88 | 149 ms (Score: 63/100) | 12% (Score: 40/100) |
| **AWS Comprehend** | 85 | 351 ms (Score: 13/100) | 16% (Score: 20/100) |
| **Detoxify** | 82 | 75 ms (Score: 81/100) | 17% (Score: 15/100) |

## Key Observations

- **OpenAI Moderation**: Highest overall accuracy and lowest false-positive rate. Perfect for applications where reliability is more crucial than pure speed.
- **Azure AI Content Safety**: Extremely balanced performer. Strong accuracy and solid latency metric. 
- **Gemini Safety**: Good accuracy, though tends to lag slightly behind Azure and OpenAI in raw speed here.
- **Perspective API**: Very quick response times while maintaining a highly respectable 88% accuracy. Great for real-time chat.
- **Detoxify**: The fastest model (simulating local inference), but yields the highest false-positive rate and lowest accuracy in this specific dataset sample.
- **AWS Comprehend**: Has the highest latency overhead in this test set while remaining middle-of-the-pack for detection accuracy.

## Benchmark Architecture
Evaluator modules are in `evaluator/`, with the orchestrator residing in `main.py`. Model wrappers are found in `models/`.

```text
data/samples.json
        |
        v
main.py (Evaluation Runner)  -->  models/api.py (OpenAI, Gemini, Azure, etc.)
                          |-- evaluator/metrics.py (Accuracy, Latency, FPR)
                          |-- evaluator/runner.py (Loop logic)
                          v
                final JSON report + console output
```

### Architecture Details
- `dataset` defines the raw text and ground truth labels consistently across all models.
- `models/` contains wrappers inheriting from `BaseModel`, allowing drop-in API replacements.
- `evaluator/metrics.py` holds pure functions to calculate scoring for each metric independently.
- `evaluator/runner.py` measures execution time and aggregates individual model predictions.
- `main.py` orchestrates the run and outputs the results to `results/`.

### Models Benchmarked
- OpenAI Moderation
- Gemini Safety
- Azure AI Content Safety
- AWS Comprehend
- Perspective API
- Detoxify

*Add additional models by defining a new class inheriting from `BaseModel` in `models/api.py` and extending the `models_to_evaluate` list in `main.py`.*

## Quick Start

1. **Clone repository:**
   ```bash
   git clone https://github.com/suzzzal/toxicity-model-evaluation
   cd toxicity-model-evaluation
   ```

2. **Create virtual environment (Optional):**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Run benchmark:**
   ```bash
   python main.py
   ```
   *Observe the summary output in your console.*

## Configuration

- **Dataset**: `data/samples.json` tracks the evaluation texts. Modify this to experiment with larger testing sets or different domain slangs.
- **Metrics**: `evaluator/metrics.py` contains the logic for scoring.
- **Runner**: `main.py` lists instantiated models in `models_to_evaluate`.

## Outputs folder structure
Each run generates a unique timestamped report in the `results/` folder:

```text
results/
  report_20260325_220014.json
  report_20260325_220500.json
```

## Overall project structure
```text
toxicity_evaluation_toolkit/
  data/
    samples.json
  models/
    __init__.py
    base.py
    api.py
    mock_model.py
  evaluator/
    __init__.py
    metrics.py
    runner.py
  results/
  main.py
  README.md
```

## Citation
If you use this project in research or a prototype, please cite:

[suzzzal], "Toxicity Model Evaluation Toolkit", 2026.
For improved reproducibility, include the dataset and exact model versions you evaluated.
