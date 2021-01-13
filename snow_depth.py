import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/toronto_2020.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	# Get dates, snow depths, and average temperatures from this file.
	dates, snwds, temps = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			snwd = float(row[4])
		except ValueError:
			snwd = 0
			print(f'Missing snow depth for {current_date}')
		try:
			temp = float(row[5])
		except ValueError:
			temp = 0
			print(f'Missing high temperature for {current_date}')
		dates.append(current_date)
		snwds.append(snwd)
		temps.append(temp)

# Plot the snow depth values.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(dates, snwds, c=temps, cmap='coolwarm', marker='*')

# Format plot.
plt.gca().set_ylim([0, 160])
fig.patch.set_facecolor('#efc9af')

plt.savefig('images/snow_depth.png', bbox_inches='tight')
