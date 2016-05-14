import re

"""
    Author
        - Scot Matson

    Contributors:
        - [Your name here]

    Description:
        Functions related to carrying out mapreduce operations.
        This particular implementation is developed to look at instances
        of HTML elements on a collection of web pages. It currently runs
        sequentially (it should be parallel)

    TODO: FanIn implementation, I (Scot) I know where this should go and
          I think how to implement it. If somebody else would like to do this
          I can work with you to make it happen. It should go into it's own
          class file I believe.
"""
def map(filename, filedata):
    """
        Author:
            - Scot Matson

        Contributors:
            - [Your name here]

        Maps instances of an HTML tag (Will need to be modified for FanIn)
    """
    emit = dict()

    # Parse data
    r = re.compile('<\w*>|<\w*\s', re.IGNORECASE)
    tags = r.findall(filedata.read())
    for tag in tags:
        # Clense data
        tag = tag.replace('<', '')
        tag = tag.replace('>', '')
        tag = tag.strip()

        # Store data
        if tag != '':
            if tag in emit:
                emit[tag] += 1
            else:
                emit[tag] = 1
    return emit

def unshuffle(shuffled_data):
    """
        Author:
            - Scot Matson

        Contributors:
            - [Your name here]

        Collates related sets of data as a key/value pair.
    """
    sorted_data = dict()

    for tag_dict in shuffled_data:
        for tag in tag_dict:
            if tag in sorted_data:
                sorted_data[tag].append(tag_dict[tag])
            else:
                sorted_data[tag] = [tag_dict[tag]]
    return sorted_data

def reduce(sorted_data):
    """
        Author:
            - Scot Matson

        Contributors:
            - [Your name here]

        Reduces like data sets into a single condensed entity
    """
    reduced_data = dict()

    for tag in sorted_data:
        tag_sum = 0
        for value in sorted_data[tag]:
            tag_sum += value
        if tag in reduced_data:
            reduced_data[tag] += tag_sum
        else:
            reduced_data[tag] = tag_sum
    return reduced_data
