@echo off
echo ========================================
echo Pushing DNA Trait Predictor to GitHub
echo Repository: https://github.com/babasveeramallu/bioinfotech
echo ========================================

cd "c:\Users\sumuk\Documents\Personal\Idea\DNA Biotech"

echo.
echo [1/6] Initializing Git repository...
git init

echo.
echo [2/6] Adding remote repository...
git remote remove origin 2>nul
git remote add origin https://github.com/babasveeramallu/bioinfotech.git

echo.
echo [3/6] Creating .gitignore...
echo models/*.pkl > .gitignore
echo __pycache__/ >> .gitignore
echo *.pyc >> .gitignore
echo .DS_Store >> .gitignore
echo *.log >> .gitignore
echo .vscode/ >> .gitignore
echo .idea/ >> .gitignore

echo.
echo [4/6] Adding all files...
git add .

echo.
echo [5/6] Committing changes...
git commit -m "Complete DNA Trait Predictor - All 4 Sprints (46 Story Points)

- Sprint 1: Data Pipeline (US-01 to US-04) - 12 pts
- Sprint 2: Eye Color ML Model (US-05 to US-09) - 14 pts  
- Sprint 3: Multi-Trait Models (US-10 to US-13) - 15 pts
- Sprint 4: GUI Application (US-14 to US-16) - 6 pts

Features:
- Complete production code following Scrum plan
- Workshop materials for teaching
- Training data generators
- Full documentation
- GUI application with tkinter
- 3 ML models (Eye, Hair, Ancestry)

Tech Stack: Python, pandas, scikit-learn, tkinter, matplotlib"

echo.
echo [6/6] Pushing to GitHub...
git branch -M main
git push -u origin main --force

echo.
echo ========================================
echo Done! Check your repository at:
echo https://github.com/babasveeramallu/bioinfotech
echo ========================================
pause
