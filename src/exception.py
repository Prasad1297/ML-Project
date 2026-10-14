import sys
import logging

def error_message_detail(error, error_detail: sys) :

    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, exec_tb.tb_lineno, str(error)        
    )
    
    return error_message
