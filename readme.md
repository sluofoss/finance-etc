# related project for reference

<https://amortizer.readthedocs.io/en/latest/amortizer.html>

---
---
---

# Notes to be moved

<https://help.obsidian.md/Editing+and+formatting/Callouts>

related terms:

- notice block
- alert
- quote
<https://www.markdownguide.org/basic-syntax/#blockquotes-1>

# python testing for multiple python environment versions

- tox

# python testing

- pytest

# reconfiging git on laptop after years of inactivity

After changing github username, github changing rsa ip, and some other potential things, I need to create another ssh key for laptop windows ps, for some reason by following the github <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>, it run into `git@github.com: Permission denied (publickey)` .

By checking output of `ssh -vT git@gitlab.com` that behaves correctly it lead me to suspect something else is preventing the config from getting called from git. This windows related answer on SO fixed it. <https://stackoverflow.com/a/61163458/10249728>
