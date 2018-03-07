from xml.etree.ElementTree import ElementTree as ET
from xml.etree.ElementTree import Element

def if_match(node, kv_map):  
  for key in kv_map:  
    if node.get(key) != kv_map.get(key):  
      return False  
  return True  

def get_node_by_keyvalue(nodelist, kv_map):  
  result_nodes = []  
  for node in nodelist:  
    if if_match(node, kv_map):  
      result_nodes.append(node)  
  return result_nodes  

def main_switch(tree, setting):
	rn = get_node_by_keyvalue(tree.getroot().iter('config') ,{'name':'main_switch'})

	rn[0][0].text = str(setting)

	tree.write('./ssconfig.xml', encoding="utf-8",xml_declaration=True)


def plot_switch(tree, setting):
	rn = get_node_by_keyvalue(tree.getroot().iter('config') ,{'name':'plot_switch'})

	rn[0][0].text = str(setting)

	tree.write('./ssconfig.xml', encoding="utf-8",xml_declaration=True)


if __name__ == '__main__':
	tree = ET()
	tree.parse('./ssconfig.xml')

	main_switch(tree,0)
	plot_switch(tree,0)