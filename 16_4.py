    def playHand(self):
        #playHandの、より高速な、もう一つの実装
        pointsDict = {4:1/3, 5:2/5, 6:5/11, 8:5/11, 9:2/5, 10:1/3}
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else:
                self.dpWins += 1
        else:
            if random.rondom() <= pointsDict[throw]: #7の前にポイントが出る
                self.passWins += 1
                self.dpLosses += 1
            else:                                    #ポイントの前に７が出る
                self.passLossses += 1
                self.dpWins += 1

            