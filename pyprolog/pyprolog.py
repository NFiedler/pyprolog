import pexpect


class Prolog:
    def __init__(self, import_path=None):
        self._import_path = import_path
        self._swipl_command = 'swipl'

        self._instance = self._init_swipl_instance()

    def _init_swipl_instance(self):
        if self._import_path:  # TODO: verify, this is a real path and no command
            return pexpect.spawn(self._swipl_command + ' ' + self._import_path)
        return pexpect.spawn(self._swipl_command)

    def _reinit_swipl_instance(self):
        self._instance.close()
        self._instance = self._init_swipl_instance()

    def consult_many(self, args):
        for arg in args:
            self.consult(arg)

    def consult(self, arg):
        self._instance.sendline('consult(' + arg + ').\r')

