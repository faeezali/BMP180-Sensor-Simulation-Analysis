import csv 
import random 
import matplotlib.pyplot as plt 
import numpy as np 

# Module to Simulate/Collect Raw Data

with open("raw_sensor_data.csv", "w") as csv_file: 
    csv_writer = csv.writer(csv_file, delimiter= ",") 
    csv_writer.writerow([ "Timestamp" , "Temperature_C", "Altitude_cm"])

    base_temp = 22 
    alt = 0 
    


    for second in range (0,301): 

        if random.random() > 0.05:         
            temp = base_temp + random.uniform(-2, 2)
        else: 
            jump = random.choice((-1, 1)) * random.uniform(3,5)
            temp = base_temp + jump 
        if random.random() > 0.03:
            alt = alt + .508
        else: 
            alt = alt + random.uniform(1.5,5)

        csv_writer.writerow([second, round(temp, 2), round(alt, 2)])



# Module to Analyze Data 

with open("raw_sensor_data.csv", "r") as csv_file: 
    reader = csv.DictReader(csv_file)
    start_alt = 0 
    temp_error = 0 
    alt_error = 0 
    time = 300
    accuracy_temp = 0
    accuracy_alt = 0
    temp_error_times = []
    alt_error_times = []
    temp_error_values = []
    alt_error_values = []
    all_time = []
    all_temp = []
    all_alt = []


    
    for row in reader: 
        all_time.append(int(row["Timestamp"]))

        all_temp.append(float(row["Temperature_C"]))

        all_alt.append(float(row["Altitude_cm"]))

        if float(row["Temperature_C"]) > 24.00 or float(row["Temperature_C"]) < 20.00: 
            temp_error += 1 
            temp_current_time = int(row["Timestamp"])
            temp_error_times.append(float(temp_current_time))
            temp_error_values.append(float(row["Temperature_C"]))
        else: 
            accuracy_temp += 1

        current_alt = float(row["Altitude_cm"])
    
        velocity = current_alt - start_alt

        if velocity > 1: 
             alt_error += 1
             alt_current_time = int(row["Timestamp"])
             alt_error_times.append(int(alt_current_time))
             alt_error_values.append(float(row["Altitude_cm"]))
        else: 
            accuracy_alt += 1

        start_alt = current_alt
        
print(f"There are {temp_error} temperature anomalies and happen at these timestamps: {temp_error_times}")
print(f"The accuracy percentage is {accuracy_temp / time * 100 :.2f}%")
print()
print(f"There are {alt_error} velocity anomalies and happen at these timestamps: {alt_error_times}")
print(f"The accuracy percentage is {accuracy_alt / time * 100: .2f}% ")


# Module to Visualize data

figure, (ax1, ax2) = plt.subplots(2, 1)

y_alt = np.array(all_alt)
y_temp = np.array(all_temp)
x = np.array(all_time)


ax1.set_title("Data Performance")

ax1.plot(x,y_temp, color = "black", label="Temperature")
ax1.scatter(temp_error_times, temp_error_values, color = "red", label="Anomalies")

ax2.plot(x,y_alt, color = "blue", label="Altitude" )
ax2.scatter(alt_error_times, alt_error_values, color = "red", label="Anomalies")


ax1.set_xlabel("Time (s)")
ax2.set_xlabel("Time (s)")

ax1.set_ylabel("Temperature (°C)")
ax2.set_ylabel("Altitude (cm)")

ax1.legend(loc="lower left", fontsize="x-small")
ax2.legend(loc="upper left", fontsize="x-small")


plt.tight_layout()
plt.savefig("sensor_diagnostic_report.png", dpi=300, bbox_inches='tight')
plt.show()