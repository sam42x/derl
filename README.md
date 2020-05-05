# derl

*A CLI utility for searching for **de**ad U**RL**s inside a project directory.*

## Test and Install

```sh
python setup.py test
python setup.py develop --user
```

## Concept

### Description

The CLI utility should take a directory as one argument, find all files recursively,
find all URLs inside those files and send an HTTP GET request. All returning codes
should be collected and then filtered by 404 Not found. The final list should be
output in a formatted way.

### Features

- Passing a command line argument with the directory to process
- Iterate over all subdirectories and gather a list of all files
  (Including relative path and skipping any binary files)
- Search for URLs (http and https) inside the file list and store all found URLs
- Send an HTTP GET request to all URLs (In later version this definitely should happen parallel)
- Record the returning HTTP Status Code
- Output a list of files and urls where a 404 was returned (something like file:line-number:url)

### Data structure

```txt
files:
  -- filename
  -- relative path
  -- urls
    -- (0)
      -- url
      -- response
      -- line_number
    -- (1)
      -- url
      -- response
      -- line_number
    ...
    -- (n)
      -- url
      -- response
      -- line_number
```

## Test directory structure

``txt
test-directory/
├── dir-1
│   ├── dir-2
│   │   └── test-4-dir-2.txt
│   └── test-3-dir-1.txt
├── test-1-dir-0.txt
└── test-2-dir-0.txt

2 directories, 4 files
```

## Note

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see [https://pyscaffold.org/](https://pyscaffold.org/).

## References

- [Learn Python in 60 Minutes from Java](https://www.youtube.com/watch?v=xLovcfIugy8)
- [Python Primer for Java Developers](https://lobster1234.github.io/2017/05/25/python-java-primer/)
- [The Python Tutorial](https://docs.python.org/3.7/tutorial/index.html)
