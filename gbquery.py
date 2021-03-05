#!/usr/bin/python3
import sys
from appparams import AppParams
from gbffsearchtools import GbffSearchTools
from gbffdatatools import GbffDataTools

def main():

    params_manager = AppParams()
    params = params_manager.get_params()
    print('using params:',params)

    search_gbff = GbffSearchTools(params)
    filelist = search_gbff.search_files()
    print('total matching files = ',len(filelist))
    print('matching files = ',filelist)

    query_gbff = GbffDataTools(params,filelist)
    query_gbff.exec_query()

if __name__ == '__main__':
    main()
