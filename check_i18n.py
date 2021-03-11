#!/usr/bin/env python3

import json

def get_keys(dl, keys_list):
    keys_list += dl.keys()    
    if isinstance(dl, dict):                
        for (k, v) in dl.items():           
           if isinstance(v, dict):                              
               keys_list = get_keys(v, keys_list)                          
    return keys_list
    
        
def main():
        with open('./en_GB.json') as json_file:
            jsonENfile = json.load(json_file)            
            keysEN = []
            keysEN = get_keys(jsonENfile, keysEN)            
            sorted(keysEN, key=str.lower)
            # print(*keysEN, sep='\n')
            # print(keysEN)

        print("-------------------------------------------------------") 

        with open('./es_ES.json') as json_file:
            jsonESfile = json.load(json_file)            
            keysES = []
            keysES = get_keys(jsonESfile, keysES)
            sorted(keysES, key=str.lower)
            # print(*keysES, sep='\n')
            # print(keysES)

        res1 = (keysEN==keysES)
        result = "true"
        if not res1:                
                result = "The languages files there are not equals"
                keysInEN = list(set(keysEN) - set(keysES))                
                if len(keysInEN)>0:
                        result += "\n\nIn the English file you have the following keys that do not exist in the Spanish file:\n\n"                        
                        result += '\n'.join(keysInEN)
                keysInES = list(set(keysES) - set(keysEN))                
                if len(keysInES)>0:                        
                        result += "\n\nIn the Spanish file you have the following keys that do not exist in the English file:\n\n"
                        result += '\n'.join(keysInES)
        
        if (result != "true"):
            raise ValueError('ERROR: The language files do not contain the same keys \n\n'+result)            
		
            
   
if (__name__ == '__main__'):
	main()
