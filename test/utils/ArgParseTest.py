from test.GenericTest import GenericTest
from utils import argparser

class ArgParseTest(GenericTest):

    def test(self):
        self.testMonth()
        self.testLs()
        self.testRm()
        self.testAdd()
        self.testEdit()
        self.testPay()

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

    def testMonth(self):
        argv = ['progname', 'month', '06/1983']
        self.assertArgs(argv, "method_name == 'change_month' and param[0] == '06/1983'", "expected method_name or argument is wrong.")

    def testLs(self):
        argv = ['progname', 'ls', 'despesa']
        self.assertArgs(argv, "method_name == 'ls_desp'", 'expected method_name is wrong.')

        argv = ['progname', 'ls', 'despesa', 3]
        self.assertUsage(argv)

        argv = ['progname', 'ls', 'despes']
        self.assertUsage(argv)

        argv = ['progname', 'ls']
        self.assertUsage(argv)

        argv = ['progname', 'ls', 'despesa', 'anual']
        self.assertArgs(argv, "method_name == 'ls_desp_an'", 'expected method_name is wrong.')

#        argv = ['progname', 'ls', 'despesa', 'anual', 3]
#        self.assertUsage(argv)

        argv = ['progname', 'ls', 'despes', 'anual']
        self.assertUsage(argv)

        argv = ['progname', 'ls', 'despesa', 'temp']
        self.assertArgs(argv, "method_name == 'ls_desp_tmp'", 'expected method_name is wrong.')

#        argv = ['progname', 'ls', 'despesa', 'temp', 3]
#        self.assertUsage(argv)

        argv = ['progname', 'ls', 'despes', 'temp']
        self.assertUsage(argv)

        argv = ['progname', 'ls', 'renda']
        self.assertArgs(argv, "method_name == 'ls_renda'", 'expected method_name is wrong.')

 #       argv = ['progname', 'ls', 'renda', 3]
 #       self.assertUsage(argv)

        argv = ['progname', 'ls', 'rend']
        self.assertUsage(argv)

        argv = ['progname', 'ls', 'tipo', 'renda']
        self.assertArgs(argv, "method_name == 'ls_tipo_renda'", 'expected method_name is wrong.')

  #      argv = ['progname', 'ls', 'tipo', 'renda', 3]
  #      self.assertUsage(argv)

        argv = ['progname', 'ls', 'tipo']
        self.assertUsage(argv)

        argv = ['progname', 'ls', 'tipo', 'rend']
        self.assertUsage(argv)

        argv = ['progname', 'ls', 'carne', 'leao']
        self.assertArgs(argv, "method_name == 'ls_carne_leao'", 'expected method_name is wrong.')

#        argv = ['progname', 'ls', 'carne', 'leao', 3]
#        self.assertUsage(argv)

        argv = ['progname', 'ls', 'carne', 3]
        self.assertUsage(argv)

        argv = ['progname', 'ls', 'carn', 'leao']
        self.assertUsage(argv)

        argv = ['progname', 'ls', 'parameter']
        self.assertArgs(argv, "method_name == 'ls_param'", 'expected method_name is wrong.')

#        argv = ['progname', 'ls', 'parameter', 3]
#        self.assertUsage(argv)

        argv = ['progname', 'ls', 'param']
        self.assertUsage(argv)

    def testRm(self):
        argv = ['progname', 'rm', 'despesa', 3]
        self.assertArgs(argv, "method_name == 'rm_desp' and param[0] == 3", 'expected method_name or argument is wrong.')

        argv = ['progname', 'rm', 'despesa', 'anual', 3]
        self.assertArgs(argv, "method_name == 'rm_desp_an' and param[0] == 3", 'expected method_name or argument is wrong.')

        argv = ['progname', 'rm', 'despesa', 'temp', 3]
        self.assertArgs(argv, "method_name == 'rm_desp_tmp' and param[0] == 3", 'expected method_name or argument is wrong.')

        argv = ['progname', 'rm', 'despesa', 'tmp', 3]
        self.assertUsage(argv)

        argv = ['progname', 'rm', 'despesa', 'anual']
        self.assertUsage(argv)

        argv = ['progname', 'rm', 'despesa', 'temp']
        self.assertUsage(argv)

        argv = ['progname', 'rm', 'despesa', 'tmp']
        self.assertUsage(argv)

        argv = ['progname', 'rn', 'despesa', 3]
        self.assertUsage(argv)

        argv = ['progname', 'rm', 'despesa']
        self.assertUsage(argv)

        argv = ['progname', 'rm']
        self.assertUsage(argv)

        argv = ['progname', 'rm', 'renda', 3]
        self.assertArgs(argv, "method_name == 'rm_renda' and param[0] == 3", 'expected method_name or argument is wrong.')

        argv = ['progname', 'rm', 'renda']
        self.assertUsage(argv)

        argv = ['progname', 'rn', 'renda', '3']
        self.assertUsage(argv)

        argv = ['progname', 'rm', 'tipo', 'renda', 3]
        self.assertArgs(argv, "method_name == 'rm_tipo_renda' and param[0] == 3", 'expected method_name or argument is wrong.')

        argv = ['progname', 'rm', 'tipo', 3]
        self.assertUsage(argv)

        argv = ['progname', 'rm', 'tipo']
        self.assertUsage(argv)

        argv = ['progname', 'rm', 'parameter', 3]
        self.assertArgs(argv, "method_name == 'rm_param' and param[0] == 3", 'expected method_name or argument is wrong.')

        argv = ['progname', 'rm', 'param', 3]
        self.assertUsage(argv)

        argv = ['progname', 'rm', 'parameter']
        self.assertUsage(argv)

    def testAdd(self):
        argv = ['progname', 'add', 'despesa']
        self.assertArgs(argv, "method_name == 'add_desp'", 'expected method_name is wrong')

        argv = ['progname', 'add', 'despesa', 'anual']
        self.assertArgs(argv, "method_name == 'add_desp_an'", 'expected method_name is wrong')

        argv = ['progname', 'add', 'despesa', 'temp']
        self.assertArgs(argv, "method_name == 'add_desp_tmp'", 'expected method_name is wrong')

        argv = ['progname', 'add', 'despesa', 'tmp']
        self.assertUsage(argv)

        argv = ['progname', 'add']
        self.assertUsage(argv)

        argv = ['progname', 'add', 'ddd']
        self.assertUsage(argv)

        argv = ['progname', 'add', 'renda']
        self.assertArgs(argv, "method_name == 'add_renda'", 'expected method_name is wrong')

        argv = ['progname', 'add', 'tipo', 'renda']
        self.assertArgs(argv, "method_name == 'add_tipo_renda'", 'expected method_name is wrong')

        argv = ['progname', 'add', 'tipo', 'anything']
        self.assertUsage(argv)

        argv = ['progname', 'add', 'tipo']
        self.assertUsage(argv)
    def testEdit(self):
        argv = ['progname', 'edit', 'despesa', 3]
        self.assertArgs(argv, "method_name == 'edit_desp' and param[0] == 3", 'expected method_name or param is wrong')

        argv = ['progname', 'edit', 'despesa', 'anual', 3]
        self.assertArgs(argv, "method_name == 'edit_desp_an' and param[0] == 3", 'expected method_name or param is wrong')

        argv = ['progname', 'edit', 'despesa', 'temp', 3]
        self.assertArgs(argv, "method_name == 'edit_desp_tmp' and param[0] == 3", 'expected method_name or param is wrong')

        argv = ['progname', 'edit', 'despesa', 'tmp', 3]
        self.assertUsage(argv)

        argv = ['progname', 'edit', 'despesa']
        self.assertUsage(argv)

        argv = ['progname', 'edit', 'despesa', 'anual']
        self.assertUsage(argv)

        argv = ['progname', 'edit', 'despesa', 'temp']
        self.assertUsage(argv)

        argv = ['progname', 'edit']
        self.assertUsage(argv)

        argv = ['progname', 'edit', 'renda', 3]
        self.assertArgs(argv, "method_name == 'edit_renda' and param[0] == 3", 'expected method_name or param is wrong')

        argv = ['progname', 'edit', 'renda']
        self.assertUsage(argv)

        argv = ['progname', 'edit', 'tipo', 'renda', 3]
        self.assertArgs(argv, "method_name == 'edit_tipo_renda' and param[0] == 3", 'expected method_name or param is wrong')

        argv = ['progname', 'edit', 'tipo']
        self.assertUsage(argv)

        argv = ['progname', 'edit', 'tipo', 'renda']
        self.assertUsage(argv)

    def testPay(self):
        argv = ['progname', 'pay', 'despesa', 3]
        self.assertArgs(argv, "method_name == 'pay_desp' and param[0] == 3", 'expected method_name or param is wrong')

        argv = ['progname', 'edit', 'despesa', 'anual', 3]
        self.assertArgs(argv, "method_name == 'edit_desp_an' and param[0] == 3", 'expected method_name or param is wrong')

        argv = ['progname', 'pay', 'despesa', 'temp', 3]
        self.assertArgs(argv, "method_name == 'pay_desp_tmp' and param[0] == 3", 'expected method_name or param is wrong')

        argv = ['progname', 'pay', 'despesa', 'temp', 3, 300.5]
        self.assertArgs(argv, "method_name == 'pay_desp_tmp' and param[0] == 3 and param[1] == 300.5", 'expected method_name or param is wrong')

        argv = ['progname', 'pay', 'despesa', 'tmp', 3]
        self.assertUsage(argv)

        argv = ['progname', 'pay', 'despesa']
        self.assertUsage(argv)

        argv = ['progname', 'pay', 'despesa', 'anual']
        self.assertUsage(argv)

        argv = ['progname', 'pay', 'despesa', 'temp']
        self.assertUsage(argv)

        argv = ['progname', 'pay']
        self.assertUsage(argv)
