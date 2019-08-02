modules = [
    {
        "MOD_NAME" : { 'dir':'MOD_DIR',                                                                                 # Base directory name (iRTC component)
               'bpn':'123456',                                                                                  # Base software partnumber
               'proc':'PPC',                                                                                    # Processor type for get_cs_crc_con.exe
               'app':'Mod.h86',                                                                                 # Intel hex file
               'jname':'MOD-M',                                                                                 # Name of module application for json file, None if not application code
               'info':'0x20100',                                                                                # Information address of application, otherwise None
               'pinfo':'0x40000',                                                                               # Parameter information address, otherwise None
               'pnomin': '160933',                                                                              # Parameter part number range(min)
               'pnomax': '160958',                                                                              # Parameter part number range(max)
               'fpn':None,                                                                                      # None, placeholder for full partnumber
               'crc':None,                                                                                      # None, placeholder for application crc
               'cks':None,                                                                                      # None, placeholder for application cks
               'dxy':True,                                                                                      # True if this component has doxygen documentation, otherwise False
               'dxy_path':'',                                                                                   # Doxygen Folder path
               'wmode': False,                                                                                  # False if processor uses byte-mode, True if processor uses word-mode
               'files':[{'file':'mod.h86',        'suf':''},                                                    # List of files to include in the bundle with optional suffix
                        {'file':'Mod_Master.a2l', 'suf':''}
                       ]                                                                                        # NOTE: All files will be renamed to [full partnumber][suf].[ext]
             }
    },
    {
        "MOD2" : {
            "bpn" : "153304"
        }
    },
    {}
]

class DictQuery(dict):
    def get(self, path, default = None):
        keys = path.split("/")
        val = None

        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [ v.get(key, default) if v else None for v in val]
                else:
                    val = val.get(key, default)
            else:
                val = dict.get(self, key, default)

            if not val:
                break;

        return val


for item in modules:
    for key in item:
        for key1 in item[key]:
            #print(key1)
            #print(key,item[key],'\n')
            print (DictQuery(item).get(key+"/"+key1)    )
