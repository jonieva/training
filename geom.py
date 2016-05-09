# print ("result: ", denominations2(10, [2,4]))

def bounding_boxes(b1, b2):
    if b1['bottom_y'] < b2['bottom_y']:
        bottom_y = b1
        top_y = b2
    else:
        bottom_y = b2
        top_y = b1

    if b1['left_x'] < b2['left_x']:
        left_x = b1
        right_x = b2
    else:
        left_x = b2
        right_x = b1

    # Check for wrong cases
    # No intersection
    if bottom_y['bottom_y'] + bottom_y["height"] < top_y['bottom_y'] or \
        left_x["left_x"] + left_x["width"] < right_x["left_x"]:
        return None

    # One rectangle totally contained inside another
    if top_y['bottom_y'] + top_y["height"] < bottom_y['bottom_y'] + bottom_y['height'] and \
        right_x["left_x"] + right_x["width"] < left_x["left_x"] + left_x["width"]:
        return right_x


    # Calculate coords
    lx = right_x["left_x"]
    width = left_x["left_x"] + left_x["width"] - right_x["left_x"]
    by = top_y["bottom_y"]
    height = bottom_y["bottom_y"] + bottom_y["height"] - top_y["bottom_y"]
    return {
        'left_x': lx,
        'bottom_y': by,
        # width and height
        'width': width,
        'height': height,
    }

b1 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,
    # width and height
    'width': 10,
    'height': 4,
}

b11 = {
    # coordinates of bottom-left corner
    'left_x': 11,
    'bottom_y': 6,
    # width and height
    'width': 3,
    'height': 4,
}

b2 = {
    # coordinates of bottom-left corner
    'left_x': 3,
    'bottom_y': 6,
    # width and height
    'width': 10,
    'height': 8,
}

print (bounding_boxes(b1, b11))

class TempTracker(object):
    max_ = min_ = mode_ = __most_frequent__ = _sum = _mean = None
    mode_dict = dict()
    __lenght__ = 0

    def insert_measure(self, temp):
        temp = int(round(temp, 0))
        if temp > self.max_: self.max_ = temp
        elif temp < self.min_: self.min_ = temp
        self.__lenght__ += 1
        self.sum_ += temp
        self.mean_ = (float)self.sum_ / self.__lenght__
        self.mode_dict[temp] = 1 if not self.mode_dict.has_key(temp) else self.mode_dict[temp] + 1
        if self.mode_dict[temp] > self.__most_frequent__:
            self.mode_ = temp
            self.__most_frequent__ = self.mode_dict[temp]

    def get_mean(self):
        return self.mean_