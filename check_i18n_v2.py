#!/usr/bin/env python3

import json
import os

def get_keys(dl, keys_list):
    keys_list += dl.keys()    
    if isinstance(dl, dict):                
        for (k, v) in dl.items():           
           if isinstance(v, dict):                              
               keys_list = get_keys(v, keys_list)                          
    return keys_list
    
        
def main():

        i18nBaseLanguageFile = "en_GB.json"        
        i18nDirectory = './src/assets/i18n/'

        with open(i18nDirectory + i18nBaseLanguageFile) as json_file:
            jsonBasefile = json.load(json_file)            
            keysBase = []
            keysBase = get_keys(jsonBasefile, keysBase)            
            sorted(keysBase, key=str.lower)
            # print(*keysBase, sep='\n')
            # print(keysBase)

        result = ""                
        with os.scandir(i18nDirectory) as ficheros:
            for fichero in ficheros:                
                if (fichero.name!=i18nBaseLanguageFile):                    
                    with open(i18nDirectory + fichero.name) as json_file:
                        jsonFile = json.load(json_file)            
                        keys = []
                        keys = get_keys(jsonFile, keys)
                        sorted(keys, key=str.lower)
                        
                    res = (keysBase==keys)                    
                    
                    if not res:
                        result += "\n ----------------------------------------------------------------------------------"
                        result += "\n\t The languages files there are not equals: " + i18nBaseLanguageFile + " != " + fichero.name 
                        result += "\n ----------------------------------------------------------------------------------"

                        keysInBASE = list(set(keysBase) - set(keys))                        
                        if len(keysInBASE)>0:                            
                                result += "\n\nIn the " + i18nBaseLanguageFile + " file you have the following keys that do not exist in the " + fichero.name + "\n\n"
                                result += "\t".join(keysInBASE)
                                
                        keysInOtherLanguege = list(set(keys) - set(keysBase))
                        print(*keysInOtherLanguege, sep='\n')
                        if len(keysInOtherLanguege)>0:
                                result += "\n\nIn the " + fichero.name + " file you have the following keys that do not exist in the " + i18nBaseLanguageFile + "\n\n"
                                result += "\t".join(keysInOtherLanguege)
                    else:
                        print("Language files " + i18nBaseLanguageFile + " and " + fichero.name + " are equals.")

        if (result != ""):
            raise ValueError('ERROR: The language files do not contain the same keys \n\n'+result) 

            
   
if (__name__ == '__main__'):
	main()
