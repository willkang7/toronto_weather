import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/toronto_2020.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	# Get dates and precipitation from this file.
	dates, prcps = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			prcp = float(row[3])
		except ValueError:
			print(f'Missing data for {current_date}')
		else:
			dates.append(current_date)
			prcps.append(prcp)

# Plot the precipitation values.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.bar(dates, prcps, width=2, color='lightblue')

# Format plot.
plt.gca().set_ylim([0, 60])
fig.patch.set_facecolor('#efc9af')

plt.savefig('images/precipitation.png', bbox_inches='tight')
