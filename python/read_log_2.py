def read_log(logfile):
    with open(logfile) as f:
        log_obj = f.read()
        print(log_obj)

if __name__ == '__main__':
    read_log('/var/log/auth.log')