import numpy as np
import math
import colorsys

num_colors = 256
t = 5

s_min = 0
s_max = 1

v_min = 0
v_max = 1

s_phase = 0
v_phase = math.pi / 2


# H: Generate indexes with 256 values that go between 0 and 360 (not included)
H = np.linspace(0, 360, num_colors, endpoint=False)

# S
max_ = s_max
min_ = s_min
phase = s_phase
S = (max_ - min_) * (np.sin((2 * math.pi * H / t) + phase) + 1) / 2.0 + min_


# V
max_ = v_max
min_ = v_min
phase = v_phase
V = (max_ - min_) * (np.sin((2 * math.pi * H / t) + phase) + 1) / 2.0 + min_



# HTML:
html = """<!DOCTYPE html>
<html>
  <head>
    <meta  content="text/html; charset=UTF-8"  http-equiv="content-type">
    <title></title>
  </head>
  <body>
    <table  style="height: 71px;"  border="1px solid">
      <tbody>
        <tr>
          <td  style="width: 60px;">Id</td>
          <td  style="width: 60px;">H</td>
          <td  style="width: 60px;">S</td>
          <td  style="width: 60px;">V</td>
          <td  style="width: 123px;">Color</td>
        </tr>"""



for i in range(num_colors):
    #color = colorsys.hsv_to_rgb(int(H[i]), int(S[i]), int(V[i]))
    color = colorsys.hsv_to_rgb(H[i], S[i], V[i])
    # print(int(color[0]*255), int(color[1]*255), int(color[2]*255))
    html += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td style='background-color: rgb({4},{5},{6})'><br></td>".format(
        i, H[i], S[i], V[i], int(color[0]*255), int(color[1]*255), int(color[2]*255))

html += "</table>"

html += "<div>Range S: {0}-{1}, Phase: {2}</div>".format(s_min, s_max, s_phase)
html += "<div>Range V: {0}-{1}, Phase: {2}</div>".format(v_min, v_max, v_phase)
html += "<div>t = {0}</div>".format(t)
html += "</body></html>"

path = "colors-{0}-{1}-{2}-{3}-{4}-{5}-{6}.html".format(s_min, s_max, s_phase, v_min, v_max, v_phase, t)
with open("/Users/jonieva/Desktop/" + path, 'w+b') as f:
    f.write(html)