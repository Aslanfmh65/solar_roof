import cv2

class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):  # c is the contour of the shape
        shape = "unidentified"
        peri = cv2.arcLength(c, True)  # Contour Perimeter
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)  # contour approximation

        if len(approx) == 3:
            shape = "triangle"

        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            if (ar >= 0.95) and (ar <= 1.05):
                shape = "square"

            elif 2 * (w + h) < approx:
                shape = "trapezoid"

            else:
                shape = "rectangle"

        elif (len(approx) >= 5) and (len(approx) <= 10):
            shape = "polygon"

        else:
            shape = "circle"

        return shape
