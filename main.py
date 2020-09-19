import libtmux
import tqdm
import os
import argparse


server = libtmux.Server()
base_ip = "0.0.0.0"
base_port = 20000


def start(num_users, base_dir='./', session_name='my_fucking_session'):
    """
    Запустить $num_users ноутбуков. У каждого рабочай директория $base_dir+$folder_num
    """
    session = server.new_session(session_name)
    # session.kill_window(0)
    for user in tqdm.tqdm(range(num_users)):
        window = session.new_window(session_name + str(user))
        pane = window.panes[0]
        port = base_port + user
        dir_name = os.path.join(base_dir, str(user))
        token = "user" + str(user)
        pane.send_keys("mkdir {}".format(dir_name))
        pane.send_keys("jupyter notebook --ip {} --port {} --no-browser --NotebookApp.token='{}' --NotebookApp.notebook_dir='{}'".format(base_ip, port, token, dir_name))
    

def stop(num, session_name="my_fucking_session"):
    """
    @:param session_name: Названия tmux-сессии, в которой запущены окружения
    @:param num: номер окружения, кот. можно убить
    """
    session = server.find_where({ "session_name": session_name })
    session.kill_window(num)



def stop_all(session_name="my_fucking_session"):
    """
    @:param session_name: Названия tmux-сессии, в которой запущены окружения
    """
    session = server.find_where({ "session_name": session_name })
    session.kill_session()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process multiple Jupyter notebooks using tmux.')
    parser.add_argument('action', default='start', choices=['start', 'stop', 'stop_all'], help='What do you want to do?')
    parser.add_argument('--num_users', '-nu', type=int, help='Number of notebooks to open')
    parser.add_argument('--num', '-n', type=int, help='Name of tmux window to kill')
    parser.add_argument('--session_name', '-s', default='my_fucking_session', help='Name of tmux-session')
    parser.add_argument('--base_dir', '-d', default='./', help='Directory to create Jupyter notebooks into')

    args = parser.parse_args()

    if args.action == 'start':
        start(args.num_users, args.base_dir, args.session_name)
    elif args.action == 'stop':
        stop(args.num, args.session_name)
    elif args.action == 'stop_all':
        stop_all(args.session_name)
    else:
        print("Nothing happens")