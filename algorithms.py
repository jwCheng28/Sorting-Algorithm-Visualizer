from display import Display

class Algorithms(Display):
    def bubbleSort(self):
        N = self.barAmount
        for i in range(N):
            for j in range(N-i-1):
                self.checkQuit()

                # Swap if nxt index is larger
                if self.barH[j] > self.barH[j+1]:
                    self.barH[j], self.barH[j+1] = self.barH[j+1], self.barH[j]
                    self.barCLR[j], self.barCLR[j+1] = self.barCLR[j+1], self.barCLR[j]

                # Redraw Visual
                self.display_surface.fill((0,0,0))
                self.drawBars(self.barLoc, self.barH, self.barCLR)

                # Draw current index location
                self.recolorIndex(index=j+1)
                self.update(30)

    def selectionSort(self):
        N = self.barAmount
        for i in range(N):
            smallestIndex = i
            for j in range(i+1, N):
                self.checkQuit()

                # Find the Smallest Bar
                if self.barH[j] < self.barH[smallestIndex]:
                    smallestIndex = j

                # Draw Visual
                self.display_surface.fill((0,0,0))
                self.draw(self.barLoc, self.barH, self.barCLR)
                # Draw the largest index currently found
                self.recolorIndex(index=smallestIndex, color=(255, 0, 0))
                # Draw the index of current iteration
                self.recolorIndex(index=j)
                self.update(30)

            # Swap the current and largest bar index
            self.barH[smallestIndex], self.barH[i] = self.barH[i], self.barH[smallestIndex]
            self.barCLR[i] = (255, 0, 0)

            # Redraw the Visual
            self.display_surface.fill((0,0,0))
            self.drawBars(self.barLoc, self.barH, self.barCLR)
            self.update(30)
