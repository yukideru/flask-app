# 進入 GitHub 👉 GitHub

# 點擊右上角的 +，選擇 New repository（建立新儲存庫）

# 輸入儲存庫名稱（例如 flask-app）

# 選擇 Public 或 Private（如果不想讓別人看到，就選 Private）

# 不要勾選 Initialize this repository with a README

# 按下 Create repository（建立儲存庫）

# 你會看到一個 GitHub 遠端 URL，類似：

# https://github.com/你的GitHub帳號/flask-app.git

# VS設定 git init 初始化
# git remote add origin https://github.com/yukideru/flask-app.git 設定 GitHub 遠端倉庫
# git add .將檔案加入 Git
# git commit -m "此次變更內容" 提交變更
# git push -u origin main 將程式碼推送到 GitHub

# （如果是第一次使用 GitHub）
# GitHub 可能會要求你登入，請依照指示操作。
# 如果出現「fatal: the current branch has no upstream branch」，請執行：

# git branch -M main
# git push -u origin main

# git config --global user.name "yukideru"
# git config --global user.email "yuki70506@gmail.com"
