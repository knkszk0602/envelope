import matplotlib.pyplot as pltfrom mpl_toolkits.axes_grid.axislines import SubplotZeroimport numpy as npimport fractions# 改変箇所をまとめておくt_max = 2  # 傾きの最大、最小値の設定x_max = 7y_max = 6y_min = -5step = fractions.Fraction(1, 3)  # 傾きをいくつ刻みで変化させるか。分数のまま計算させるためにFraction()を利用したdef f(x, t):	return t*x-t**2# 以上が改変箇所t_min = -t_max  # 対称性の利用x_min = -x_maxif 1:    fig = plt.figure(1)    ax = SubplotZero(fig, 111)    fig.add_subplot(ax)    for direction in ["xzero", "yzero"]:        ax.axis[direction].set_axisline_style("-|>")        ax.axis[direction].set_visible(True)    for direction in ["left", "right", "bottom", "top"]:        ax.axis[direction].set_visible(False)    ax.text(0, 1.05, 'y',            transform=BlendedGenericTransform(ax.transData, ax.transAxes),            ha='center')    ax.text(1.05, 0, 'x',            transform=BlendedGenericTransform(ax.transAxes, ax.transData),            va='center')    plt.xticks([])    plt.yticks([])    plt.xlim(x_min, x_max)    plt.ylim(y_min, y_max)    x = np.linspace(x_min, x_max, 100)    """    整数以外もとれて、かつ繰り返しができるように、    以下のtの定義ではrangeではなくarangeにしました。    ガウス記号のイメージで、0から数えて１刻みでtをとるようにしました。    """    for t in arange(t_min, t_max+step, step):        y = f(x, t)        ax.plot(x, y, color='black', linewidth=1)plt.show()