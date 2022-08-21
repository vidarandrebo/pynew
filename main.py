#!/usr/bin/python

import os
import sys

import venv


class Program:
    def main(self, argv: list[str]):
        if len(argv) > 1:
            name = argv[1]
            success = self.create_folder(name)
            if not success:
                return

            success = self.create_file(name, "main.py")
            os.chmod(os.path.join(name, "main.py"), 0o755)
            venv.create(os.path.join(name, "venv"))
            req = open(os.path.join(name, "requirements.txt"), "w")
            req.close()
            #os.chmod(os.path.join(name, "main.py"), 0o755)

    def create_folder(self, folder_name: str) -> bool:
        try:
            os.mkdir(folder_name)
        except OSError as err:
            print(err)
            return False
        return True

    def create_file(self, folder_name: str, file_name: str) -> bool:
        path = os.path.join(folder_name, file_name)
        file = open(path, 'w')
        file.write("#!/usr/bin/python\n"
                   "\n"
                   "import sys\n"
                   "\n"
                   "class Program:\n"
                   "    def main(self, argv: list[str]):\n"
                   "        print(\"Hello Python\")\n"
                   "    \n"
                   "if __name__ == '__main__':\n"
                   "    program = Program()\n"
                   "    program.main(sys.argv)\n"
                   )

        file.close()
        return True


if __name__ == '__main__':
    program = Program()
    program.main(sys.argv)
