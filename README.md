gitTree
====

List contents of git in a tree-like format

## Demo

```
$git tree
git-tree/
├── .gitignore
├── LICENSE
├── README.md
├── gitTree/
│   ├── __init__.py
│   └── gitTree.py
├── sampleTree/
│   ├── a
│   ├── dir0/
│   │   ├── a0
│   │   ├── dir00/
│   │   │   ├── dir000/
│   │   │   │   ├── file0000
│   │   │   │   └── file0001
│   │   │   └── file001
│   │   └── dir01/
│   │       └── file01
│   └── dir1/
│       ├── dir10/
│       │   └── file101
│       └── dir11/
│           ├── dir111/
│           │   └── dir1111/
│           │       └── dir1111/
│           │           └── file.txt
│           └── file111
└── setup.py
```


## Requirement
 - git
 - python

## Usage
```
$git-tree
```
or
```
$git tree
```

## Install
```
$pip install git-tree
```

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[kosystem](https://github.com/kosystem)
