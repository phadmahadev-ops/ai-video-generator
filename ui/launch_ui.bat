@echo off
title AI Video Model Hub UI
where python >nul 2>nul || (echo Python nahi mila & pause & exit /b)
python -m pip install -q gradio 2>nul
python "%~dp0model_hub_ui.py"
pause
