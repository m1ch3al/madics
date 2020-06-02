echo "# madics" >> README.md
git init
git remote add origin https://github.com/m1ch3al/madics.git
git config credential.helper store
git push https://github.com/m1ch3al/madics.git
git config --global credential.helper 'cache --timeout 7200'
