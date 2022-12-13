# Personal Color finder 🎨
---
This is our project for opensource software term project

by
- 202133708 김나현
- 202234926 장승우
- 202133753 지수민

## Project overview 
---
***Extract face color using webcam then find and recommand personal color***

Personal color finder with OpenCV & python

### Requirements(install): (with versions I tested on)
- opencv (4.6.0)
- python (3.9.12)
- numpy (1.23.5)
- xml file !!

### Steps of operation
1. running webcam and recognize the face
2. capture the Web Caps
3. Composite image with filter

## Results
---

### Demo
![image](https://user-images.githubusercontent.com/112880884/207248004-ac17c72e-3ab3-4fca-8e87-de13eed06be8.png)


## The limitations
---
1. At first, we wanted to extract the color of our faces from the captured pictures. However, the project did not go smoothly because it required studying various colors such as HSV as well as gray scale and RGB.
We were sorry for these limitations, so we're going to study more about color extraction and recognition and develop this project.

2. So instead, we had opencv recognize faces in pictures and cut the captured images accordingly and show them in combination with color palettes.

## References
---
- https://antilibrary.org/2673
- https://blog.naver.com/dbssk6904/222714280768
- https://076923.github.io/posts/Python-opencv-20/
- https://076923.github.io/posts/Python-opencv-9/
- https://blog.naver.com/oosuhxxxn/222905610710
