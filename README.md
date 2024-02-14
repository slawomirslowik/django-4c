# my-django-app
My first python django application

1. Create folder locally with your app name <my-first-django-app>
   Add Python and Django linter to VS Code: 
   VS Code > Extensions > Find & Install (Python by Microsoft, Django by Baptiste Darthenay, Auto Close Tag by Jun Han)

2. Open git bash in this folder
3. git init - initialize repozitory locally
4. Create new public repo on github, adding README and .gitignore template - python
5. Copy repository address (code / https > link   <https://my-repo-link>.git)
6. In git bash link local repo to remote origin: 
   
    git remote add origin  <https://my-repo-link>.git
	git branch -M main
    git branch --set-upstream-to=origin/main main
	
7. Install Django framework: pip install django --upgrade
8. Follow tutorial part 1: 
   https://docs.djangoproject.com/pl/5.0/intro/tutorial01/#top
