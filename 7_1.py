def getRatios(vect1, vect2):
    """vect1とvect2を同じ長さのリストとする
    vect1[i]/vect2[i]を意味する値からなるリストを返す"""
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) # nan = Not a Number
        except:
            raise ValueError('getRatios callws with bad arguments')
    return ratios
