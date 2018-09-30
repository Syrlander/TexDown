# TexDown
Program to simply convert Markdown files with embedded TeX math to pdf's. Intended to convert notes made in Markdown to pdf's, without having to bother about problems with Pandoc and/or having to convert every file individually.

## Dependencies
For the program depends on Pandoc to be installed, since it's used for the actual conversion of the files. You can get Pandoc at: https://pandoc.org/installing.html

## How to use
To run the current program use:
```
python texdown.py <LIST_OF_MARKDOWN_FILES>
```

### Specifying output directory
```
python texdown.py <LIST_OF_MARKDOWN_FILES> -o <OUTPUT_FOLDER>
```

## TO-DO
- [ ] LaTeX preprocessing before conversion (replace \bm with \mathbf, since pandoc complains - and any other latex/markdown based problems)
- [x] Automatically convert files when changed and save pdf's to specified folder
  - [x] Create file/direcotry changes observer
- [x] Refactor argument parser to take in a list of strings instead of FileType, so that validator methods doesn't have to take in arguments of FileType aswell.
- [ ] Take in formats like '*.md' for the file list to just find all markdown files in a directory.
- [ ] Allow for multiple markdown files to be concatenate together into one pdf
  - [ ] Auto-generate and insert table of contents

### Far future
- [ ] Pandoc wrapper
- [ ] Own markdown parser (rewrite old F# parser)

## Additional notes
The code is written in Python using the Google docstring style: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
