#!/usr/bin/env python

import subprocess
import os

src_dir = 'yejianye.github.io'
target_dir = 'blog-static'
target_branch = 'coding-pages'

def exec_cmd(cmd):
    return subprocess.check_output(cmd, shell=True)

def main():
    print "Build site..."
    exec_cmd('jekyll build')
    os.chdir('../{}'.format(target_dir))
    exec_cmd("git checkout {}".format(target_branch))
    exec_cmd('rsync --recursive --delete --exclude ".git" --exclude ".gitignore" ../{}/_site/. .'.format(src_dir))
    exec_cmd("git add .")
    print exec_cmd("git diff --cached --stat")
    exec_cmd("git commit -m 'Generate static file'")
    print "Publish to coding.net..."
    exec_cmd("git push origin {}".format(target_branch))

if __name__ == '__main__':
    main()
