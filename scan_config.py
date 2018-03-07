import numpy as np
import GetScanConfig

#GetScanConfig.xmlreading()
global HOST1,HOST2,PORT1,PORT2

main_switch = 1

HOST1 = '10.14.9.62'
PORT1 = 2112

HOST2 = '10.14.9.63'
PORT2 = 2112

plc_host = '10.14.9.4'
plc_port = 3000


buffer_size = 16384

# plot
plot_switch = True
plot_split = False
plot_all = True
plot_trolley = True
plot_spreader = True
plot_yard = True
# time
time_delay_switch = True
time_delay_val = 1
process_time_print = True

# plc communication
csv_send = '' #'c://pyinstall//egg123.csv'
csv_recv = '' #'c://pyinstall//double_egg123.csv'
plc_comm_switch = False


# angle setting
start_angle = -5
end_angle = 185
total_number = 1141

ScanAngle_total = (end_angle - start_angle) * np.pi / 180
angle_step = ScanAngle_total / total_number
theta = np.arange(start_angle * np.pi / 180, end_angle * np.pi / 180, angle_step)


# scan config gether rotation number
scan_config_rotation = 10
# log-in config setting

# new added
lidar_overall_x_offset = []
lidar_overall_y_offset = 0
lidar_overall_angle_offset = 0


lidar_1_x_offset = 0
lidar_1_y_offset = 0
lidar_1_angle_offset = 0

lidar_2_x_offset = -3.5
lidar_2_y_offset = 0
lidar_2_angle_offset = 0



trolley_height_high = 25
trolley_height_low = 19
spreader_range_left = -1
spreader_range_right = 1

grey_prefix = 0

trolley_len_preset = 58
trolley_len_varying_range = 0.25

spreader_calibration = True
spreader_calibration_tube = 999

yard_left = 10
yard_right = 0
yard_spreader_left = 0
yard_spreader_right = 0
yard_sort_ratio = 0

lidar_offset_1 = [lidar_overall_x_offset,
				lidar_overall_y_offset,
				lidar_overall_angle_offset,
				lidar_1_x_offset,
				lidar_1_y_offset,
				lidar_1_angle_offset]

lidar_offset_2 = [lidar_overall_x_offset,
				lidar_overall_y_offset,
				lidar_overall_angle_offset,
				lidar_2_x_offset,
				lidar_2_y_offset,
				lidar_2_angle_offset]