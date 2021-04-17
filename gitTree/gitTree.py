#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

C_GREEN = '\033[92m'
C_BLUE = '\033[94m'
C_END = '\033[00m'


def grouping(fileList):
    root = {}
    for path in fileList:
        current = root
        for p in path.rstrip('\n').split('/'):
            current.setdefault(p, {})
            current = current[p]
    return root


def displayItems(items, path, prefix, color):
    for index, item in enumerate(sorted(items.keys())):
        if index == len(items)-1:
            print(prefix + '└── ' + appendColor(path, item, color))
            nextPrefix = prefix + '    '
        else:
            print(prefix + '├── ' + appendColor(path, item, color))
            nextPrefix = prefix + '│   '
        if len(items[item]) > 0:
            nextpath = os.path.join(path, item)
            displayItems(items[item], nextpath, nextPrefix, color)


def appendColor(path, item, color=False):
    filepath = os.path.join(path, item)
    colorCode = ''
    endCode = C_END if color else ''
    indicator = ''
    if color:
        if os.path.isdir(filepath):
            colorCode = C_BLUE
        elif os.access(filepath, os.X_OK):
            colorCode = C_GREEN
        else:
            colorCode = C_END

    if os.path.isdir(filepath):
        indicator = '/'

    return colorCode + item + endCode + indicator


def main():
    cmd = 'git ls-files'
    p = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    p.wait()
    stdout_data = [l.decode('utf-8') for l in p.stdout.readlines()]
    stderr_data = p.stderr.read()
    if len(stderr_data) > 0:
        print(stderr_data, end=' ')
    else:
        color = True
        currentDir = os.path.split(os.getcwd())
        print(appendColor(currentDir[0], currentDir[1], color))
        group = grouping(stdout_data)

        displayItems(group, '.', '', color)


if __name__ == '__main__':
    main()
