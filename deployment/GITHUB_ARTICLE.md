# Publishing the Iris Flower Prediction API to GitHub

We built a FastAPI application that receives Iris flower measurements and predicts the flower name: **Iris-setosa**, **Iris-versicolor**, or **Iris-virginica**. We also added a root route, API documentation, dependency configuration, and a README so the project can be run and understood by others.

This is the brief path from a local project to GitHub using SSH.

## 1. Set up SSH access to GitHub

Create an SSH key once on your computer:

```powershell
ssh-keygen -t ed25519 -C "your-email@example.com"
```

Copy the contents of the public-key file ending in `.pub`, then add it in GitHub under **Settings → SSH and GPG keys → New SSH key**. Test the connection:

```powershell
ssh -T git@github.com
```

## 2. Create a GitHub repository

Create an empty repository on GitHub, for example `iris-flower-api`. Do not add a README or `.gitignore` there if this local project already has them.

## 3. Prepare the local project

Open PowerShell in the folder containing this project and initialize Git if it has not been initialized already:

```powershell
cd D:\Data\etl\deployment
git init
git branch -M main
git remote add origin git@github.com:YOUR-USERNAME/iris-flower-api.git
```

Replace `YOUR-USERNAME` with your GitHub username.

## 4. Pull remote changes when needed

If the GitHub repository already contains commits, download them before pushing your work:

```powershell
git pull origin main
```

Resolve any merge conflicts if Git reports them, then continue with the commit.

## 5. Add, commit, and push

Check what will be included, add the files, create a commit, and publish it:

```powershell
git status
git add .
git commit -m "Build Iris flower prediction API"
git push -u origin main
```

After the first push, future updates only need `git add .`, `git commit`, and `git push`.

## Recommended picture

Use a clean cover image of the three Iris varieties side by side—**setosa**, **versicolor**, and **virginica**—with a subtle overlay showing the four input measurements: sepal length, sepal width, petal length, and petal width. It immediately explains what the API predicts and makes a strong GitHub repository banner.
