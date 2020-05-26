import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random

fig=plt.figure(figsize=(10,6))

city=['City A','City B','City C','City D','City E']
x_pos_summer=list(range(1,6))
x_pos_winter=[ i+0.4 for i in x_pos_summer]

graph_summer=plt.bar(x_pos_summer, temp_summer,color='tomato',label='Summer',width=0.4)
graph_winter=plt.bar(x_pos_winter, temp_winter,color='dodgerblue',label='Winter',width=0.4)

plt.title('City Temperature')
plt.ylabel('Temperature ($^\circ$C)')
plt.ylim(0,45)

# removing axes from the figure
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Text Watermark
fig.text(0.85,0.15, 'Analytics made by XXX',
	fontsize=65, color='gray',
	ha='right', va='bottom', alpha=0.2,rotation=45)

plt.xticks([i+0.2 for i in x_pos_summer],city,fontname='Chilanka',rotation=45,fontsize=14)

for summer_bar,winter_bar,ts,tw in zip(graph_summer,graph_winter,temp_summer,temp_winter):
	plt.text(summer_bar.get_x() + summer_bar.get_width()/2.0,summer_bar.get_height(),'%.2f$^\circ$C'%ts,ha='center',va='bottom')
	plt.text(winter_bar.get_x() + winter_bar.get_width()/2.0,winter_bar.get_height(),'%.2f$^\circ$C'%tw,ha='center',va='bottom')

plt.legend(loc='upper center',ncol=2,frameon=False) 
plt.show()
