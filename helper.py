def clean_filename(name):
    """Ensures each file name does not contain forbidden characters and is within the character limit"""
    # For some reason the file system (Windows at least) is having trouble saving files that are over 180ish
    # characters.  I'm not sure why this is, as the file name limit should be around 240. But either way, this
    # method has been adapted to work with the results that I am consistently getting.
    forbidden_chars = '"*\\/\'.|?:<>'
    filename = (''.join([x if x not in forbidden_chars else '#' for x in name])).replace(
        '  ', ' ').strip()
    if len(filename) >= 176:
        filename = filename[:170] + '...'
    return filename
