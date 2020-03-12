import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path) # Account for direct usage.
    if os.path.isdir(path): # If directory
        for filename in os.listdir(path): # Then for each child
            childpath = os.path.join(path, filename) # Compose full path to child
            total += disk_usage(childpath) # Add child's usage to total
    print ('{0:<7}'.format(total), path) # Descriptive output (optional)
    return total # Return the grand total