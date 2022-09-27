#!/usr/bin/env python3
# File       : P5a.py
# Description: Analogue clock using Python closure.
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# Define your closure here
def clock_hand(r):  # do not change this function name and parameter list

    def theta_2_xy(theta):
        theta = (np.pi/180)*theta
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        return x, y
    return theta_2_xy

# Specify absolute hand lengths
r_border = 1.5
r_h = 1
r_m = 1.25
r_s = 1.5

# Specify clock numbers and locations
clock_x = []
clock_y = []
# locations loop
for i in range(0,12):
    clock_theta = 90-30*i
    x = r_border*np.cos(np.deg2rad(clock_theta))
    clock_x.append(x)
    y = r_border*np.sin(np.deg2rad(clock_theta))
    clock_y.append(y)
# numbers
clock_n = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Plot the basic layout
fig, ax = plt.subplots(1,1, figsize=(10,10))

for j in range(0,600):
    
    # Retrieve the current time in hours, minutes, seconds
    t = dt.datetime.now()
    h = t.hour
    m = t.minute
    s = t.second

    # Calculate hand layout from polar coordinates, returning cartesian coordinates
    hour_hand = clock_hand(r_h)
    minute_hand = clock_hand(r_m)
    second_hand = clock_hand(r_s)

    # Calculate theta in degrees for each hand based on current time
    theta_h = 90 - 30*h - m/2
    theta_m = 90 - 6*m
    theta_s = 90 - 6*s

    # Specify the cartesian coordinates cooresponding to the polar coordinates
    x_hour, y_hour = hour_hand(theta_h)
    x_min, y_min = minute_hand(theta_m)
    x_sec, y_sec = second_hand(theta_s)

    # Plot
    plt.title(f"The time is {h}:{m}:{s}",fontsize=20,fontweight='bold')
    plt.xlim(-2,2)
    plt.ylim(-2,2)
    plt.xticks([])
    plt.yticks([])
    ax.set_aspect('equal')
    ax.axis('off')
    # Plot the hands
    plt.plot([0,x_hour],[0,y_hour], linewidth=8, color='black')
    plt.plot([0,x_min],[0,y_min], linewidth=4, color='black')
    plt.plot([0,x_sec],[0,y_sec], linewidth=2, color='black')
    # Plot the clock numbers
    ax.scatter(clock_x,clock_y,s=1/1000)
    for i, txt in enumerate(clock_n):
        ax.annotate(txt, (clock_x[i], clock_y[i]),fontsize=20,ha='center')
    plt.pause(0.1)
    plt.cla()
plt.show()
