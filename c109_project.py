import csv
import statistics
import pandas as pd

df=pd.read_csv("Students_Performance.csv")
performance_list=df["reading score"].tolist()

mean=statistics.mean(performance_list)
print("mean of this data : ",mean)

median=statistics.median(performance_list)
print("median of this data : ",median)

mode=statistics.mode(performance_list)
print("mode of this data is : ",mode)

standard_deviation=statistics.stdev(performance_list)
print("standard deviation of this data is : ",standard_deviation)

#first,second,third stdev for height

height_first_stdev_start,height_first_stdev_end=mean-standard_deviation,mean+standard_deviation

height_second_stdev_start,height_second_stdev_end=mean-(2*standard_deviation),mean+(2*standard_deviation)

height_third_stdev_start,height_third_stdev_end=mean-(3*standard_deviation),mean+(3*standard_deviation)

#percentage of data within first second third stdev

performance_list_within_first_stdev=[result for result in performance_list if result>height_first_stdev_start and result<height_first_stdev_end]

performance_list_within_second_stdev=[result for result in performance_list if result>height_second_stdev_start and result<height_second_stdev_end]

performance_list_within_third_stdev=[result for result in performance_list if result>height_third_stdev_start and result<height_third_stdev_end]

#printing data
print("{}% data lies within first stdev ".format(len(performance_list_within_first_stdev)*100.0/len(performance_list)))

print("{}% data lies within second stdev ".format(len(performance_list_within_second_stdev)*100.0/len(performance_list)))

print("{}% data lies within third stdev ".format(len(performance_list_within_third_stdev)*100.0/len(performance_list)))