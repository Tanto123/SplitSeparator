def split_separator(lines, separator):
    """
    Split each line by the given separator into left and right parts.
    
    Args:
        lines (list of str): Input lines to split.
        separator (str): Separator string to split by.
        
    Returns:
        tuple: (left_list, right_list) where each is a list of strings.
    """
    left_list = []
    right_list = []
    
    for line in lines:
        if separator in line:
            left, right = line.split(separator, 1)
            left_list.append(left.strip())
            right_list.append(right.strip())
        else:
            # If separator not found, treat whole line as left and right empty
            left_list.append(line.strip())
            right_list.append("")
    
    return left_list, right_list


if __name__ == "__main__":
    # Example input lines (like hash:pass)
    input_lines = [
        "5f4dcc3b5aa765d61d8327deb882cf99:password",
        "098f6bcd4621d373cade4e832627b4f6:test",
        "d8578edf8458ce06fbc5bb76a58c5ca4:qwerty"
    ]
    
    sep = ":"
    left, right = split_separator(input_lines, sep)
    
    print("Left list:")
    for item in left:
        print(item)
    print("\nRight list:")
    for item in right:
        print(item)
