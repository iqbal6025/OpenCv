import cv2
import webcolors

# color converter
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

def Events(events,x,y,flag,param):

    if events==cv2.EVENT_LBUTTONDOWN:
        strXY=str(x)+','+str(y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,strXY,(x,y),font,0.5,(0,255,255),1,cv2.LINE_AA)
        cv2.imshow('image',img)
    elif events==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        # strBGR=str(blue)+','+str(green)+','+str(red)
        requested_colour =(red,green,blue)
        color=tuple([int(i) for i in requested_colour])
        actual_name, color_name = get_colour_name(requested_colour)
        cv2.putText(img,color_name,(x,y),font,0.5,(0,0,0),1)
        cv2.imshow('image',img)
img=cv2.imread('color1.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',Events)
cv2.waitKey(0)
cv2.destroyAllWindows()