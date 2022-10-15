import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from scipy.stats import randint
import statistics
import scipy.stats as st

data = [2.0, 4.8, 5.2, 3.8, 3.5, 3.2, 3.2, 3.9, 4.9,
        2.8, 3.7, 1.8, 3.4, 2.3, 3.2, 4.5, 0.5, 3.3,
        2.8, 2.5, 1.4, 3.2, 3.5, 2.2, 2.3, 3.5, 3.5,
        4.1, 4.4, 2.3, 1.9, 2.2, 3.8, 3.4, 2.2, 3.1,
        2.1, 2.1, 3.2, 2.5, 2.1, 2.9, 2.8, 3.1, 4.3,
        2.8, 4.0, 2.3, 2.7, 2.4, 2.4, 2.3, 2.4, 2.9,
        2.2, 3.6, 2.1, 3.2, 2.3, 2.9, 2.0, 4.7, 3.5,
        2.8, 3.0, -0.2, 3.6, 3.1, 3.3, 1.4, 2.6, 2.6,
        1.8, 4.3, 1.8, 0.7, 4.6, 3.0, 1.9, 3.7, 3.2,
        2.6, 2.6, 4.2, 2.9, 2.3, 5.4, 3.3, 3.1, 2.8,
        2.7, 2.7, 1.8, 2.8, 4.6, 2.7, 1.4, 3.9, 3.7, 2.5]

# numargs = randint.numargs
# a, b = 0.2, 0.8
# rv = randint(a, b)
# plot = plt.plot(data, rv.ppf(data))
fig = plt.figure('гистограмма относительных частот')
ax = fig.add_subplot(111)
ax.set_title('гистограмма относительных частот')
ax.hist(data, edgecolor='violet', linewidth=1.2, color='pink')

print('среднее ' + str(statistics.fmean(data)),
      'дисперсия' + str(statistics.pvariance(data)),
      'ср квадратичное отклонение' + str(np.std(data)),
      'коэффицент вариации' + str(statistics.variance(data)), sep='\n')

ints = st.norm.interval(confidence=0.99,
                        loc=np.mean(data),
                        scale=st.sem(data))
print('границы', ints)

xmin, xmax = min(data), max(data)
x = np.linspace(xmin, xmax, 10)
kde = st.gaussian_kde(data)
print('эмпирическая функция распределения', kde(x))

fig_2 = plt.figure('эмпирическая функция распределения')
sns.set_style('whitegrid')
sns.kdeplot(np.array(data))
plt.show()
