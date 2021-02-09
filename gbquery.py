import sys
from appparams import AppParams
def main():
    params_manager = AppParams()
    params = params_manager.get_params()
    print('using params:',params)

if __name__ == '__main__':
    main()
