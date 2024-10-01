import tkinter as tk
from tkinter import colorchooser

updating = False

ONE_THIRD = 1.0/3.0
ONE_SIXTH = 1.0/6.0
TWO_THIRD = 2.0/3.0

def rgb_to_hls(r, g, b):
    maxc = max(r, g, b)
    minc = min(r, g, b)
    sumc = (maxc+minc)
    rangec = (maxc-minc)
    l = sumc/2.0
    if minc == maxc:
        return 0, int(l * 100), 0
    if l <= 0.5:
        s = rangec / sumc
    else:
        s = rangec / (2.0-maxc-minc)
    rc = (maxc-r) / rangec
    gc = (maxc-g) / rangec
    bc = (maxc-b) / rangec
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return int(h * 360), int(l * 100), int(s * 100)

def hls_to_rgb(h, l, s):
    if s == 0.0:
        return l, l, l
    if l <= 0.5:
        m2 = l * (1.0+s)
    else:
        m2 = l+s-(l*s)
    m1 = 2.0*l - m2
    return int(_v(m1, m2, h + ONE_THIRD) * 255), int(_v(m1, m2, h) * 255), int(_v(m1, m2, h - ONE_THIRD) * 255)

def _v(m1, m2, hue):
    hue = hue % 1.0
    if hue < ONE_SIXTH:
        return m1 + (m2-m1)*hue*6.0
    if hue < 0.5:
        return m2
    if hue < TWO_THIRD:
        return m1 + (m2-m1)*(TWO_THIRD-hue)*6.0
    return m1

def rgb_to_cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        return 0, 0, 0, 100
    r_prime, g_prime, b_prime = r / 255, g / 255, b / 255
    k = 1 - max(r_prime, g_prime, b_prime)
    c = (1 - r_prime - k) / (1 - k)
    m = (1 - g_prime - k) / (1 - k)
    y = (1 - b_prime - k) / (1 - k)
    return int(c * 100), int(m * 100), int(y * 100), int(k * 100)

def cmyk_to_rgb(c, m, y, k):
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)
    return int(r), int(g), int(b)

def validate_entry(value, min_val, max_val):
    try:
        if value < min_val:
            return min_val
        elif value > max_val:
            return max_val
        return round(value, 2)
    except ValueError:
        return min_val

def update_all(r, g, b, c, m, y, k, h, l, s):
    r_val.set(r)
    g_val.set(g)
    b_val.set(b)

    r_slider.set(r)
    g_slider.set(g)
    b_slider.set(b)

    c_val.set(c)
    m_val.set(m)
    y_val.set(y)
    k_val.set(k)

    c_slider.set(c)
    m_slider.set(m)
    y_slider.set(y)
    k_slider.set(k)

    h_val.set(h)
    l_val.set(l)
    s_val.set(s)

    h_slider.set(h)
    l_slider.set(l)
    s_slider.set(s)

    color_box.config(bg=f'#{r:02x}{g:02x}{b:02x}')

def update_all_from_rgb(*args):
    global updating
    if updating:
        return
    updating = True
    try:
        r = validate_entry(r_val.get(), 0, 255)
        g = validate_entry(g_val.get(), 0, 255)
        b = validate_entry(b_val.get(), 0, 255)
        c, m, y, k = rgb_to_cmyk(r, g, b)
        h, l, s = rgb_to_hls(r / 255, g / 255, b / 255)
        update_all(r, g, b, c, m, y, k, h, l, s)
    finally:
        updating = False

def update_all_from_cmyk(*args):
    global updating
    if updating:
        return
    updating = True
    try:
        c = validate_entry(c_val.get(), 0, 100)
        m = validate_entry(m_val.get(), 0, 100)
        y = validate_entry(y_val.get(), 0, 100)
        k = validate_entry(k_val.get(), 0, 100)
        r, g, b = cmyk_to_rgb(c / 100, m / 100, y / 100, k / 100)
        h, l, s = rgb_to_hls(r / 255, g / 255, b / 255)
        update_all(r, g, b, c, m, y, k, h, l, s)
    finally:
        updating = False

def update_all_from_hls(*args):
    global updating
    if updating:
        return
    updating = True
    try:
        h = validate_entry(h_val.get(), 0, 360)
        l = validate_entry(l_val.get(), 0, 100)
        s = validate_entry(s_val.get(), 0, 100)
        r, g, b = hls_to_rgb(h / 360, l / 100, s / 100)
        c, m, y, k = rgb_to_cmyk(r, g, b)
        update_all(r, g, b, c, m, y, k, h, l, s)
    finally:
        updating = False

def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")[0]
    if color_code:
        r, g, b = map(int, color_code)
        r_val.set(r)
        g_val.set(g)
        b_val.set(b)
        update_all_from_rgb(r, g, b)

root = tk.Tk()
root.geometry("1600x900")
root.title("Color models")

color_box = tk.Label(root, text='Color', bg='black', width=40, height=10, font=('Arial', 16))
color_box.pack(pady=20)

rgb_frame = tk.Frame(root)
rgb_frame.pack(pady=10)

r_val = tk.IntVar()
g_val = tk.IntVar()
b_val = tk.IntVar()

r_val.trace('w', update_all_from_rgb)
g_val.trace('w', update_all_from_rgb)
b_val.trace('w', update_all_from_rgb)

r_slider = tk.Scale(rgb_frame, from_=0, to=255, resolution=1, orient='horizontal', length=800, variable=r_val)
g_slider = tk.Scale(rgb_frame, from_=0, to=255, resolution=1, orient='horizontal', length=800, variable=g_val)
b_slider = tk.Scale(rgb_frame, from_=0, to=255, resolution=1, orient='horizontal', length=800, variable=b_val)

r_slider.grid(row=0, column=1)
g_slider.grid(row=1, column=1)
b_slider.grid(row=2, column=1)

tk.Entry(rgb_frame, textvariable=r_val, width=10, font=('Arial', 14)).grid(row=0, column=0)
tk.Entry(rgb_frame, textvariable=g_val, width=10, font=('Arial', 14)).grid(row=1, column=0)
tk.Entry(rgb_frame, textvariable=b_val, width=10, font=('Arial', 14)).grid(row=2, column=0)

tk.Label(rgb_frame, text="R:", font=('Arial', 14)).grid(row=0, column=2)
tk.Label(rgb_frame, text="G:", font=('Arial', 14)).grid(row=1, column=2)
tk.Label(rgb_frame, text="B:", font=('Arial', 14)).grid(row=2, column=2)

cmyk_frame = tk.Frame(root)
cmyk_frame.pack(pady=10)

c_val = tk.IntVar()
m_val = tk.IntVar()
y_val = tk.IntVar()
k_val = tk.IntVar()

c_val.trace('w', update_all_from_cmyk)
m_val.trace('w', update_all_from_cmyk)
y_val.trace('w', update_all_from_cmyk)
k_val.trace('w', update_all_from_cmyk)

c_slider = tk.Scale(cmyk_frame, from_=0, to=100, resolution=1, orient='horizontal', length=800, variable=c_val)
m_slider = tk.Scale(cmyk_frame, from_=0, to=100, resolution=1, orient='horizontal', length=800, variable=m_val)
y_slider = tk.Scale(cmyk_frame, from_=0, to=100, resolution=1, orient='horizontal', length=800, variable=y_val)
k_slider = tk.Scale(cmyk_frame, from_=0, to=100, resolution=1, orient='horizontal', length=800, variable=k_val)

c_slider.grid(row=0, column=1)
m_slider.grid(row=1, column=1)
y_slider.grid(row=2, column=1)
k_slider.grid(row=3, column=1)

tk.Entry(cmyk_frame, textvariable=c_val, width=10, font=('Arial', 14)).grid(row=0, column=0)
tk.Entry(cmyk_frame, textvariable=m_val, width=10, font=('Arial', 14)).grid(row=1, column=0)
tk.Entry(cmyk_frame, textvariable=y_val, width=10, font=('Arial', 14)).grid(row=2, column=0)
tk.Entry(cmyk_frame, textvariable=k_val, width=10, font=('Arial', 14)).grid(row=3, column=0)

tk.Label(cmyk_frame, text="C:", font=('Arial', 14)).grid(row=0, column=2)
tk.Label(cmyk_frame, text="M:", font=('Arial', 14)).grid(row=1, column=2)
tk.Label(cmyk_frame, text="Y:", font=('Arial', 14)).grid(row=2, column=2)
tk.Label(cmyk_frame, text="K:", font=('Arial', 14)).grid(row=3, column=2)

hls_frame = tk.Frame(root)
hls_frame.pack(pady=10)

h_val = tk.IntVar()
l_val = tk.IntVar()
s_val = tk.IntVar()

h_val.trace('w', update_all_from_hls)
l_val.trace('w', update_all_from_hls)
s_val.trace('w', update_all_from_hls)

h_slider = tk.Scale(hls_frame, from_=0, to=360, resolution=1, orient='horizontal', length=800, variable=h_val)
l_slider = tk.Scale(hls_frame, from_=0, to=100, resolution=1, orient='horizontal', length=800, variable=l_val)
s_slider = tk.Scale(hls_frame, from_=0, to=100, resolution=1, orient='horizontal', length=800, variable=s_val)

h_slider.grid(row=0, column=1)
l_slider.grid(row=1, column=1)
s_slider.grid(row=2, column=1)

tk.Entry(hls_frame, textvariable=h_val, width=10, font=('Arial', 14)).grid(row=0, column=0)
tk.Entry(hls_frame, textvariable=l_val, width=10, font=('Arial', 14)).grid(row=1, column=0)
tk.Entry(hls_frame, textvariable=s_val, width=10, font=('Arial', 14)).grid(row=2, column=0)

tk.Label(hls_frame, text="H:", font=('Arial', 14)).grid(row=0, column=2)
tk.Label(hls_frame, text="L:", font=('Arial', 14)).grid(row=1, column=2)
tk.Label(hls_frame, text="S:", font=('Arial', 14)).grid(row=2, column=2)

color_button = tk.Button(root, text="Choose color", command=choose_color, font=('Arial', 14))
color_button.pack(pady=20)

update_all_from_rgb(0, 0, 0)

root.mainloop()