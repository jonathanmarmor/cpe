#!/usr/bin/env python

import datetime
import os

from PIL import Image


def spiral(X, Y):
    # Adapted from https://stackoverflow.com/questions/398299/looping-in-a-spiral
    result = []
    x = y = 0
    dx = 0
    dy = -1
    for i in xrange(max(X, Y) ** 2):
        if (-X / 2 < x <= X / 2) and (-Y / 2 < y <= Y / 2):
            result.append((x, y))
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
    return result


def shade(value, multiplier=0.7):
    return int(value * multiplier)


def tint(value, multiplier=0.7):
    return int((255 - value) * multiplier)


def color_all(image, function, multiplier):
    pixels = image.load()
    width, height = image.size
    for x in xrange(width):
        for y in xrange(height):
            r, g, b, a = pixels[x, y]
            pixels[x, y] = (
                    function(r, multiplier),
                    function(g, multiplier),
                    function(b, multiplier),
                    a)


def main():
    timestamp = datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S')

    canvas_width = 3000
    canvas_height = 3000
    canvas = Image.new('RGBA', (canvas_width, canvas_height), (255, 255, 255, 255))

    head = Image.open('cpe-head.png').copy()
    head = head.convert('RGBA')
    head_width, head_height = head.size

    # color_all(head, tint, 0.9)

    centered_x = (canvas_width / 2) - (head_width / 2)
    centered_y = (canvas_height / 2) - (head_height / 2)

    offsets = spiral(30, 30)
    for i, coords in enumerate(reversed(offsets)):
        if i % 2 != 0:
            continue

        print i

        x, y = coords
        x = (x * 150) + centered_x
        y = (y * 150) + centered_y
        canvas.paste(head, (x, y), mask=head)


    output_dir = 'output/cover_images/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filename = '{}cover_image_{}.png'.format(output_dir, timestamp)
    canvas.save(filename, format='PNG')


if __name__ == '__main__':
    main()
