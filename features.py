from typing import List


def points_to_sections(contours, step=1, print_endpoints=False):
    sections = []
    if print_endpoints:
        maxx = 0
        minx = 1000000000000
        maxy = 0
        miny = 1000000000000

    for current_contour in contours:
        for point_index in range(0, len(current_contour) - 1, step):
            if point_index + step < len(current_contour):
                # x&y of startpoint in section
                x1 = current_contour[point_index][0][0]
                y1 = current_contour[point_index][0][1]
                # x&y of endpoint in section
                x2 = current_contour[point_index + step][0][0]
                y2 = current_contour[point_index + step][0][1]
                # search the biggest & the lowest points
                if print_endpoints:
                    maxx = max(maxx, x1, x2)
                    minx = min(minx, x1, x2)
                    maxy = max(maxy, y1, y2)
                    miny = min(miny, y1, y2)
                # add section into sections
                section = [x1, y1, x2, y2]
                sections.append(section)
            else: break
    # returning
    if print_endpoints:
        print(len(sections), ";", maxx, minx, maxy, miny)
        return sections, maxx, minx, maxy, miny
    else:
        print(len(sections))
        return sections


def transform_points(sections, maxx, minx, maxy, miny) -> List:
    # preparing  lines
    x = 400
    y = 400
    # preparing points
    maxx = (maxx - minx) / 2
    maxy = (maxy - miny) / 2

    for section in sections:
        section[0] = (section[0] - minx - maxx) / maxx * x
        section[1] = (section[1] - miny - maxy) / maxy * y
        section[2] = (section[2] - minx - maxx) / maxx * x
        section[3] = (section[3] - miny - maxy) / maxy * y

    return sections


def points_to_sections_reduced(contours, number_of_sections) -> List:
    sections = points_to_sections(contours)
    step = len(sections) // number_of_sections + 1
    sections, maxx, minx, maxy, miny = points_to_sections(contours, step, True)
    sections = transform_points(sections, maxx, minx, maxy, miny)
    return sections
