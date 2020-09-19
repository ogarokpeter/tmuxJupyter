# tmuxJupyter

## Description

Program that runs a pre-defined number of isolated Jupyter notebooks. Each notebook has its own working directory, port and token, and the program is capable of  shutting down unneeded notebooks.

Program was implemented as a task in my university. The description of the task (in Russian) is below.

## How to run

Just run 

```
$ python3 main.py
```

with nessessary CLI arguments. The list of all arguments and a quick help can be reached by running

```
$ python3 main.py --help
```

## Description of the task (Russian)

Написать программу, которая запускает в tmux *N* изолированных окружений Jupyter.
* **\[1.5\]** У каждого окружения должна быть своя рабочая директория, свой порт и токен.
* **\[1\]** Каждое окружение должно жить в своём tmux-окне (window).
* **\[2\]** Программа должна уметь стартовать и убивать окружения.
* **\[0.5\]** При старте окружений должен выводиться progress bar (т.к. старт большого кол-ва сессий с Jupyter может занять время). Для этого можно использовать библиотеку tqdm.

Команда, с помощью которой можно стартовать Jupyter'ы:
```
jupyter notebook --ip {} --port {} --no-browser --NotebookApp.token='{}' --NotebookApp.notebook_dir='{}'
```

Интерфейс для реализации.

```python
import libtmux
import socket
import os
import tqdm


def start(num_users, base_dir='./'):
    """
    Запустить $num_users ноутбуков. У каждого рабочай директория $base_dir+$folder_num
    """
    pass
    

def stop(session_name, num):
    """
    @:param session_name: Названия tmux-сессии, в которой запущены окружения
    @:param num: номер окружения, кот. можно убить
    """
    pass


def stop_all(session_name):
    """
    @:param session_name: Названия tmux-сессии, в которой запущены окружения
    """
    pass

```

Закоммитьте код в соответствующий репозиторий на [gitlab.atp-fivt.org](http://gitlab.atp-fivt.org/).
Программа должна вызываться из консоли и иметь возможность получать аргументы командной строки. Для работы с аргументами командной строки можно использвать `sys.argv` (быстро, но не рекомендуется по codestyle), или же библиотеку [argparse](https://docs.python.org/3/howto/argparse.html).

Как проверить, что всё работает.
1. Сгенерируйте окружения для N пользователей и откройте 2-3 jupyter-ноутбука.
2. Убедитесь, что работа в одном ноутбуке не отражается на других окружениях.
3. Посмотрите логи ноутбука, подключившись к соответствующему окну в tmux-сессии.
Если какой-то из ноутбуков не стартует (а все остальные Ок) есть смысл проверить не занят ли порт (`netstat -nultp`) каким-нибудь другим сервисом.
