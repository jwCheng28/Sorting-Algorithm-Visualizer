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

    def mergeSort(self, arr, lbound, rbound):
        self.checkQuit()
        # if left bound is less than right bound, recursive breakdown the array, sort, then merge
        if lbound < rbound:
            mid = (lbound + rbound)//2
            self.mergeSort(arr, lbound, mid)
            self.mergeSort(arr, mid+1, rbound)
            self.merge(arr, lbound, mid, mid+1, rbound)

    def merge(self, arr, lStart, lEnd, rStart, rEnd):
        self.checkQuit()
        # Merge array in sorted order
        i, j = lStart, rStart
        res = []
        while i <= lEnd and j <= rEnd:
            if arr[i] < arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
        while i <= lEnd:
            res.append(arr[i])
            i += 1
        while j <= rEnd:
            res.append(arr[j])
            j += 1

        for j, i in enumerate(range(lStart, rEnd+1)):
            self.barH[i] = res[j]
            self.display_surface.fill((0,0,0))
            self.drawBars(self.barLoc, self.barH, self.barCLR)
        self.update(100)
