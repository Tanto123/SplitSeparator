
# SplitSeparator

A simple utility to split lines of text by a specified separator.

## Description

SplitSeparator is a lightweight tool designed to process lists of strings by splitting each line into two parts using a user-defined separator. This is useful for parsing hash:password lists, CSV-like data, or any text data where you want to separate key-value pairs or columns.

## Features

- Split each line of input text by a custom separator.
- Outputs two lists: left parts and right parts of the split.
- Handles lines without the separator gracefully.
- Easy to integrate into scripts or workflows.

## Usage

### Example

Given an input list:

```
hash1:password1
hash2:password2
hash3:password3
```

and separator `:`, the tool will output:

- Left list:
  ```
  hash1
  hash2
  hash3
  ```
- Right list:
  ```
  password1
  password2
  password3
  ```

### How to use

1. Clone the repository:

```
git clone https://github.com/Tanto123/SplitSeparator.git
cd SplitSeparator
```

2. Run the script or import the module in your Python project.

3. Use the provided function to split lines by your desired separator.

## Example Python code

```
from split_separator import split_separator

lines = [
    "5f4dcc3b5aa765d61d8327deb882cf99:password",
    "098f6bcd4621d373cade4e832627b4f6:test",
    "d8578edf8458ce06fbc5bb76a58c5ca4:qwerty"
]

separator = ":"

left, right = split_separator(lines, separator)

print("Left parts:", left)
print("Right parts:", right)
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

