# 📝 Git Cheat Sheet

## Repo:
	git init                # инициализация репо
	git status              # состояние
	git add .               # добавить все изменения
	git commit -m "msg"     # создать коммит
	git log --oneline --graph --decorate -n 10  # история (10 последних)
	git reset --soft <id>   # откат (сохранить в индексе)
	git reset --mixed <id>  # откат (оставить в рабочей папке)
	git reset --hard <id>   # полный откат
## Remote:
	git remote -v                   # список remotes
	git remote add origin <url>     # добавить remote
	git push -u origin <branch>     # пушить и запомнить ветку
	git pull origin <branch>        # обновить из ветки
	git fetch                       # скачать изменения (без merge)
## Branch:
	git branch -a             # все ветки
	git branch -d <name>      # удалить (слиты изменения)
	git branch -D <name>      # удалить принудительно
	git switch <branch>       # перейти
	git switch -c <branch>    # создать и перейти
	git checkout <hash>       # перейти к коммиту
	git merge <branch>        # слить ветку в текущую
	git rebase <branch>       # переписать историю поверх
## Stash:
	git restore <file>                 # вернуть файл из последнего коммита
	git restore --staged <file>        # убрать из индекса
	git restore --source=<id> <file>   # вернуть из коммита
## Restore:
	git restore <file>                 # вернуть файл из последнего коммита
	git restore --staged <file>        # убрать из индекса
	git restore --source=<id> <file>   # вернуть из коммита
## Clean:
	git clean -fd     # удалить мусорные файлы/папки
## Tags:
	git tag v1.0             # создать тег
	git tag -a v1.0 -m "msg" # аннотированный тег
	git push origin v1.0     # отправить тег
## Useful:
	git diff           # показать изменения
	git diff --staged  # изменения в индексе
	git show <id>      # детали коммита
	git blame <file>   # кто менял строки файла
	git reflog         # все действия (включая сбросы)
