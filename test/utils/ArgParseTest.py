from test.GenericTest import GenericTest
from utils import argparser

class ArgParseTest(GenericTest):

    def test(self):
        self.testLs()
        self.testRm()
        self.testAdd()
        self.testEdit()

    def assertArgs(self, argv, expression_str, msg):
        method_name, param = argparser.parseArgs(argv=argv)
        msg = 'Args: {} - {}'.format(argv, msg)
        assert eval(expression_str), msg
        print(self.getJustifiedSuccessMsg(argv))

    def assertUsage(self, argv):
        try:
            method_name, param = argparser.parseArgs(argv=argv)
            assert False, 'should have seen an Exception here'
        except Exception as e:
            assert str(e).lower().find('usage') > 0, 'Exception should be a \'usage\' message'
   
        print(self.getJustifiedSuccessMsg(argv))

    def getJustifiedSuccessMsg(self, argv):
        msg = 'Args: {}'.format(argv)
        return super().getJustifiedSuccessMsg(msg)

    def testLs(self):
        # ['progname', 'ls', 'despesa']
        argv = ['progname', 'ls', 'despesa']
        self.assertArgs(argv, "method_name == 'ls_desp'", 'expected method_name is wrong.')

        # ['progname', 'ls', 'despesa', 3]
        argv = ['progname', 'ls', 'despesa', 3]
        self.assertUsage(argv)

        # ['progname', 'ls', 'despes']
        argv = ['progname', 'ls', 'despes']
        self.assertUsage(argv)

        # ['progname', 'ls']
        argv = ['progname', 'ls']
        self.assertUsage(argv)

    def testRm(self):
        # ['progname', 'rm', 'despesa', 3]
        argv = ['progname', 'rm', 'despesa', 3]
        self.assertArgs(argv, "method_name == 'rm_desp' and param[0] == 3", 'expected method_name or argument is wrong.')

        # ['progname', 'rm', 'despesa', 'anual', 3]
        argv = ['progname', 'rm', 'despesa', 'anual', 3]
        self.assertArgs(argv, "method_name == 'rm_desp_an' and param[0] == 3", 'expected method_name or argument is wrong.')

        # ['progname', 'rm', 'despesa', 'temp', 3]
        argv = ['progname', 'rm', 'despesa', 'temp', 3]
        self.assertArgs(argv, "method_name == 'rm_desp_tmp' and param[0] == 3", 'expected method_name or argument is wrong.')

        # ['progname', 'rm', 'despesa', 'tmp', 3]
        argv = ['progname', 'rm', 'despesa', 'tmp', 3]
        self.assertUsage(argv)

        # ['progname', 'rm', 'despesa', 'anual']
        argv = ['progname', 'rm', 'despesa', 'anual']
        self.assertUsage(argv)

        # ['progname', 'rm', 'despesa', 'temp']
        argv = ['progname', 'rm', 'despesa', 'temp']
        self.assertUsage(argv)

        # ['progname', 'rm', 'despesa', 'tmp']
        argv = ['progname', 'rm', 'despesa', 'tmp']
        self.assertUsage(argv)

        # ['progname', 'rn', 'despesa', 3]
        argv = ['progname', 'rn', 'despesa', 3]
        self.assertUsage(argv)

        # ['progname', 'rm', 'despesa']
        argv = ['progname', 'rm', 'despesa']
        self.assertUsage(argv)

        # ['progname', 'rm']
        argv = ['progname', 'rm']
        self.assertUsage(argv)

    def testAdd(self):
        # ['progname', 'add', 'despesa']
        argv = ['progname', 'add', 'despesa']
        self.assertArgs(argv, "method_name == 'add_desp'", 'expected method_name is wrong')

        # ['progname', 'add', 'despesa', 'anual']
        argv = ['progname', 'add', 'despesa', 'anual']
        self.assertArgs(argv, "method_name == 'add_desp_an'", 'expected method_name is wrong')

        # ['progname', 'add', 'despesa', 'temp']
        argv = ['progname', 'add', 'despesa', 'temp']
        self.assertArgs(argv, "method_name == 'add_desp_tmp'", 'expected method_name is wrong')

        # ['progname', 'add', 'despesa', 'tmp']
        argv = ['progname', 'add', 'despesa', 'tmp']
        self.assertUsage(argv)

        # ['progname', 'add']
        argv = ['progname', 'add']
        self.assertUsage(argv)

        # ['progname', 'add', 'ddd']
        argv = ['progname', 'add', 'ddd']
        self.assertUsage(argv)

    def testEdit(self):
        # ['progname', 'edit', 'despesa', 3]
        argv = ['progname', 'edit', 'despesa', 3]
        self.assertArgs(argv, "method_name == 'edit_desp' and param[0] == 3", 'expected method_name or param is wrong')

        # ['progname', 'edit', 'despesa', 'anual', 3]
        argv = ['progname', 'edit', 'despesa', 'anual', 3]
        self.assertArgs(argv, "method_name == 'edit_desp_an' and param[0] == 3", 'expected method_name or param is wrong')

        # ['progname', 'edit', 'despesa', 'temp', 3]
        argv = ['progname', 'edit', 'despesa', 'temp', 3]
        self.assertArgs(argv, "method_name == 'edit_desp_tmp' and param[0] == 3", 'expected method_name or param is wrong')

        # ['progname', 'edit', 'despesa', 'tmp', 3]
        argv = ['progname', 'edit', 'despesa', 'tmp', 3]
        self.assertUsage(argv)

        # ['progname', 'edit', 'despesa']
        argv = ['progname', 'edit', 'despesa']
        self.assertUsage(argv)

        # ['progname', 'edit', 'despesa', 'anual']
        argv = ['progname', 'edit', 'despesa', 'anual']
        self.assertUsage(argv)

        # ['progname', 'edit', 'despesa', 'temp']
        argv = ['progname', 'edit', 'despesa', 'temp']
        self.assertUsage(argv)

        # ['progname', 'edit']
        argv = ['progname', 'edit']
        self.assertUsage(argv)

