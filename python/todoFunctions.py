import vim

def find_header_line(line):
    result = line.endswith(':')
    if result:
        return "pass"
    else:
        return "fail"

def archive_line_exists():
    lines = vim.current.buffer
    completed_tasks = []
    archive_header = "_____ARCHIVE_____"
    archive_line = None
    # Check to see if there is an archive line. If yes, save line number, else
    # create archive line
    for i, line in enumerate(lines):
        if archive_header in line:
            archive_line = i + 1 #vim.current.buffer indexes starting at 1
            break
        # adds completed task lines to completed_tasks list
        if '✔' in line:
            completed_tasks.append(i)
    if archive_line is None:
        lines.append("") #cannot append newline characters
        lines.append("")
        lines.append(archive_header)
        archive_line = len(vim.current.buffer)

    # reverses the order of the completed tasks to ensure as they are removed
    # they do not impact line numbers of later tasks
    completed_tasks.reverse()

    # iterates through completed task numbers to add tasks below archive line,
    # then delete those lines from the active tasks area
    for task in completed_tasks:
        lines.append(lines[task].lstrip(), archive_line)
    # Separate for loops so the tasks are appended in order, then deleted
    # correctly
    for task in completed_tasks:
        del lines[task]
