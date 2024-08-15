title = 'Mean abs(#Heads - #Tails)' + numTrialsString
makePlot(xAxis, diffsMeans, title, 'Number of Flips', 'Mean abs(#Heads - #Tails)', 'ko', logX = True, logY = True)
title = 'SD abs(#Heads - #Tails)' + numTrialsString
makePlot(xAxis, diffsSDs, title, 'Number of Flips', 'Standard Deviation', 'ko', logX = True, logY = True)
