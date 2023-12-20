"""
not a real test, just putting a file in tests/
"""
import matplotlib.pyplot as plt
from mandelviews import draw_rect


if __name__ == '__main__':
    rect_coords = [0.1, 0.1, 0.5, 0.5]
    ax0 = plt.subplot(111)
    draw_rect(rect_coords, color='red', ax=ax0, line_width=2)
    ax0.set_title("Rect Tester", fontsize=16)
    plt.show()