# import os
# import sys
# import pexpect
# def remote_ssh(remote_ip, user, passwd, cmd):
#     ret = -1
#     pexpect.
#     ssh = pexpect.spawnu('ssh %s@%s "%s"' % (user, remote_ip, cmd))
#     try:
#         i = ssh.expect(['password:', 'continue connect (yes/no)?'], timeout = 5)
#         if i == 0:
#             ssh.sendline(passwd)
#         elif i == 1:
#             ssh.sendline('yes\n')
#             ssh.expect('password:')
#             ssh.sendline(passwd)
#         r = ssh.read()
#         print (r)
#         ret = 0
#     except pexpect.EOF:
#         print ("EOF")
#         ssh.close()
#         ret = -1
#     except pexpect.TIMEOUT:
#         print ("TIMEOUT")
#         ssh.close()
#         ret = -2
#     return ret, r
#
# if __name__ == "__main__":
#     ip = "192.168.2.10"
#     user = "gpu"
#     passwd = ""
#     cmd = "df -h"
#     ret, msg = remote_ssh(ip, user, passwd, cmd)
#     print (ret)
#     print (msg)


import paramiko
host='192.168.2.10'
port=22
name='gpu'
passwd='talent2012'
cmd=['/vload/bin/secv_shell','display version']
s=paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(host,port,username=name,password=passwd)
#stdin,stdout,stderr=s.exec_command('/root/test.sh')
stdin,stdout,stderr=s.exec_command('cd kaldi/egs/aidatatang_asr;python3 run_sh.py testAudio/Database/ResDB3.db test3')
# stdin.write("Gpu001\n")
# # stdin.flush()
out=stdout.readlines()
print(out)
for o in out:
    print(o)
