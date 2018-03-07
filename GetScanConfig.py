import scan_config
from xml.dom.minidom import parse
import xml.dom.minidom

def TorF(ans):
	if ans == 'True' or ans == 'true' or ans == 'Yes' or ans == 'yes' or ans == '1':
		return True
	elif ans == 'False' or ans == 'false' or ans == 'No' or ans == 'no' or ans == '0':
		return False
	elif ans == 'test':
		return 'test was here'





def SetVal(valName,val):
	if valName == 'main_switch':
		scan_config.main_switch = eval(val)

	if valName == 'HOST1':
		scan_config.HOST1 = val

	elif valName == 'HOST2':
		scan_config.HOST2 = val

	elif valName == 'plc_host':
		scan_config.plc_host = val

	elif valName == 'PORT1':
		scan_config.PORT1 = eval(val)

	elif valName == 'PORT2':
		scan_config.PORT2 = eval(val)

	elif valName == 'plc_port':
		scan_config.plc_port = eval(val)

	elif valName == 'buffer_size':
		scan_config.buffer_size = eval(val)

	elif valName == 'plot_switch':
		scan_config.plot_switch = TorF(val)

	elif valName == 'plot_splite':
		scan_config.plot_splite = TorF(val)
	
	elif valName == 'plot_all':
		scan_config.plot_all = TorF(val)

	elif valName == 'plot_trolley':
		scan_config.plot_trolley = TorF(val)

	elif valName == 'plot_spreader':
		scan_config.plot_spreader = TorF(val)

	elif valName == 'plot_yard':
		scan_config.plot_yard = TorF(val)

	elif valName == 'time_delay_switch':
		scan_config.time_delay_switch = TorF(val)
	
	elif valName == 'time_delay_val':
		scan_config.time_delay_val = eval(val)

	elif valName == 'process_time_print':
		scan_config.process_time_print = TorF(val)

	elif valName == 'csv_send':
		scan_config.csv_send = val

	elif valName == 'csv_recv':
		scan_config.csv_recv = val

	elif valName == 'plc_comm_switch':
		scan_config.plc_comm_switch = TorF(val)

	elif valName == 'start_angle':
		scan_config.start_angle = eval(val)

	elif valName == 'end_angle':
		scan_config.end_angle = eval(val)

	elif valName == 'total_number':
		scan_config.total_number = eval(val)

	elif valName == 'scan_config_rotation':
		scan_config.scan_config_rotation = eval(val)

	elif valName == 'lidar_1_x_offset':
		scan_config.lidar_1_x_offset = eval(val)

	elif valName == 'lidar_1_y_offset':
		scan_config.lidar_1_y_offset = eval(val)

	elif valName == 'lidar_1_angle_offset':
		scan_config.lidar_1_angle_offset = eval(val)

	elif valName == 'lidar_2_x_offset':
		scan_config.lidar_2_x_offset = eval(val)

	elif valName == 'lidar_2_y_offset':
		scan_config.lidar_2_y_offset = eval(val)

	elif valName == 'lidar_2_angle_offset':
		scan_config.lidar_2_angle_offset = eval(val)

	elif valName == 'lidar_overall_x_offset':
		scan_config.lidar_overall_x_offset = eval(val)

	elif valName == 'lidar_overall_y_offset':
		scan_config.lidar_overall_y_offset = eval(val)

	elif valName == 'lidar_overall_angle_offset':
		scan_config.lidar_overall_angle_offset = eval(val)

	elif valName == 'trolley_height_high':
		scan_config.trolley_height_high = eval(val)

	elif valName == 'trolley_height_low':
		scan_config.trolley_height_low = eval(val)

	elif valName == 'spreader_range_left':
		scan_config.spreader_range_left = eval(val)

	elif valName == 'spreader_range_right':
		scan_config.spreader_range_right = eval(val)

	elif valName == 'grey_prefix':
		scan_config.grey_prefix = eval(val)

	elif valName == 'trolley_len_preset':
		scan_config.trolley_len_preset = eval(val)

	elif valName == 'trolley_len_varying_range':
		scan_config.trolley_len_varying_range = eval(val)

	elif valName == 'spreader_calibration':
		scan_config.spreader_calibration = TorF(val)

	elif valName == 'spreader_calibration_tube':
		scan_config.spreader_calibration_tube = eval(val)

	elif valName == 'yard_left':
		scan_config.yard_left = eval(val)

	elif valName == 'yard_right':
		scan_config.yard_right = eval(val)

	elif valName == 'yard_spreader_left':
		scan_config.yard_spreader_left = eval(val)

	elif valName == 'yard_spreader_right':
		scan_config.yard_spreader_right = eval(val)
	
	elif valName == 'yard_sort_ratio':
		scan_config.yard_sort_ratio = eval(val)




def xmlreading():
	DOMTree = xml.dom.minidom.parse("ssconfig.xml")
	collection = DOMTree.documentElement
	config = collection.getElementsByTagName("config")

	print('scan setting RENEWed!!!!')
	
	for ele in config:
	   #print("*****ele*****")
	   config_name = ele.getAttribute("name")
	   #print(config_name)
	   value_node = ele.getElementsByTagName("value")[0]
	   config_value = value_node.childNodes[0].data
	   SetVal(config_name,config_value)


if __name__ == '__main__':
	print(scan_config.HOST1)
	print(scan_config.HOST2)
	print(scan_config.PORT1)
	print(scan_config.PORT2)
	print(scan_config.buffer_size)
	print(scan_config.plot_switch)
	print(scan_config.time_delay_switch)
	print(scan_config.time_delay_val)
	print(scan_config.process_time_print)
	print(scan_config.csv_send)
	print(scan_config.csv_recv)
	print(scan_config.plc_comm_switch)
	print(scan_config.start_angle)
	print(scan_config.end_angle)
	print(scan_config.total_number)
	print(scan_config.lidar_overall_x_offset)
	
	
	xmlreading()
	print('  ')

	print(scan_config.HOST1)
	print(scan_config.HOST2)
	print(scan_config.PORT1)
	print(scan_config.PORT2)
	print(scan_config.buffer_size)
	print(scan_config.plot_switch)
	print(scan_config.time_delay_switch)
	print(scan_config.time_delay_val)
	print(scan_config.process_time_print)
	print(scan_config.csv_send)
	print(scan_config.csv_recv)
	print(scan_config.plc_comm_switch)
	print(scan_config.start_angle)
	print(scan_config.end_angle)
	print(scan_config.total_number)
	print(scan_config.lidar_overall_x_offset)