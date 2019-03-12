def get_file_content_as_list(filename):
    """Return content of the file as a list of lines

    The file is expected to be in the current working directory.
    The lines in the list contains trailing line breaks.

    Example:
    If the a.txt has two lines 'aaa' and 'bbb',
    get_file_content_as_list('a.txt') returns ['aaa\n', 'bbb']
    """
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


stats = []


def get_file_stats(contents):
    """Given a list of lines, return line count and letter count as a dictionary

    Trailing line breaks (if any) are not counted for letter count.
    Spaces, even trailing spaces, are counted for letter count.
    Example:
    get_stats(['aaa\n', 'bbb']) returns {'lines': 2, 'letters': 6}
    """

    stats = contents
    # stats = stats.strip()
    for i, stat in enumerate(stats):
        stats[i] = stat.strip()
        stats = stats[i]

    return len(stats)


def analyze_file(filename):
    contents_as_list = get_file_content_as_list(filename)
    print('lines in file:', contents_as_list)
    stats = get_file_stats(contents_as_list)
    # print('It has', stats[0], 'lines containing', stats[1], 'letters')


analyze_file('file1.txt')
# analyze_file('file2.txt')
