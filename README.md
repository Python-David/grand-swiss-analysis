# Grand Swiss Analysis ♟️  

Data analysis of the **FIDE Grand Swiss 2025 (Open Section)** using the official Lichess PGN broadcast. This project parses every game into structured datasets and explores tournament insights through Python and Jupyter notebooks.  

---

## 🔑 Key Insights Explored
- **Result Distribution** → Draws vs wins with White/Black  
- **Opening Trends** → Most played openings and their performance  
- **Giant-Killer Upsets** → 2600s defeating 2700+ opponents  
- **Accuracy Under Pressure** → Blunders vs time scrambles  
- **Game Lengths** → From 20-move knockouts to Abdusattorov–Erdogmus (189 moves!)  

---

## 📂 Project Structure
```
grand-swiss-analysis/
│── data/
│   ├── raw/         # Original PGN files
│   ├── processed/   # Parsed datasets (games.csv, moves.csv)
│
│── notebooks/
│   ├── 01_parsing.ipynb      # PGN → CSV pipeline
│   ├── 02_exploration.ipynb  # First look at the data
│   ├── 03_insights.ipynb     # Core tournament insights
│
│── src/
│   ├── parse_pgn.py          # PGN parsing logic
│
│── README.md
```

---

## 🛠️ Tech Stack
- Python 3.11+  
- [python-chess](https://python-chess.readthedocs.io/) for PGN parsing  
- Pandas, Matplotlib, Seaborn for data analysis + viz  
- Jupyter Notebooks for exploration  

---

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/grand-swiss-analysis.git
   cd grand-swiss-analysis
   ```

2. Create a virtual environment and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the parsing pipeline:
   ```bash
   python src/parse_pgn.py data/raw/grand_swiss_2025.pgn data/processed/games.csv data/processed/moves.csv
   ```

4. Open Jupyter notebooks to explore insights:
   ```bash
   jupyter notebook notebooks/
   ```

---

## 🎯 Goal
The aim of this project is to move beyond anecdotal impressions and use **data** to understand tournament dynamics, player psychology, and meta-trends in elite chess.  

All analysis is open-source and reproducible — feel free to fork, extend, or adapt for your own chess projects.  

---

✌🏾 *Built by [Yours truly](https://github.com/Python-David), for chess & data lovers.*  
