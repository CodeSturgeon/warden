from pprint import pprint as pp
from os import system, mkdir, environ
from shutil import copytree, rmtree

DEBUG = True
LISTEN_IP = '127.0.0.1'
LISTEN_PORT = 6666

#CHECKOUT_DIR = '/Users/nick/Projects/git-webhook-ninja/data'
#NIKOLA_CMD = '/Users/nick/Projects/git-webhook-ninja/whenv/bin/nikola'
#SITE_DIR = '/Users/nick/temp/site_gen'
#DOMAIN = '.cloudlockng.com'

print environ
CHECKOUT_DIR = environ['WARDEN_CHECKOUT_DIR']
NIKOLA_CMD = environ['WARDEN_NIKOLA_CMD']
SITE_DIR = environ['WARDEN_SITE_DIR']
DOMAIN = environ['WARDEN_DOMAIN']


def handler(data):
    pp(data.repo_name)
    pp(data.branch_name)
    sitename = data.branch_name + '.' + data.repo_name + DOMAIN
    web_dir = SITE_DIR + '/%s' % sitename
    gen_dir = CHECKOUT_DIR + '/hooktest/sitegen'
    out_dir = gen_dir + '/output'

    c = 'cd %s && %s build' % (gen_dir, NIKOLA_CMD)
    system(c)
    rmtree(web_dir, ignore_errors=True)
    print 'copy!', out_dir
    copytree(out_dir, web_dir)
    print 'copy! done'

PROVIDERS = {}

PROVIDERS['github'] = {
    'whitelist_ips': ['207.97.227.224/27', '173.203.140.192/27',
                       '204.232.175.64/27', '72.4.117.96/27',
                       '192.30.252.0/22', '204.232.175.64/27', '127.0.0.1/32'],
    'local_repo_dir': CHECKOUT_DIR,
    'ssh_account': 'git@github.com',
    'post_receive_handler': handler
}
