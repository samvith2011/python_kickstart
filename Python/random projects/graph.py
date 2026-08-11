import matplotlib.pyplot as plt

plt.axis([2020,2025,0,10])

plt.xticks([2020,2021,2022,2023,2024,2025],[2020,2021,2022,2023,2024,2025])

plt.yticks([0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10])

datax = [2020,2021,2022,2023,2024,2025]

datay = [4.9,7.6,6.2,6.1,7.2,8.3]

plt.plot(datax, datay, color='blue', marker='o')
plt.show()
