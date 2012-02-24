import dl
#python 2.5 only
import ctypes

'''
@author: ahuaxuan
@since: 2008-12-03
'''
class ProcessChange(object):
    
    def __init__(self):
        print '#################### init Process change middleware #############'
        
    def __del__(self):
        print "#################### del Process change middleware ##############"
    
    def process_request(self, request):

        procname = 'django' + str(request.get_full_path())
        
        
        '''
        libc = dl.open('/lib/libc.so.6')
        libc.call('prctl', 15, '%s\0' %procname, 0, 0, 0)
        '''
        
        # BSD 如果使用dl模块，在bsd下得这么用
        # libc.call('setproctitle', '%s\0' %procname) 

        #python 2.5 only，bsd下一样，所以ctypes还是比较好滴
        libc = ctypes.CDLL('/lib/libc.so.6')
        libc.prctl(15, '%s\0' %procname, 0, 0, 0)
