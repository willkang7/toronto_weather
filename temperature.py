import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/toronto_2020.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	# Get dates, and high and low temperatures from this file.
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = float(row[6])
			low = float(row[7])
		except ValueError:
			print(f'Missing data for {current_date}')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.gca().set_ylim([-20, 40])
fig.patch.set_facecolor('#D7E1E5')

plt.savefig('images/temperature.png', bbox_inches='tight')
