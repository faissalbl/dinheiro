from utils import argparser 

class GenericTest:

    def getJustifiedSuccessMsg(self, msg):
        success_msg = '{} -> {} {}'.format(self.getClassName(), msg, 'Success!'.rjust(70 - len(str(msg)), ' '))
        return success_msg

    def getClassName(self):
        return type(self).__name__  


    def test(self):
    	raise NotImplementedError('not implemented yet')


