cd  C:\akademie\EERI418
set HOME=%USERPROFILE%
git config credential.https://github.com.username myusername
git add .
git commit -am "made changes: .bat commit"
git push
echo Press Enter...
read
pause
