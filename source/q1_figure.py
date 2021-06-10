#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Mohd Hafizuddin Bin Kamilin"
__date__ = "31 May 5021"

# use pyplot to draw the geometry on a graph
import matplotlib.pyplot as plt
# randomizing the move and degree
from random import randint, seed
# used to calculate cos, sin and radians
from math import cos, sin, radians

class Point:

    global timing

    def __init__(self, x, y):

        # get the xy-coordinate for the point to be plotted
        self.x = x
        self.y = y
        # size of the point to be drawn
        self.size = 50

    def move(self, xUnit, yUnit):

        # update the xy-coordinate of the point
        self.x += xUnit
        self.y += yUnit

    def rotate(self, xPivot, yPivot, turnDegree):

        rad = radians(turnDegree)
        # calculate the new xy-coordinate of the point
        newX = (self.x - xPivot) * cos(rad) - (self.y - yPivot) * sin(rad) + xPivot
        newY = (self.x - xPivot) * sin(rad) + (self.y - yPivot) * cos(rad) + yPivot
        # update the original value
        self.x = newX
        self.y = newY

    def drawPoint(self):

        # split the subplot contents
        _, ax = plt.subplots()
        # fix the scale of the graph bounding box
        ax.set_aspect(1)
        # plot the point
        ax.scatter(
            self.x,
            self.y,
            s = self.size
        )
        # set the bounding box limit for the graph
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)

        return plt

    def showGraph(self):

        for i in range (5):

            if (i == 0):

                # get the plotted point
                geometry = self.drawPoint()
                # set the title
                print("\nPlotting the point at coordinate [" + str(self.x) + ", " + str(self.y) + "].")
                geometry.title("Point drawn at coordinate [" + str(self.x) + ", " + str(self.y) + "].")


            elif (0 < i <= 2):

                # randomize xy-unit to move the point
                randomX = randint(-10, 10)
                randomY = randint(-10, 10)
                # move the point to the defined xy-unit
                self.move(randomX, randomY)
                # get the plotted point
                geometry = self.drawPoint()
                # set the title
                print("Moving the point to coordinate [" + str(randomX) + ", " + str(randomY) + "].")
                geometry.title("Point moved to coordinate [" + str(randomX) + ", " + str(randomY) + "].")

            else:

                # randomize xy-unit to rotate the point
                xPivot = randint(-10, 10)
                yPivot = randint(-10, 10)
                # randomize turnDegree of turn to rotate the point
                turnDegree = randint(1, 360)
                # move the point to the defined xy-unit
                self.rotate(xPivot, yPivot, turnDegree)
                # get the plotted point
                geometry = self.drawPoint()
                # set the title
                print("Rotating the point for " + str(turnDegree) + "° with coordinate ["  + str(xPivot) + ", " + str(yPivot) + "] as pivot.")
                geometry.title("Point rotated for " + str(turnDegree) + "° with coordinate ["  + str(xPivot) + ", " + str(yPivot) + "] as pivot.")

            # shows the plotted point on a graph
            geometry.draw()
            geometry.pause(timing)
            geometry.close()

class Line:

    global timing

    def __init__(self, x0, y0, x1, y1):

        # get the xy-coordinate for the point0 and point1 to be plotted
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        # size of the line to be drawn
        self.size = 3

    def move(self, xUnit, yUnit):

        # update the xy-coordinate of the line
        self.x0 += xUnit
        self.y0 += yUnit
        self.x1 += xUnit
        self.y1 += yUnit

    def rotate(self, xPivot, yPivot, turnDegree):

        rad = radians(turnDegree)
        # calculate the new xy-coordinate of the line
        # NOTE: line will keep getting shorter if you continue to rerotate the same line due to
        #       the imprecision in floating point calculation.  
        newX0 = (self.x0 - xPivot) * cos(rad) - (self.y0 - yPivot) * sin(rad) + xPivot
        newY0 = (self.x0 - xPivot) * sin(rad) + (self.y0 - yPivot) * cos(rad) + yPivot
        newX1 = (self.x1 - xPivot) * cos(rad) - (self.y1 - yPivot) * sin(rad) + xPivot
        newY1 = (self.x1 - xPivot) * sin(rad) + (self.y1 - yPivot) * cos(rad) + yPivot
        # update the original value
        self.x0 = newX0
        self.y0 = newY0
        self.x1 = newX1
        self.y1 = newY1

    def drawLine(self):

        # split the subplot contents
        _, ax = plt.subplots()
        # fix the scale of the graph bounding box
        ax.set_aspect(1)
        # plot the line
        ax.plot(
            [self.x0, self.x1],
            [self.y0, self.y1],
            linewidth = self.size
        )
        # set the bounding box limit for the graph
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)

        return plt

    def showGraph(self):

        for i in range (5):

            if (i == 0):

                # get the plotted line
                geometry = self.drawLine()
                # set the title
                print("\nPlotting the line at coordinate [" + str(self.x0) + ", " + str(self.y0) + "] and [" + str(self.x1) + ", " + str(self.y1) + "]")
                geometry.title("Line drawn at coordinate [" + str(self.x0) + ", " + str(self.y0) + "] and [" + str(self.x1) + ", " + str(self.y1) + "]")

            elif (0 < i <= 2):

                # randomize xy-unit to move the line
                randomX = randint(-10, 10)
                randomY = randint(-10, 10)
                # move the line to the defined xy-unit
                self.move(randomX, randomY)
                # get the plotted line
                geometry = self.drawLine()
                # set the title
                print("Moving the line to coordinate [" + str(randomX) + ", " + str(randomY) + "].")
                geometry.title("Line moved to coordinate [" + str(randomX) + ", " + str(randomY) + "].")

            else:

                # randomize xy-unit to rotate the line
                xPivot = randint(-10, 10)
                yPivot = randint(-10, 10)
                # randomize turnDegree of turn to rotate the line
                turnDegree = randint(1, 360)
                # rotate the line
                self.rotate(xPivot, yPivot, turnDegree)
                # get the plotted line
                geometry = self.drawLine()
                # set the title
                print("Rotating the line for " + str(turnDegree) + "° with coordinate ["  + str(xPivot) + ", " + str(yPivot) + "] as pivot.")
                geometry.title("Line rotated for " + str(turnDegree) + "° with coordinate ["  + str(xPivot) + ", " + str(yPivot) + "] as pivot.")

            # shows the plotted line on a graph
            geometry.draw()
            geometry.pause(timing)
            geometry.close()

class Circle:

    global timing

    def __init__(self, x, y, r):

        # get the xy-coordinate center of the circle
        self.x = x
        self.y = y
        # size of the circle to be drawn
        self.radius = r

    def move(self, xUnit, yUnit):

        # update the xy-coordinate of the circle
        self.x += xUnit
        self.y += yUnit

    def rotate(self, xPivot, yPivot, turnDegree):

        rad = radians(turnDegree)
        # calculate the new xy-coordinate of the circle
        newX = (self.x - xPivot) * cos(rad) - (self.y - yPivot) * sin(rad) + xPivot
        newY = (self.x - xPivot) * sin(rad) + (self.y - yPivot) * cos(rad) + yPivot
        # update the original value
        self.x = newX
        self.y = newY

    def drawCircle(self):

        # split the subplot contents
        _, ax = plt.subplots()
        # fix the scale of the graph bounding box
        ax.set_aspect(1)
        # plot the circle
        circle = plt.Circle((self.x, self.y), self.radius)
        ax.add_artist(circle)
        # set the bounding box limit for the graph
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)

        return plt

    def showGraph(self):

        for i in range (5):

            if (i == 0):

                # get the plotted circle
                geometry = self.drawCircle()
                # set the title
                
                print("\nPlotting the circle with " + str(self.radius) + " unit of radius drawn at coordinate [" + str(self.x) + ", " + str(self.y) + "].")
                geometry.title("Circle with " + str(self.radius) + " unit of radius drawn at coordinate [" + str(self.x) + ", " + str(self.y) + "].")


            elif (0 < i <= 2):

                # randomize xy-unit to move the circle
                randomX = randint(-10, 10)
                randomY = randint(-10, 10)
                # move the circle to the defined xy-unit
                self.move(randomX, randomY)
                # get the plotted circle
                geometry = self.drawCircle()
                # set the title
                print("Moving the circle to coordinate [" + str(randomX) + ", " + str(randomY) + "].")
                geometry.title("Circle moved to coordinate [" + str(randomX) + ", " + str(randomY) + "].")

            else:

                # randomize xy-unit to rotate the circle
                xPivot = randint(-10, 10)
                yPivot = randint(-10, 10)
                # randomize turnDegree of turn to rotate the circle
                turnDegree = randint(1, 360)
                # rotate the circle
                self.rotate(xPivot, yPivot, turnDegree)
                # get the plotted circle
                geometry = self.drawCircle()
                # set the title
                print("Rotating the circle for " + str(turnDegree) + "° with coordinate ["  + str(xPivot) + ", " + str(yPivot) + "] as pivot.")
                geometry.title("Circle rotated for " + str(turnDegree) + "° with coordinate ["  + str(xPivot) + ", " + str(yPivot) + "] as pivot.")

            # shows the plotted circle on a graph
            geometry.draw()
            geometry.pause(timing)
            geometry.close()

class Aggregation:

    global timing

    def __init__(self):

        # set the number of points, line and circle to be drawn
        self.numberOfPoint = randint(0, 5)
        self.numberOfLine = randint(0, 5)
        self.numberOfCircle = randint(0, 5)
        # store the randomized parameters for moving and rotating
        self.pointsXY = []
        self.linesX0 = []
        self.linesY0 = []
        self.linesX1 = []
        self.linesY1 = []
        self.circlesXY = []
        # define the point's size to be drawn
        self.pointSize = 50
        # define the line's size to be drawn
        self.lineSize = 3

        # initiate the xy-coordinate for point
        for _ in range(self.numberOfPoint):

            self.pointsXY.append(
                [
                    randint(-10, 10),
                    randint(-10, 10)
                ]
            )

        # initiate the xy-coordinate for line
        for _ in range(self.numberOfLine):

            self.linesX0.append(
                randint(-10, 10)
            )
            self.linesX1.append(
                randint(-10, 10)
            )
            self.linesY0.append(
                randint(-10, 10)
            )

            self.linesY1.append(
                randint(-10, 10)
            )

        # initiate the xy-coordinate for circle
        for _ in range(self.numberOfCircle):

            self.circlesXY.append(
                [
                    randint(-10, 10),
                    randint(-10, 10)
                ]
            )

    def move(self, xUnit, yUnit):

        # update the xy-coordinate of the point
        for i in range(self.numberOfPoint):

            self.pointsXY[i][0] += xUnit
            self.pointsXY[i][1] += yUnit

        # update the xy-coordinate of the line
        for j in range(self.numberOfLine):

            # update the xy-coordinate of the line
            self.linesX0[j] += xUnit
            self.linesX1[j] += xUnit
            self.linesY0[j] += yUnit
            self.linesY1[j] += yUnit

        # update the xy-coordinate of the circle
        for k in range(self.numberOfCircle):

            self.circlesXY[k][0] += xUnit
            self.circlesXY[k][1] += yUnit

    def rotate(self, xPivot, yPivot, turnDegree):

        rad = radians(turnDegree)

        # update the xy-coordinate of the point
        for i in range(self.numberOfPoint):

            # calculate the new xy-coordinate of the point
            newPointX = (self.pointsXY[i][0] - xPivot) * cos(rad) - (self.pointsXY[i][1] - yPivot) * sin(rad) + xPivot
            newPointY = (self.pointsXY[i][0] - xPivot) * sin(rad) + (self.pointsXY[i][1] - yPivot) * cos(rad) + yPivot
            # update the original value
            self.pointsXY[i][0] = newPointX
            self.pointsXY[i][1] = newPointY

        # update the xy-coordinate of the line
        for j in range(self.numberOfLine):

            # calculate the new xy-coordinate of the line
            # NOTE: line will keep getting shorter if you continue to rerotate the same line due to
            #       the imprecision in floating point calculation.  
            newX0 = (self.linesX0[j] - xPivot) * cos(rad) - (self.linesY0[j] - yPivot) * sin(rad) + xPivot
            newY0 = (self.linesX0[j] - xPivot) * sin(rad) + (self.linesY0[j] - yPivot) * cos(rad) + yPivot
            newX1 = (self.linesX1[j] - xPivot) * cos(rad) - (self.linesY1[j] - yPivot) * sin(rad) + xPivot
            newY1 = (self.linesX1[j] - xPivot) * sin(rad) + (self.linesY1[j] - yPivot) * cos(rad) + yPivot
            # update the original value
            self.linesX0[j] = newX0
            self.linesY0[j] = newY0
            self.linesX1[j] = newX1
            self.linesY1[j] = newY1

        # update the xy-coordinate of the circle
        for k in range(self.numberOfCircle):

            # calculate the new xy-coordinate of the point
            newCircleX = (self.circlesXY[k][0] - xPivot) * cos(rad) - (self.circlesXY[k][1] - yPivot) * sin(rad) + xPivot
            newCircleY = (self.circlesXY[k][0] - xPivot) * sin(rad) + (self.circlesXY[k][1] - yPivot) * cos(rad) + yPivot
            # update the original value
            self.circlesXY[k][0] = newCircleX
            self.circlesXY[k][1] = newCircleY

    def drawAggregation(self):

        # split the subplot contents
        _, ax = plt.subplots()
        # fix the scale of the graph bounding box
        ax.set_aspect(1)
        # set the bounding box limit for the graph
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)
        # control which figure are being displayed on top for scattter
        orderFromTop = self.numberOfPoint + self.numberOfLine + self.numberOfCircle
        # custom coloring for the circle
        cmap = plt.cm.get_cmap("jet")

        # draw point(s)
        for i in range(self.numberOfPoint):

            # plot the point
            ax.scatter(
                self.pointsXY[i][0],
                self.pointsXY[i][1],
                s = self.pointSize,
                zorder = orderFromTop
            )

            orderFromTop -= 1

        # draw line(s)
        for j in range(self.numberOfLine):

            ax.plot(
                [self.linesX0[j], self.linesX1[j]],
                [self.linesY0[j], self.linesY1[j]],
                linewidth = self.lineSize,
                zorder = orderFromTop
            )

            orderFromTop -= 1

        # draw circle(s)
        for k in range(self.numberOfCircle):

            # plot the circle
            ax.add_patch(
                plt.Circle(
                    (
                        self.circlesXY[k][0],
                        self.circlesXY[k][1]
                    ),
                    10,
                    color = cmap(k / self.numberOfCircle),
                    zorder = orderFromTop
                )
            )

            orderFromTop -= 1

        return plt

    def showGraph(self):

        for i in range(5):

            if (i == 0):

                # get the plotted aggregation
                geometry = self.drawAggregation()
                # set the title
                print("\nPlotting the aggregation that consist of " + str(self.numberOfPoint) + " point(s), " + str(self.numberOfLine) + " line(s) and " + str(self.numberOfCircle) + " circle(s).")
                plt.title("Aggregation: " + str(self.numberOfPoint) + " point(s), " + str(self.numberOfLine) + " line(s) and " + str(self.numberOfCircle) + " circle(s).")

            elif (0 < i <= 2):

                # randomize xy-unit to move the point
                randomX = randint(-10, 10)
                randomY = randint(-10, 10)
                # move the point to the defined xy-unit
                self.move(randomX, randomY)
                # get the plotted point
                geometry = self.drawAggregation()
                # set the title
                print("Moving the aggregation to coordinate [" + str(randomX) + ", " + str(randomY) + "].")
                geometry.title("Aggregation moved to coordinate [" + str(randomX) + ", " + str(randomY) + "].")

            else:

                # randomize xy-unit to rotate the line
                xPivot = randint(-10, 10)
                yPivot = randint(-10, 10)
                # randomize turnDegree of turn to rotate the line
                turnDegree = randint(1, 360)
                # rotate the aggregation
                self.rotate(xPivot, yPivot, turnDegree)
                # get the plotted line
                geometry = self.drawAggregation()
                # set the title
                print("Rotating the aggregation for " + str(turnDegree) + "° with coordinate ["  + str(xPivot) + ", " + str(yPivot) + "] as pivot.")
                geometry.title("Aggregation rotated for " + str(turnDegree) + "° with coordinate ["  + str(xPivot) + ", " + str(yPivot) + "] as pivot.")

            # shows the plotted point on a graph
            geometry.draw()
            geometry.pause(timing)
            geometry.close()

# main
if __name__ == "__main__":

    setSeed = input("\nEnter the randomization seed number to ensure the result is replicable (i.e. 1994): ")
    seed(setSeed)

    # control the speed for the graph to be updated (second)
    timing = 5

    # shows a point
    p = Point(0, 0)
    p.showGraph()

    # shows a line
    l = Line(-10, 0, 10, 0)
    l.showGraph()

    # shows a circle
    c = Circle(0, 0, 15)
    c.showGraph()

    # shows a aggregation
    a = Aggregation()
    a.showGraph()

    print()
