    def computeDifference(self) :
        self.maximumDifference = 0
        for i in range(len(self.__elements) - 1) :
            for j in range(len(self.__elements)) :
                x = abs(self.__elements[i] - self.__elements[j])
                if x > self.maximumDifference :
                    self.maximumDifference = x
